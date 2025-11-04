#!/usr/bin/env python3
"""
Product Inventory Analysis - Google & YouTube Unpublish
Analyzes products CSV to identify products with 5 or fewer in-stock variants
for unpublishing from Google & YouTube sales channel.
"""

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Path to products CSV
PRODUCTS_CSV = Path(__file__).parent.parent.parent / "data" / "AD_PRODUCTS_Export_2025-11-04_095613" / "Products.csv"
OUTPUT_DIR = Path(__file__).parent
OUTPUT_JSON = OUTPUT_DIR / "products_to_unpublish.json"
OUTPUT_CSV = OUTPUT_DIR / "products_to_unpublish.csv"
OUTPUT_REPORT = OUTPUT_DIR / "unpublish_analysis_report.md"


def read_products_csv(csv_path: Path) -> List[Dict[str, Any]]:
    """Read and parse products CSV file."""
    products = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products


def get_variant_inventory_qty(row: Dict[str, str]) -> int:
    """Get variant inventory quantity from CSV row.
    
    Checks 'Variant Inventory Qty' field. If empty or invalid, returns 0.
    """
    qty_str = row.get('Variant Inventory Qty', '0').strip()
    if not qty_str or qty_str == '':
        return 0
    try:
        qty = int(float(qty_str))
        return max(0, qty)  # Ensure non-negative
    except (ValueError, TypeError):
        return 0


def analyze_products(products: List[Dict[str, str]]) -> Dict[str, Any]:
    """Analyze products to find those with 5 or fewer in-stock variants."""
    
    # Group variants by product ID
    product_variants = defaultdict(list)
    
    for row in products:
        # Handle BOM in CSV header - utf-8-sig should handle it, but just in case
        product_id = row.get('ID', '').strip()
        if not product_id:
            continue
            
        variant_id = row.get('Variant ID', '').strip()
        variant_sku = row.get('Variant SKU', '').strip()
        variant_title = f"{row.get('Option1 Value', '')} / {row.get('Option2 Value', '')} / {row.get('Option3 Value', '')}".strip(' / ')
        
        inventory_qty = get_variant_inventory_qty(row)
        
        variant_info = {
            'variant_id': variant_id,
            'variant_sku': variant_sku,
            'variant_title': variant_title or 'Default Title',
            'inventory_qty': inventory_qty,
            'is_in_stock': inventory_qty > 0
        }
        
        product_variants[product_id].append(variant_info)
    
    # Analyze each product
    products_to_unpublish = []
    product_stats = {
        'total_products': len(product_variants),
        'products_analyzed': 0,
        'products_with_5_or_fewer_in_stock': 0,
        'total_variants_analyzed': 0,
        'total_in_stock_variants': 0,
        'total_out_of_stock_variants': 0
    }
    
    for product_id, variants in product_variants.items():
        # Get product info from first variant row
        product_row = next((r for r in products if r.get('ID', '').strip() == product_id), None)
        if not product_row:
            continue
        
        # Count in-stock variants
        in_stock_count = sum(1 for v in variants if v['is_in_stock'])
        out_of_stock_count = sum(1 for v in variants if not v['is_in_stock'])
        total_variants = len(variants)
        
        product_stats['products_analyzed'] += 1
        product_stats['total_variants_analyzed'] += total_variants
        product_stats['total_in_stock_variants'] += in_stock_count
        product_stats['total_out_of_stock_variants'] += out_of_stock_count
        
        # If 5 or fewer variants are in stock, mark for unpublish
        if in_stock_count <= 5:
            product_stats['products_with_5_or_fewer_in_stock'] += 1
            
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
                'variants': variants
            }
            
            products_to_unpublish.append(product_info)
    
    return {
        'stats': product_stats,
        'products_to_unpublish': products_to_unpublish
    }


def generate_json_output(analysis: Dict[str, Any]) -> None:
    """Generate JSON output file."""
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)


def generate_csv_output(analysis: Dict[str, Any]) -> None:
    """Generate CSV output file for easy import/review."""
    products = analysis['products_to_unpublish']
    
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
            'Out of Stock Variants'
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
                'Out of Stock Variants': product['out_of_stock_variants']
            })


def generate_report(analysis: Dict[str, Any]) -> None:
    """Generate markdown report."""
    stats = analysis['stats']
    products = analysis['products_to_unpublish']
    
    report_lines = [
        "# Google & YouTube Unpublish Analysis",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
        f"- **Total Products Analyzed:** {stats['products_analyzed']:,}",
        f"- **Total Variants Analyzed:** {stats['total_variants_analyzed']:,}",
        f"- **Total In-Stock Variants:** {stats['total_in_stock_variants']:,}",
        f"- **Total Out-of-Stock Variants:** {stats['total_out_of_stock_variants']:,}",
        f"- **Products with ≤5 In-Stock Variants:** {stats['products_with_5_or_fewer_in_stock']:,}",
        "",
        "## Criteria",
        "",
        "Products are flagged for unpublishing from Google & YouTube sales channel if they have **5 or fewer in-stock variants** (inventory quantity > 0).",
        "",
        "This ensures products with limited size availability are not shown in Google Shopping.",
        "",
        "## Products to Unpublish",
        "",
        f"**Total Products:** {len(products)}",
        "",
        "| Product ID | Handle | Title | Total Variants | In Stock | Out of Stock | URL |",
        "|------------|--------|-------|----------------|----------|---------------|-----|"
    ]
    
    # Sort by in-stock count (ascending) then by total variants (descending)
    sorted_products = sorted(products, key=lambda x: (x['in_stock_variants'], -x['total_variants']))
    
    for product in sorted_products:
        report_lines.append(
            f"| {product['product_id']} | `{product['handle']}` | {product['title'][:50]} | "
            f"{product['total_variants']} | {product['in_stock_variants']} | "
            f"{product['out_of_stock_variants']} | [View]({product['url']}) |"
        )
    
    report_lines.extend([
        "",
        "## Next Steps",
        "",
        "1. Review the products listed above",
        "2. Use the Shopify Admin API or GraphQL to unpublish these products from Google & YouTube sales channel",
        "3. See `unpublish_products.py` for an automated script (requires API credentials)",
        "",
        "## Files Generated",
        "",
        f"- `{OUTPUT_JSON.name}` - Full analysis data in JSON format",
        f"- `{OUTPUT_CSV.name}` - Products list in CSV format for easy review",
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
    
    print("Analyzing products...")
    analysis = analyze_products(products)
    
    print(f"Found {analysis['stats']['products_with_5_or_fewer_in_stock']} products with ≤5 in-stock variants")
    
    print("Generating output files...")
    generate_json_output(analysis)
    generate_csv_output(analysis)
    generate_report(analysis)
    
    print(f"\n✅ Analysis complete!")
    print(f"   - JSON: {OUTPUT_JSON}")
    print(f"   - CSV: {OUTPUT_CSV}")
    print(f"   - Report: {OUTPUT_REPORT}")


if __name__ == '__main__':
    main()

