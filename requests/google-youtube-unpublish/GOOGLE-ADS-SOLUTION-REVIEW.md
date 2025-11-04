# Google Ads Inventory Filtering - Solution Review

*Analysis Date: November 04, 2025*  
*Prepared for: RUDIS*  
*Prepared by: Arcadia Digital*

---

## Executive Summary

### Problem Statement

Google product ads are currently being paid for on products with broken inventory (limited size/color availability). This results in wasted ad spend when customers click on ads but cannot purchase due to limited inventory options.

### Current Situation

- **Current Setup:** Shopify native Google & YouTube sales channel (direct feed)
- **Issue:** Cannot exclude products based on inventory rules
- **Impact:** Ad spend wasted on products customers can't purchase
- **Scope:** Analysis identified 1,154 active products with partial inventory (some variants in stock, some out)

### Recommended Solution

**Feed Management Platform** - A third-party service that sits between Shopify and Google Merchant Center, automatically filtering products based on inventory rules before ads are served.

**Why This Approach:**
- ✅ Automatically excludes products with ≤5 in-stock variants
- ✅ Real-time updates as inventory changes
- ✅ No external scripts or manual maintenance
- ✅ Professional rule engine built for this use case

---

## Problem Analysis

### Inventory Breakdown (Active Products)

- **Total Active Products:** 4,629
- **Products Fully In Stock:** 1,522 (32.9%)
- **Products Fully Out of Stock:** 1,953 (42.2%)
- **Products with Mixed Inventory:** 1,154 (24.9%) ← **Focus Area**

### Why This Matters

Products with mixed inventory create poor customer experiences:
- Customer clicks ad for a product
- Product appears available
- Customer selects size/color → most options are out of stock
- Customer abandons purchase
- **Result:** Ad spend wasted, no sale

### Current Limitations

Shopify's native Google & YouTube sales channel cannot:
- Filter products based on inventory rules
- Calculate "number of in-stock variants" dynamically
- Exclude products automatically based on inventory metrics
- Update feed in real-time based on inventory changes

---

## Solution Options Evaluated

### Option 1: Feed Management Platform ⭐ **RECOMMENDED**

**What It Is:** Professional platform that manages product feeds between Shopify and Google Merchant Center with advanced filtering capabilities.

**How It Works:**
```
Shopify Store
    ↓
Feed Management Platform
    ↓ [Applies Rules: "Exclude if ≤5 variants in stock"]
    ↓
Google Merchant Center
```

**Key Benefits:**
- Automatic inventory-based filtering
- Real-time feed updates
- No external scripts required
- Multi-channel support (Google, Facebook, Bing, etc.)
- Professional support and maintenance

**Platform Options:**

#### Feedonomics (Enterprise Solution)
- **Pricing:** Custom pricing (~$500-2,000+/month)
- **Best For:** Complex inventory rules, enterprise scale
- **Features:**
  - Powerful rule engine
  - Real-time inventory calculations
  - Multi-channel support
  - Enterprise-grade support

#### DataFeedWatch (Mid-Tier)
- **Pricing:** $99-299/month
- **Best For:** Good features at lower cost
- **Features:**
  - Inventory filtering rules
  - Custom product rules
  - Feed optimization
  - Multi-channel support

#### ShoppingFeeder (Budget Option)
- **Pricing:** Starts at $20/month
- **Best For:** Cost-conscious, basic needs
- **Question:** May not support complex inventory calculations

**Implementation:**
1. Connect Shopify store to feed platform
2. Configure rule: "Exclude products where in-stock variants ≤ 5"
3. Feed platform generates filtered feed
4. Feed platform sends to Google Merchant Center
5. Disable native Shopify feed

**Timeline:** 2-4 weeks for setup and testing

---

### Option 2: Shopify Flow + Metafield + Feed App ⚠️ **COMPLEX**

**How It Works:**
1. Shopify Flow calculates in-stock variant count
2. Flow sets metafield: `custom.in_stock_variant_count`
3. Feed app filters products based on metafield
4. Products with metafield ≤ 5 are excluded

**Pros:**
- Uses Shopify-native Flow
- No external scripts
- Lower cost than feed management platform

**Cons:**
- Complex Flow setup required
- May not be real-time
- Requires managing both Flow and feed app
- Flow has limitations on complex calculations

**Feasibility:** ⚠️ Partially feasible - requires complex Flow configuration

---

### Option 3: Google Merchant Center Rules ⚠️ **LIMITED**

**How It Works:**
1. Shopify Flow sets metafield with inventory count
2. Google Merchant Center rule filters based on metafield

**Limitations:**
- Cannot calculate inventory dynamically
- Requires Flow to calculate and set metafield
- Not designed for complex inventory rules

**Feasibility:** ⚠️ Limited - requires workarounds

---

### Option 4: External Scripts ❌ **NOT RECOMMENDED**

**Why Not:**
- Requires infrastructure and maintenance
- Not preferred per client requirements
- External dependency adds complexity

---

## Decision Matrix

| Solution                     | Cost | Complexity | Real-time | Maintenance | Recommendation  |
| ---------------------------- | ---- | ---------- | --------- | ----------- | --------------- |
| **Feedonomics**              | $$$$ | Medium     | ✅ Yes     | Low         | ⭐⭐⭐⭐⭐ Best      |
| **DataFeedWatch**            | $$   | Low        | ✅ Yes     | Low         | ⭐⭐⭐⭐ Good       |
| Flow + Metafield + Feed App  | $    | High       | ⚠️ Delayed | Medium      | ⭐⭐⭐ Complex     |
| Google Merchant Center Rules | $    | Medium     | ⚠️ Delayed | Medium      | ⭐⭐ Limited      |
| External Scripts             | $    | Low        | ⚠️ Delayed | High        | ⭐ Not preferred |

---

## Cost-Benefit Analysis

### Current Cost of Problem

**To Calculate:**
1. Review Google Ads spend for products with broken inventory
2. Calculate click-through rate for those products
3. Estimate conversion loss from poor inventory experience
4. Factor in time spent on manual management

**Example Calculation:**
- If spending $5,000/month on ads for broken inventory products
- Even 20% waste = $1,000/month in wasted ad spend
- Annual waste: $12,000

### Feed Management Platform Cost

- **Feedonomics:** ~$500-2,000/month (~$6,000-24,000/year)
- **DataFeedWatch:** ~$99-299/month (~$1,200-3,600/year)
- **ShoppingFeeder:** ~$20-50/month (~$240-600/year)

### ROI Calculation

**If wasted ad spend > platform cost:**
- Platform pays for itself
- Additional benefits: Time savings, automation, better customer experience

**Recommendation:**
- Calculate current wasted ad spend
- Compare to platform costs
- Factor in time savings and improved customer experience

---

## Recommended Path Forward

### Phase 1: Platform Evaluation

1. **Calculate Current Wasted Ad Spend**
   - Review Google Ads performance data
   - Identify spend on products with broken inventory
   - Quantify the problem

2. **Request Platform Demos**
   - Feedonomics (if budget allows)
   - DataFeedWatch (recommended starting point)
   - Compare capabilities and pricing

3. **Key Questions to Ask:**
   - Can you exclude products where in-stock variants ≤ 5?
   - How do you calculate variant inventory levels?
   - How quickly do feed updates reflect inventory changes?
   - What's the pricing for our product volume (~4,600 active products)?
   - Can we test with a small subset first?

### Phase 2: Pilot Testing

1. **Select Platform** based on demo and pricing
2. **Setup Test Feed** with one product category
3. **Verify Filtering** works correctly
4. **Compare Results** with current feed
5. **Adjust Rules** as needed

### Phase 3: Full Implementation

1. **Configure Full Feed** for all products
2. **Run in Parallel** with native Shopify feed
3. **Verify Results** - ensure filtering works correctly
4. **Switch Google Merchant Center** to feed platform
5. **Disable Native Feed** from Shopify
6. **Monitor and Optimize**

---

## Implementation Considerations

### Criteria Definition

**Recommended Rule:**
- Exclude products where number of in-stock variants ≤ 5

**Alternative Rules to Consider:**
- Products with <50% inventory (if product has >10 variants)
- Products where specific size ranges are completely out of stock
- Products with no in-stock variants (already handled)

### Testing Approach

1. **Start Small:** Test with one product category
2. **Verify Filtering:** Ensure correct products are excluded
3. **Monitor Performance:** Check ad performance and conversions
4. **Adjust Rules:** Fine-tune criteria based on results

### Migration Strategy

1. **Parallel Operation:** Run both feeds simultaneously
2. **Gradual Rollout:** Start with subset, expand gradually
3. **Monitoring:** Track performance metrics
4. **Cutover:** Switch to feed platform when confident

---

## Next Steps

### Immediate Actions

1. ✅ **Inventory Analysis Complete** - Identified 1,154 products with mixed inventory
2. 📋 **Calculate Wasted Ad Spend** - Review Google Ads data
3. 📞 **Request Platform Demos** - Feedonomics and DataFeedWatch
4. 💰 **Compare Pricing** - Determine ROI

### Success Metrics

- Reduction in wasted ad spend on broken inventory
- Improved conversion rates for products in ads
- Better customer experience (fewer abandoned carts)
- Automated feed management (time savings)

---

## Questions & Support

For questions about this analysis or implementation support, contact:
- **Arcadia Digital** - Technical documentation and implementation support

---

*This document is part of the RUDIS technical documentation repository. For technical details, see the full analysis in `/requests/google-youtube-unpublish/`.*

