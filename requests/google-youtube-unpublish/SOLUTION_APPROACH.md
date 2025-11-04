# Solution Approach: Preventing Broken Inventory in Google Ads

## Problem
Google product ads were being paid for on products with broken inventory (limited size/color availability), leading to wasted ad spend on products customers can't actually purchase.

## Proposed Solution

### Phase 1: Manual Cleanup (Immediate)
1. **Identify products with broken inventory** using `analyze_inventory.py`
2. **Define "broken inventory" criteria:**
   - Products with ≤5 in-stock variants, OR
   - Products with <50% of variants in stock, OR
   - Products where specific size ranges are completely out of stock
3. **Unpublish from Google & YouTube** using `unpublish_products.py` script

### Phase 2: Automation (Ongoing)

**Challenge:** Shopify Flow has limitations:
- ✅ Can trigger on inventory level changes
- ✅ Can modify product tags, metafields, status
- ❌ **Cannot directly unpublish from sales channels** via Publication API

**Workaround Options:**

#### Option A: Flow + Scheduled Script (Recommended)
1. **Shopify Flow** triggers on inventory change
2. Flow checks if product meets "broken inventory" criteria
3. Flow sets a metafield or tag: `google_ads_exclude = true`
4. **Scheduled script** (runs every 15-30 minutes) checks for this tag/metafield
5. Script unpublishes products with the tag from Google & YouTube
6. Script removes tag when inventory is restored

**Pros:**
- Works within Shopify Flow limitations
- Reliable automation
- Can be scheduled via Shopify API or external cron

**Cons:**
- ~15-30 minute delay (not real-time)
- Requires maintaining scheduled script

#### Option B: Flow + Webhook App
1. Flow sets tag/metafield when inventory broken
2. Webhook app (like Zapier, Make.com, or custom) listens for tag changes
3. Webhook triggers API call to unpublish

**Pros:**
- Near real-time (within seconds)
- No scheduled script to maintain

**Cons:**
- Requires third-party app or custom webhook handler
- Additional cost/complexity

#### Option C: Flow Extension (Advanced)
- Use Shopify Flow extensions if available
- Requires custom development
- May have API access limitations

## Recommended Implementation

### Step 1: Define "Broken Inventory" Criteria
Based on your analysis, suggest:
- **Primary:** Products with ≤5 in-stock variants
- **Secondary:** Products with <50% inventory (if product has >10 variants)
- **Exclude:** Products with single variant (handle separately)

### Step 2: Manual Cleanup Script
Update `analyze_products.py` to identify products meeting criteria:
```python
# Criteria: ≤5 in-stock variants
if in_stock_count <= 5:
    flag_for_unpublish()
```

### Step 3: Shopify Flow Setup
1. **Trigger:** Product inventory level changes
2. **Condition:** Calculate in-stock variant count
3. **Action:** Set metafield `custom.google_ads_exclude = true/false`

**Flow Logic:**
```
WHEN: Inventory level changes
THEN:
  - Count variants with inventory > 0
  - IF count ≤ 5:
      Set metafield custom.google_ads_exclude = true
  - ELSE:
      Set metafield custom.google_ads_exclude = false
```

### Step 4: Automated Script
Create a script that:
1. Queries products with `google_ads_exclude = true`
2. Unpublishes from Google & YouTube publication
3. Queries products with `google_ads_exclude = false` that were previously unpublished
4. Re-publishes to Google & YouTube

**Implementation Options:**
- **Shopify Script Tag** (runs on storefront - not ideal)
- **External cron job** (Python script on server/cron)
- **Shopify App** (custom app with scheduled job)
- **Webhook handler** (listens for metafield changes)

## Feasibility Assessment

✅ **Manual cleanup:** Fully feasible - scripts ready  
✅ **Inventory detection:** Fully feasible - Flow can do this  
⚠️ **Automated unpublish:** Partially feasible - requires workaround  

**Recommendation:** Use Option A (Flow + Scheduled Script) for reliability and maintainability.

## Next Steps

1. **Confirm criteria** for "broken inventory"
2. **Run manual cleanup** on current catalog
3. **Set up Shopify Flow** to tag products
4. **Deploy scheduled script** for automated unpublish/republish
5. **Monitor and adjust** criteria based on results

## Alternative: Feed-Level Exclusion

If automation is too complex, consider:
- **Google Merchant Center feed rules** - Exclude products with specific tags/metafields
- **Shopify feed app configuration** - Filter products before sending to Google
- **Manual exclusion lists** - Maintain list of products to exclude

This might be simpler than managing publish/unpublish states.

