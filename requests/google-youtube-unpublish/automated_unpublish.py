#!/usr/bin/env python3
"""
Automated Unpublish Script - Works with Shopify Flow
This script checks for products with a metafield flag and automatically
unpublishes/republishes them from Google & YouTube sales channel.

Designed to run as a scheduled job (cron, scheduled task, etc.)
Works with Shopify Flow that sets: custom.google_ads_exclude = true/false
"""

import json
import os
import sys
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

# Shopify API configuration
SHOPIFY_STORE = os.getenv('SHOPIFY_STORE', 'rudis.myshopify.com')
SHOPIFY_ACCESS_TOKEN = os.getenv('SHOPIFY_ACCESS_TOKEN', '')
SHOPIFY_API_VERSION = '2024-01'  # Update as needed

# Metafield configuration (set by Shopify Flow)
METAFIELD_NAMESPACE = 'custom'
METAFIELD_KEY = 'google_ads_exclude'

# Google & YouTube publication ID
GOOGLE_YOUTUBE_PUBLICATION_ID = os.getenv('GOOGLE_YOUTUBE_PUBLICATION_ID', '')

# Logging
LOG_FILE = Path(__file__).parent / "unpublish_log.json"


def log_action(action: str, product_id: str, status: str, details: str = "") -> None:
    """Log action to file."""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'action': action,
        'product_id': product_id,
        'status': status,
        'details': details
    }
    
    logs = []
    if LOG_FILE.exists():
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
    
    logs.append(log_entry)
    
    # Keep last 1000 entries
    logs = logs[-1000:]
    
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)


def get_publication_id(store: str, token: str) -> str:
    """Get Google & YouTube sales channel publication ID."""
    if GOOGLE_YOUTUBE_PUBLICATION_ID:
        return GOOGLE_YOUTUBE_PUBLICATION_ID
    
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications.json"
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    publications = response.json().get('publications', [])
    
    for pub in publications:
        name = pub.get('name', '').lower()
        if 'google' in name or 'youtube' in name:
            return str(pub['id'])
    
    raise ValueError("Google & YouTube publication not found")


def get_product_metafield(store: str, token: str, product_id: str) -> Optional[bool]:
    """Get google_ads_exclude metafield value for a product."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/products/{product_id}/metafields.json"
    params = {
        'namespace': METAFIELD_NAMESPACE,
        'key': METAFIELD_KEY
    }
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    metafields = response.json().get('metafields', [])
    if metafields:
        value = metafields[0].get('value')
        return value == 'true' or value is True
    
    return None


def get_products_with_metafield(store: str, token: str, exclude: bool) -> List[Dict[str, Any]]:
    """Get all products with google_ads_exclude metafield set to specific value."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/products.json"
    params = {
        'limit': 250,
        'fields': 'id,handle,title'
    }
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    products = []
    page_info = None
    
    while True:
        if page_info:
            params['page_info'] = page_info
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        products_page = data.get('products', [])
        
        # Check metafield for each product
        for product in products_page:
            product_id = product['id']
            metafield_value = get_product_metafield(store, token, str(product_id))
            
            if metafield_value == exclude:
                products.append({
                    'id': product_id,
                    'handle': product.get('handle', ''),
                    'title': product.get('title', '')
                })
        
        # Check for next page
        link_header = response.headers.get('Link', '')
        if 'rel="next"' in link_header:
            # Extract page_info from Link header
            next_link = [l for l in link_header.split(',') if 'rel="next"' in l]
            if next_link:
                # Extract page_info from URL
                import re
                match = re.search(r'page_info=([^&>]+)', next_link[0])
                if match:
                    page_info = match.group(1)
                else:
                    break
            else:
                break
        else:
            break
    
    return products


def is_product_published(store: str, token: str, product_id: str, publication_id: str) -> bool:
    """Check if product is published to the publication."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications.json"
    params = {'product_id': product_id}
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    product_publications = response.json().get('product_publications', [])
    return len(product_publications) > 0


def unpublish_product(store: str, token: str, product_id: str, publication_id: str) -> bool:
    """Unpublish a product from a publication."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications.json"
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    # Get existing product publication
    params = {'product_id': product_id}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    product_publications = response.json().get('product_publications', [])
    if not product_publications:
        return False  # Not published
    
    # Delete the product publication
    product_pub_id = product_publications[0]['id']
    delete_url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications/{product_pub_id}.json"
    
    response = requests.delete(delete_url, headers=headers)
    response.raise_for_status()
    
    return True


def publish_product(store: str, token: str, product_id: str, publication_id: str) -> bool:
    """Publish a product to a publication."""
    url = f"https://{store}/admin/api/{SHOPIFY_API_VERSION}/publications/{publication_id}/product_publications.json"
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'product_publication': {
            'product_id': product_id
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    
    return True


def main():
    """Main execution - processes products based on metafield flag."""
    if not SHOPIFY_ACCESS_TOKEN:
        print("ERROR: SHOPIFY_ACCESS_TOKEN not set")
        sys.exit(1)
    
    print("Getting Google & YouTube publication ID...")
    publication_id = get_publication_id(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN)
    print(f"✅ Publication ID: {publication_id}")
    
    print("\nFinding products to unpublish (google_ads_exclude = true)...")
    products_to_unpublish = get_products_with_metafield(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, True)
    print(f"Found {len(products_to_unpublish)} products to unpublish")
    
    print("\nFinding products to republish (google_ads_exclude = false)...")
    products_to_republish = get_products_with_metafield(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, False)
    print(f"Found {len(products_to_republish)} products to republish")
    
    # Unpublish products
    print("\n" + "="*60)
    print("Unpublishing products...")
    unpublished_count = 0
    for product in products_to_unpublish:
        product_id = str(product['id'])
        if is_product_published(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, product_id, publication_id):
            try:
                unpublish_product(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, product_id, publication_id)
                print(f"✅ Unpublished: {product['handle']} ({product_id})")
                log_action('unpublish', product_id, 'success', product['handle'])
                unpublished_count += 1
            except Exception as e:
                print(f"❌ Error unpublishing {product['handle']}: {e}")
                log_action('unpublish', product_id, 'error', str(e))
        else:
            print(f"⚠️  Already unpublished: {product['handle']}")
    
    # Republish products
    print("\n" + "="*60)
    print("Republishing products...")
    republished_count = 0
    for product in products_to_republish:
        product_id = str(product['id'])
        if not is_product_published(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, product_id, publication_id):
            try:
                publish_product(SHOPIFY_STORE, SHOPIFY_ACCESS_TOKEN, product_id, publication_id)
                print(f"✅ Republished: {product['handle']} ({product_id})")
                log_action('republish', product_id, 'success', product['handle'])
                republished_count += 1
            except Exception as e:
                print(f"❌ Error republishing {product['handle']}: {e}")
                log_action('republish', product_id, 'error', str(e))
        else:
            print(f"⚠️  Already published: {product['handle']}")
    
    print("\n" + "="*60)
    print("Summary:")
    print(f"  Unpublished: {unpublished_count}")
    print(f"  Republished: {republished_count}")
    print(f"  Log file: {LOG_FILE}")


if __name__ == '__main__':
    main()

