#!/usr/bin/env python3
"""
Product Inventory Analysis
Analyzes products CSV to understand inventory patterns and identify products
with out-of-stock variants across styles and sizes.
"""

import csv
import json
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

# Path to products CSV (pre-filtered to Active products only)
PRODUCTS_CSV = Path(__file__).parent / "AD_ACTIVE-PRODUCTS_Export_2025-11-04_141820" / "Products.csv"
OUTPUT_DIR = Path(__file__).parent
OUTPUT_JSON = OUTPUT_DIR / "inventory_analysis.json"
OUTPUT_CSV = OUTPUT_DIR / "inventory_analysis.csv"
OUTPUT_REPORT = OUTPUT_DIR / "inventory_analysis_report.md"


def read_products_csv(csv_path: Path) -> List[Dict[str, Any]]:
    """Read and parse products CSV file."""
    products = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products


def get_variant_inventory_qty(row: Dict[str, str]) -> int:
    """Get variant inventory quantity from CSV row."""
    qty_str = row.get('Variant Inventory Qty', '0').strip()
    if not qty_str or qty_str == '':
        return 0
    try:
        qty = int(float(qty_str))
        return max(0, qty)
    except (ValueError, TypeError):
        return 0


def analyze_inventory(products: List[Dict[str, str]]) -> Dict[str, Any]:
    """Analyze inventory patterns across products."""
    
    # Group variants by product ID
    product_variants = defaultdict(list)
    
    for row in products:
        product_id = row.get('ID', '').strip()
        if not product_id:
            continue
            
        variant_id = row.get('Variant ID', '').strip()
        variant_sku = row.get('Variant SKU', '').strip()
        option1_name = row.get('Option1 Name', '').strip()
        option1_value = row.get('Option1 Value', '').strip()
        option2_name = row.get('Option2 Name', '').strip()
        option2_value = row.get('Option2 Value', '').strip()
        option3_name = row.get('Option3 Name', '').strip()
        option3_value = row.get('Option3 Value', '').strip()
        
        inventory_qty = get_variant_inventory_qty(row)
        
        variant_info = {
            'variant_id': variant_id,
            'variant_sku': variant_sku,
            'option1_name': option1_name,
            'option1_value': option1_value,
            'option2_name': option2_name,
            'option2_value': option2_value,
            'option3_name': option3_name,
            'option3_value': option3_value,
            'inventory_qty': inventory_qty,
            'is_in_stock': inventory_qty > 0,
            'is_out_of_stock': inventory_qty <= 0
        }
        
        product_variants[product_id].append(variant_info)
    
    # Analyze each product
    products_with_oos = []
    inventory_stats = {
        'total_products': len(product_variants),
        'products_analyzed': 0,
        'products_active': 0,
        'products_inactive': 0,
        'products_with_oos_variants': 0,
        'products_fully_in_stock': 0,
        'products_fully_out_of_stock': 0,
        'total_variants': 0,
        'total_in_stock_variants': 0,
        'total_out_of_stock_variants': 0
    }
    
    # Track patterns
    style_size_patterns = defaultdict(lambda: {'total': 0, 'oos': 0})
    
    for product_id, variants in product_variants.items():
        # Get product info from first variant row
        product_row = next((r for r in products if r.get('ID', '').strip() == product_id), None)
        if not product_row:
            continue
        
        # Verify product is Active (CSV is pre-filtered, but double-check)
        status = product_row.get('Status', '').strip()
        if status != 'Active':
            inventory_stats['products_inactive'] += 1
            continue
        
        inventory_stats['products_active'] += 1
        
        total_variants = len(variants)
        in_stock_count = sum(1 for v in variants if v['is_in_stock'])
        out_of_stock_count = sum(1 for v in variants if v['is_out_of_stock'])
        
        inventory_stats['products_analyzed'] += 1
        inventory_stats['total_variants'] += total_variants
        inventory_stats['total_in_stock_variants'] += in_stock_count
        inventory_stats['total_out_of_stock_variants'] += out_of_stock_count
        
        if out_of_stock_count == 0:
            inventory_stats['products_fully_in_stock'] += 1
        elif out_of_stock_count == total_variants:
            inventory_stats['products_fully_out_of_stock'] += 1
        else:
            inventory_stats['products_with_oos_variants'] += 1
        
        # Analyze by style/size if product has out-of-stock variants
        if out_of_stock_count > 0:
            # Group by option combinations to find patterns
            option1_values = set(v['option1_value'] for v in variants if v['option1_value'])
            option2_values = set(v['option2_value'] for v in variants if v['option2_value'])
            
            # Analyze patterns
            style_oos = defaultdict(int)  # option1 (usually color/style) -> OOS count
            size_oos = defaultdict(int)   # option2 (usually size) -> OOS count
            
            for variant in variants:
                if variant['is_out_of_stock']:
                    if variant['option1_value']:
                        style_oos[variant['option1_value']] += 1
                    if variant['option2_value']:
                        size_oos[variant['option2_value']] += 1
            
            product_info = {
                'product_id': product_id,
                'handle': product_row.get('Handle', '').strip(),
                'title': product_row.get('Title', '').strip(),
                'url': product_row.get('URL', '').strip(),
                'status': product_row.get('Status', '').strip(),
                'published': product_row.get('Published', '').strip(),
                'total_variants': total_variants,
                'in_stock_variants': in_stock_count,
                'out_of_stock_variants': out_of_stock_count,
                'inventory_percentage': round((in_stock_count / total_variants) * 100, 1) if total_variants > 0 else 0,
                'option1_name': variants[0]['option1_name'] if variants else '',
                'option2_name': variants[0]['option2_name'] if variants else '',
                'option1_values': sorted(option1_values),
                'option2_values': sorted(option2_values),
                'style_oos_breakdown': dict(style_oos),
                'size_oos_breakdown': dict(size_oos),
                'variants': variants
            }
            
            products_with_oos.append(product_info)
    
    # Sort by OOS count (descending) then by inventory percentage (ascending)
    products_with_oos.sort(key=lambda x: (x['out_of_stock_variants'], -x['inventory_percentage']), reverse=True)
    
    return {
        'stats': inventory_stats,
        'products_with_oos': products_with_oos
    }


def generate_json_output(analysis: Dict[str, Any]) -> None:
    """Generate JSON output file."""
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)


def generate_csv_output(analysis: Dict[str, Any]) -> None:
    """Generate CSV output file for easy import/review."""
    products = analysis['products_with_oos']
    
    with open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'Product ID',
            'Handle',
            'Title',
            'URL',
            'Status',
            'Published',
            'Total Variants',
            'In Stock Variants',
            'Out of Stock Variants',
            'Inventory %',
            'Option 1 Name',
            'Option 2 Name',
            'Option 1 Values',
            'Option 2 Values'
        ])
        writer.writeheader()
        
        for product in products:
            writer.writerow({
                'Product ID': product['product_id'],
                'Handle': product['handle'],
                'Title': product['title'],
                'URL': product['url'],
                'Status': product['status'],
                'Published': product['published'],
                'Total Variants': product['total_variants'],
                'In Stock Variants': product['in_stock_variants'],
                'Out of Stock Variants': product['out_of_stock_variants'],
                'Inventory %': product['inventory_percentage'],
                'Option 1 Name': product['option1_name'],
                'Option 2 Name': product['option2_name'],
                'Option 1 Values': ', '.join(product['option1_values']),
                'Option 2 Values': ', '.join(product['option2_values'])
            })


def generate_report(analysis: Dict[str, Any]) -> None:
    """Generate markdown report."""
    stats = analysis['stats']
    products = analysis['products_with_oos']
    
    # Calculate some additional insights
    partial_oos = [p for p in products if p['out_of_stock_variants'] > 0 and p['in_stock_variants'] > 0]
    mostly_oos = [p for p in products if p['inventory_percentage'] < 50]
    
    report_lines = [
        "# Inventory Analysis Report - Active Products Only",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Filter",
        "",
        "**Using pre-filtered CSV with Active products only**",
        "",
        "## Overall Statistics",
        "",
        f"- **Total Products in Catalog:** {stats['total_products']:,}",
        f"- **Active Products Analyzed:** {stats['products_active']:,}",
        f"- **Inactive Products Skipped:** {stats['products_inactive']:,}",
        f"- **Total Variants Analyzed:** {stats['total_variants']:,}",
        f"- **Total In-Stock Variants:** {stats['total_in_stock_variants']:,}",
        f"- **Total Out-of-Stock Variants:** {stats['total_out_of_stock_variants']:,}",
        "",
        "## Product Inventory Health (Active Products)",
        "",
        f"- **Products Fully In Stock:** {stats['products_fully_in_stock']:,} ({stats['products_fully_in_stock']/stats['products_active']*100:.1f}%)" if stats['products_active'] > 0 else "- **Products Fully In Stock:** 0",
        f"- **Products Fully Out of Stock:** {stats['products_fully_out_of_stock']:,} ({stats['products_fully_out_of_stock']/stats['products_active']*100:.1f}%)" if stats['products_active'] > 0 else "- **Products Fully Out of Stock:** 0",
        f"- **Products with Mixed Inventory:** {stats['products_with_oos_variants']:,} ({stats['products_with_oos_variants']/stats['products_active']*100:.1f}%)" if stats['products_active'] > 0 else "- **Products with Mixed Inventory:** 0",
        "",
        "## Products with Out-of-Stock Variants",
        "",
        f"**Total Active Products with OOS Variants:** {len(products):,}",
        f"- **Products with Partial Inventory:** {len(partial_oos):,} (have both in-stock and out-of-stock variants)",
        f"- **Products Mostly Out of Stock (<50% inventory):** {len(mostly_oos):,}",
        "",
        "## Top Products by Out-of-Stock Count",
        "",
        "| Product ID | Handle | Title | Total | In Stock | OOS | Inventory % |",
        "|------------|--------|-------|-------|----------|-----|-------------|"
    ]
    
    # Show top 50 products with most OOS variants
    for product in products[:50]:
        report_lines.append(
            f"| {product['product_id']} | `{product['handle']}` | {product['title'][:40]} | "
            f"{product['total_variants']} | {product['in_stock_variants']} | "
            f"{product['out_of_stock_variants']} | {product['inventory_percentage']}% |"
        )
    
    if len(products) > 50:
        report_lines.append(f"\n*... and {len(products) - 50} more products*")
    
    report_lines.extend([
        "",
        "## Analysis Notes",
        "",
        "- This analysis identifies products with broken inventory patterns across styles and sizes",
        "- Products with mixed inventory (some variants in stock, some out) may indicate inventory management issues",
        "- Review the CSV file for detailed breakdown by style/size options",
        "",
        "## Files Generated",
        "",
        f"- `{OUTPUT_JSON.name}` - Full analysis data in JSON format",
        f"- `{OUTPUT_CSV.name}` - Products list in CSV format with inventory breakdown",
        f"- `{OUTPUT_REPORT.name}` - This report"
    ])
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))


def main():
    """Main execution function."""
    print("Reading products CSV...")
    if not PRODUCTS_CSV.exists():
        print(f"ERROR: Products CSV not found at {PRODUCTS_CSV}")
        return
    
    products = read_products_csv(PRODUCTS_CSV)
    print(f"Loaded {len(products):,} product variant rows")
    
    print("Analyzing inventory patterns...")
    analysis = analyze_inventory(products)
    
    stats = analysis['stats']
    print(f"\nInventory Summary:")
    print(f"  Total Products: {stats['products_analyzed']:,}")
    print(f"  Products with OOS variants: {stats['products_with_oos_variants']:,}")
    print(f"  Products fully in stock: {stats['products_fully_in_stock']:,}")
    print(f"  Products fully out of stock: {stats['products_fully_out_of_stock']:,}")
    
    print("\nGenerating output files...")
    generate_json_output(analysis)
    generate_csv_output(analysis)
    generate_report(analysis)
    
    print(f"\n✅ Analysis complete!")
    print(f"   - JSON: {OUTPUT_JSON}")
    print(f"   - CSV: {OUTPUT_CSV}")
    print(f"   - Report: {OUTPUT_REPORT}")


if __name__ == '__main__':
    main()

