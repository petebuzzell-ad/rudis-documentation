# Feed Management & Alternative Solutions

## Current State

**Current Setup:**
- Shopify native Google & YouTube sales channel (Managed Markets)
- Direct feed from Shopify → Google Merchant Center
- No feed filtering or management layer

**Problem:**
- Cannot exclude products based on inventory rules
- Shopify Flow cannot unpublish from sales channels
- No way to filter feed before it reaches Google

## Solution Options

### Option 1: Feed Management Platform (Recommended)

**What it is:** Third-party service that sits between Shopify and Google Merchant Center. They pull your product feed, apply rules/filters, then send a filtered feed to Google.

**Top Platforms:**

#### Feedonomics
- **Pricing:** Custom (enterprise pricing, typically $500-2000+/month)
- **Features:**
  - Real-time inventory filtering
  - Custom rules engine (can exclude products with ≤5 in-stock variants)
  - Automatic feed updates
  - Multi-channel support (Google, Facebook, Bing, etc.)
  - Advanced data transformation
- **Pros:**
  - Most robust solution
  - Handles complex inventory rules
  - Real-time updates
  - No external scripts needed
- **Cons:**
  - Higher cost
  - Learning curve
  - Additional platform to manage

#### DataFeedWatch
- **Pricing:** $99-299/month (varies by plan)
- **Features:**
  - Inventory-based filtering rules
  - Custom product rules
  - Feed optimization
  - Multi-channel support
- **Pros:**
  - More affordable than Feedonomics
  - Good for inventory-based exclusions
- **Cons:**
  - Less robust than Feedonomics
  - May have limitations on complex rules

#### GoDataFeed
- **Pricing:** $99-299/month
- **Features:**
  - Inventory filtering
  - Custom rules
  - Feed management
- **Pros:**
  - Affordable option
  - Established platform
- **Cons:**
  - Less feature-rich than Feedonomics

#### AdNabu
- **Pricing:** $99-199/month
- **Features:**
  - Google Shopping feed management
  - Inventory-based rules
  - Feed optimization
- **Pros:**
  - Affordable
  - Focused on Google Shopping
- **Cons:**
  - Less comprehensive than others

**Implementation Approach:**
1. Connect Shopify store to feed platform
2. Set up rule: "Exclude products where (in-stock variants) ≤ 5"
3. Feed platform generates filtered feed
4. Feed platform sends to Google Merchant Center
5. Disable native Shopify Google & YouTube channel feed

**Key Rule Example (Feedonomics):**
```
IF product.in_stock_variant_count <= 5
THEN exclude_from_feed
```

### Option 2: Google Merchant Center Feed Rules

**What it is:** Google Merchant Center has built-in feed rules that can filter products based on attributes.

**Limitations:**
- Cannot calculate "number of in-stock variants" dynamically
- Can only filter on existing product attributes/metafields
- Would require Shopify Flow to set a metafield (which brings us back to the original problem)

**Workaround:**
- Flow sets metafield `google_in_stock_count` on inventory changes
- Google Merchant Center rule excludes products where `google_in_stock_count <= 5`
- **Problem:** Flow can set metafields, but calculating variant count in Flow is complex

**Feasibility:** ⚠️ Partially feasible - requires Flow to calculate and set metafield

### Option 3: Shopify App Store Solutions

#### Shopping Feed Apps with Filtering

**Search for:**
- "Google Shopping Feed" apps
- "Feed Management" apps
- Apps that support "inventory filtering"

**Potential Apps to Evaluate:**
1. **Feed for Google Shopping** - Check if supports inventory filtering
2. **Shopping Feed** - May have filtering options
3. **FeedGen** - Check capabilities

**Note:** Most Shopify feed apps are basic and may not support complex inventory-based rules.

### Option 4: Shopify Functions (Advanced)

**What it is:** Shopify's new extensibility platform that allows custom logic at checkout and other touchpoints.

**Limitations:**
- Functions run at checkout, not at feed generation
- Cannot filter products from sales channels
- Not applicable for this use case

**Feasibility:** ❌ Not applicable

### Option 5: Shopify Plus Features

**Shopify Scripts (Deprecated):**
- Old system, being phased out
- Not applicable for feeds

**Shopify Flow Extensions:**
- Custom extensions can be built
- Would require development
- May have API access limitations

**Feasibility:** ⚠️ Possible but requires custom development

### Option 6: Hybrid: Flow + Metafield + Feed App

**Approach:**
1. Shopify Flow calculates in-stock variant count
2. Flow sets metafield: `custom.google_in_stock_count = [number]`
3. Use feed management app (even basic one) that filters on metafield
4. Feed app excludes products where metafield ≤ 5

**Pros:**
- Uses Shopify-native Flow
- Feed app handles the filtering
- No external scripts

**Cons:**
- Requires both Flow setup AND feed app
- Flow calculation of variant count may be complex
- Still need to manage feed app

## Recommended Solution: Feedonomics

**Why Feedonomics:**
1. **Native inventory filtering** - Built-in rules for inventory-based exclusions
2. **Real-time updates** - Feed updates automatically as inventory changes
3. **No external scripts** - Everything managed in their platform
4. **Scalable** - Can add more complex rules later
5. **Professional support** - Enterprise-grade support
6. **Multi-channel** - Can use for other channels too (Facebook, Bing, etc.)

**Implementation Steps:**
1. Sign up for Feedonomics account
2. Connect Shopify store
3. Create feed template for Google Shopping
4. Add rule: "Exclude products where in-stock variants ≤ 5"
5. Configure feed to send to Google Merchant Center
6. Disable native Shopify Google & YouTube channel feed
7. Test and verify

**Cost Consideration:**
- Feedonomics pricing is typically custom/enterprise
- ROI: If you're wasting $X on broken inventory ads, Feedonomics pays for itself if cost < wasted ad spend
- Consider: How much are you currently spending on ads for products with broken inventory?

## Alternative: Start with DataFeedWatch

**If budget is a concern:**
- Start with DataFeedWatch ($99-299/month)
- Test if their inventory filtering rules meet your needs
- Upgrade to Feedonomics later if needed

## Decision Matrix

| Solution                     | Cost | Complexity | Real-time | Maintenance | Recommendation  |
| ---------------------------- | ---- | ---------- | --------- | ----------- | --------------- |
| Feedonomics                  | $$$$ | Medium     | ✅ Yes     | Low         | ⭐⭐⭐⭐⭐ Best      |
| DataFeedWatch                | $$   | Low        | ✅ Yes     | Low         | ⭐⭐⭐⭐ Good       |
| Flow + Metafield + Feed App  | $    | High       | ⚠️ Delayed | Medium      | ⭐⭐⭐ Complex     |
| Google Merchant Center Rules | $    | Medium     | ⚠️ Delayed | Medium      | ⭐⭐ Limited      |
| External Scripts             | $    | Low        | ⚠️ Delayed | High        | ⭐ Not preferred |

## Next Steps

1. **Calculate current wasted ad spend** - How much are you spending on broken inventory?
2. **Request Feedonomics demo** - See if their rule engine can handle your criteria
3. **Compare pricing** - Feedonomics vs DataFeedWatch vs current wasted spend
4. **Pilot test** - Start with one product category or feed
5. **Full migration** - Move entire feed to feed management platform

## Questions to Ask Feed Management Platforms

1. Can you exclude products based on "number of in-stock variants"?
2. How do you calculate variant inventory levels?
3. How quickly do feed updates reflect inventory changes?
4. Can we set custom rules like "exclude if ≤5 variants in stock"?
5. What's the pricing for our product volume?
6. Do you support multi-channel feeds (Google, Facebook, etc.)?
7. Can we test with a small subset of products first?

