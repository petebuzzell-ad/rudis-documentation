#!/usr/bin/env python3
"""
Unpublish Products from Google & YouTube Sales Channel
Uses Shopify Admin API to unpublish products identified in the analysis.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any
import requests

# Path to analysis results
ANALYSIS_JSON = Path(__file__).parent / "products_to_unpublish.json"

# Shopify API configuration
# Set these via environment variables or modify directly
SHOPIFY_STORE = os.getenv('SHOPIFY_STORE', 'rudis.myshopify.com')
SHOPIFY_ACCESS_TOKEN = os.getenv('SHOPIFY_ACCESS_TOKEN', '')
SHOPIFY_API_VERSION = '2024-01'  # Update as needed

# Google & YouTube sales channel publication ID
# This needs to be determined via API or Shopify admin
GOOGLE_YOUTUBE_PUBLICATION_ID = os.getenv('GOOGLE_YOUTUBE_PUBLICATION_ID', '')


def get_publication_id(store: str, token: str) -> str:
    """Get Google & YouTube sales channel publication ID."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications.json"
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    publications = response.json().get('publications', [])
    
    # Find Google & YouTube publication
    for pub in publications:
        name = pub.get('name', '').lower()
        if 'google' in name or 'youtube' in name:
            return pub['id']
    
    raise ValueError("Google & YouTube publication not found. Please set GOOGLE_YOUTUBE_PUBLICATION_ID manually.")


def unpublish_product(
    store: str,
    token: str,
    product_id: str,
    publication_id: str
) -> bool:
    """Unpublish a product from a specific sales channel publication."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications.json"
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    # First, get existing product publication to find its ID
    get_url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications.json"
    params = {'product_id': product_id}
    
    response = requests.get(get_url, headers=headers, params=params)
    response.raise_for_status()
    
    product_publications = response.json().get('product_publications', [])
    
    if not product_publications:
        print(f"  ⚠️  Product {product_id} not published to this channel")
        return False
    
    # Delete the product publication
    product_pub_id = product_publications[0]['id']
    delete_url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications/{product_pub_id}.json"
    
    response = requests.delete(delete_url, headers=headers)
    response.raise_for_status()
    
    return True


def unpublish_products_batch(
    store: str,
    token: str,
    publication_id: str,
    product_ids: List[str],
    dry_run: bool = True
) -> Dict[str, Any]:
    """Unpublish multiple products from Google & YouTube sales channel."""
    results = {
        'total': len(product_ids),
        'success': 0,
        'failed': 0,
        'not_published': 0,
        'errors': []
    }
    
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print(f"   Would unpublish {len(product_ids)} products\n")
    
    for i, product_id in enumerate(product_ids, 1):
        print(f"[{i}/{len(product_ids)}] Processing product {product_id}...", end=' ')
        
        if dry_run:
            print("✅ (dry run)")
            results['success'] += 1
            continue
        
        try:
            success = unpublish_product(store, token, product_id, publication_id)
            if success:
                print("✅ Unpublished")
                results['success'] += 1
            else:
                print("⚠️  Not published")
                results['not_published'] += 1
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            results['failed'] += 1
            results['errors'].append({
                'product_id': product_id,
                'error': str(e)
            })
    
    return results


def main():
    """Main execution function."""
    # Check for API credentials
    if not SHOPIFY_ACCESS_TOKEN:
        print("ERROR: SHOPIFY_ACCESS_TOKEN not set")
        print("Set it via environment variable: export SHOPIFY_ACCESS_TOKEN='your-token'")
        sys.exit(1)
    
    # Load analysis results
    if not ANALYSIS_JSON.exists():
        print(f"ERROR: Analysis file not found: {ANALYSIS_JSON}")
        print("Run analyze_products.py first to generate the analysis.")
        sys.exit(1)
    
    with open(ANALYSIS_JSON, 'r') as f:
        analysis = json.load(f)
    
    products = analysis.get('products_to_unpublish', [])
    
    if not products:
        print("No products to unpublish.")
        return
    
    print(f"Found {len(products)} products to unpublish")
    
    # Get publication ID
    publication_id = GOOGLE_YOUTUBE_PUBLICATION_ID
    if not publication_id:
        print("Getting Google & YouTube publication ID...")
        try:
            publication_id = get_publication_id(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN)
            print(f"✅ Found publication ID: {publication_id}")
        except Exception as e:
            print(f"ERROR: Could not get publication ID: {e}")
            print("Please set GOOGLE_YOUTUBE_PUBLICATION_ID manually")
            sys.exit(1)
    
    # Extract product IDs
    product_ids = [p['product_id'] for p in products]
    
    # Ask for confirmation
    print(f"\n⚠️  About to unpublish {len(product_ids)} products from Google & YouTube")
    print("   This action cannot be easily undone.")
    
    if '--dry-run' not in sys.argv:
        response = input("\nContinue? (yes/no): ")
        if response.lower() != 'yes':
            print("Cancelled.")
            return
        dry_run = False
    else:
        dry_run = True
    
    # Unpublish products
    print("\nUnpublishing products...\n")
    results = unpublish_products_batch(
        SHOPIFY_STORE,
        SHOPIFY_ACCESS_TOKEN,
        publication_id,
        product_ids,
        dry_run=dry_run
    )
    
    # Print summary
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"  Total: {results['total']}")
    print(f"  Success: {results['success']}")
    print(f"  Failed: {results['failed']}")
    print(f"  Not Published: {results['not_published']}")
    
    if results['errors']:
        print(f"\nErrors ({len(results['errors'])}):")
        for error in results['errors'][:10]:  # Show first 10
            print(f"  - Product {error['product_id']}: {error['error']}")
        if len(results['errors']) > 10:
            print(f"  ... and {len(results['errors']) - 10} more")


if __name__ == '__main__':
    main()

