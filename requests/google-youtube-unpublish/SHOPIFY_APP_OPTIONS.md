# Shopify App Store Feed Solutions

## Shopify App Store Options

Based on research, here are Shopify App Store apps that might support inventory-based filtering:

### FeedHub: Google Shopping Feed
- **Shopify App Store:** Available
- **Features:**
  - Automated product feed generation
  - Real-time synchronization
  - Large catalog support
- **Question:** Does it support inventory-based filtering rules?
- **Action:** Check if they support custom rules for excluding products based on variant count

### ShoppingFeeder Google Shopping
- **Shopify App Store:** Available
- **Features:**
  - Multi-channel support
  - Feed optimization
  - Multi-language/currency
- **Question:** Can filter products based on inventory rules?
- **Action:** Contact them about inventory-based exclusion rules

### Multifeed Google Shopping Feed
- **Shopify App Store:** Available
- **Features:**
  - Multi-channel feeds
  - Attribute mapping
  - Rules and filters
- **Question:** Do their rules support inventory calculations?
- **Action:** Verify if they can exclude products with ≤5 in-stock variants

### Feedmanager – Shopping Feeds
- **Shopify App Store:** Available
- **Features:**
  - Pre-mapped channel settings
  - Advanced filters and rules
  - Customization options
- **Question:** Do their filters support variant inventory calculations?
- **Action:** Check documentation for inventory-based filtering

## Limitations of Shopify App Store Apps

**Most Shopify feed apps are designed for:**
- Basic feed generation
- Data transformation
- Multi-channel distribution

**They typically DON'T support:**
- Complex inventory calculations (like counting in-stock variants)
- Dynamic rules based on calculated values
- Real-time inventory-based filtering

**Why:**
- Apps operate on product data, not variant-level inventory aggregations
- Calculating "number of in-stock variants" requires logic the apps don't have
- Most apps filter on existing product attributes, not calculated values

## Potential Workaround with Shopify Apps

**If an app supports custom fields/metafields:**

1. **Shopify Flow** calculates in-stock variant count
2. Flow sets metafield: `custom.in_stock_variant_count = [number]`
3. Feed app filters products where `in_stock_variant_count <= 5`

**Pros:**
- Uses Shopify-native Flow
- No external scripts
- Feed app handles filtering

**Cons:**
- Requires Flow to calculate variant count (complex)
- Flow has limitations on complex calculations
- May not be real-time

## Recommendation: Feed Management Platform

**For this specific use case, a dedicated feed management platform is likely needed because:**

1. **Complex Inventory Rules** - Need to calculate "number of in-stock variants" per product
2. **Real-time Updates** - Need feed to update immediately when inventory changes
3. **Rule Engine** - Need powerful rules engine that can handle calculations
4. **No External Scripts** - Want everything managed within platform

**Shopify App Store apps are typically not powerful enough for this use case.**

