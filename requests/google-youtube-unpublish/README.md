# Inventory Analysis - Out of Stock Variants

## Context

This analysis identifies products with out-of-stock variants to understand inventory patterns across core styles and sizes. This helps identify broken inventory patterns and products that may need attention.

## Files

- **`analyze_inventory.py`** - Analyzes products CSV to identify inventory patterns and out-of-stock variants
- **`analyze_products.py`** - Original script (identifies products with ≤5 in-stock variants for unpublishing)
- **`unpublish_products.py`** - Script to unpublish products from Google & YouTube sales channel via Shopify API
- **`inventory_analysis.json`** - Full inventory analysis data in JSON format (generated)
- **`inventory_analysis.csv`** - Products list with inventory breakdown in CSV format (generated)
- **`inventory_analysis_report.md`** - Inventory analysis report with findings (generated)

## Source Data

- **Products CSV:** `../../data/AD_PRODUCTS_Export_2025-11-04_095613/Products.csv`

## Running the Inventory Analysis

```bash
python3 analyze_inventory.py
```

The script will:
1. Read the products CSV export
2. Group variants by product ID
3. Analyze inventory patterns across styles and sizes
4. Identify products with out-of-stock variants
5. Generate output files (JSON, CSV, and markdown report)

## What This Analysis Shows

- **Products with out-of-stock variants** - Products that have some but not all variants out of stock
- **Inventory breakdown by style/size** - How inventory is distributed across option values
- **Inventory health metrics** - Percentage of variants in stock per product
- **Pattern identification** - Products with broken inventory patterns across core styles and sizes

This helps identify:
- Products where specific colors/styles are out of stock
- Products where specific sizes are out of stock
- Products with inventory management issues
- Overall inventory health across the catalog

## Unpublishing Products

### Prerequisites

1. **Shopify API Access Token** - Required for API calls
2. **Google & YouTube Publication ID** - Can be auto-detected or set manually

### Setup

Set environment variables:

```bash
export SHOPIFY_STORE='rudis.myshopify.com'
export SHOPIFY_ACCESS_TOKEN='your-access-token'
export GOOGLE_YOUTUBE_PUBLICATION_ID='publication-id'  # Optional, will auto-detect if not set
```

### Dry Run (Recommended First)

Test the script without making changes:

```bash
python3 unpublish_products.py --dry-run
```

### Execute Unpublish

```bash
python3 unpublish_products.py
```

The script will:
1. Load products from the analysis JSON file
2. Get the Google & YouTube publication ID (if not set)
3. Ask for confirmation
4. Unpublish each product from the sales channel
5. Provide a summary of results

## Shopify API Notes

### Publication Endpoints

The script uses Shopify's Publication API:
- `GET /admin/api/{version}/publications.json` - List all publications
- `GET /admin/api/{version}/publications/{id}/product_publications.json` - Get product publications
- `DELETE /admin/api/{version}/publications/{id}/product_publications/{product_pub_id}.json` - Unpublish product

### Finding Publication ID Manually

1. Go to Shopify Admin → Settings → Sales channels
2. Find "Google & YouTube" channel
3. Or use GraphQL Admin API:
   ```graphql
   query {
     publications(first: 10) {
       edges {
         node {
           id
           name
         }
       }
     }
   }
   ```

## Alternative Methods

### Manual Unpublish (Shopify Admin)

1. Go to Shopify Admin → Products
2. Filter by the products in `products_to_unpublish.csv`
3. For each product:
   - Click product → Sales channels
   - Uncheck "Google & YouTube"
   - Save

### Bulk Edit (Shopify Admin)

1. Select multiple products from the CSV
2. Use bulk editor to unpublish from Google & YouTube channel
3. Apply changes

### GraphQL Alternative

If you prefer GraphQL, you can use the Shopify GraphQL Admin API:

```graphql
mutation unpublishProduct($publicationId: ID!, $productId: ID!) {
  publicationUnpublish(
    id: $publicationId
    productId: $productId
  ) {
    publishedPublication {
      id
    }
    userErrors {
      field
      message
    }
  }
}
```

## Next Steps

1. **Review the analysis** - Check `unpublish_analysis_report.md` for the list of products
2. **Verify products** - Ensure these products should indeed be unpublished
3. **Execute unpublish** - Use the script or manual method above
4. **Monitor results** - Check Google Merchant Center for updates
5. **Re-publish later** - When inventory is restored, products can be re-published

## Notes

- Unpublishing removes products from Google Shopping but doesn't delete them from Shopify
- Products can be re-published at any time
- This is a one-time analysis based on the export date
- Consider automating this check if inventory levels change frequently

