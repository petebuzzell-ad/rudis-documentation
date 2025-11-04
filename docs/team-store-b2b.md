# Team Store / B2B System Documentation

**Last Updated:** November 4, 2025  
**For:** Developers, Technical Teams, Business Operations  
**Focus:** Complete technical architecture of Team Store/B2B system

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Architecture & Components](#architecture--components)
3. [Data Flow & Integrations](#data-flow--integrations)
4. [Custom Cart Logic](#custom-cart-logic)
5. [Approval Workflow & Middleware](#approval-workflow--middleware)
6. [Celigo Integration](#celigo-integration)
7. [NetSuite Integration](#netsuite-integration)
8. [Order Processing Flow](#order-processing-flow)
9. [Troubleshooting](#troubleshooting)
10. [Reference](#reference)

---

## System Overview

### What is Team Store / B2B?

Team Store is a **custom B2B e-commerce micro-site system** built into the RUDIS Shopify theme. It enables wrestling teams to:

- **Customize products** with team colors, logos, and personalization
- **Place bulk orders** with tiered pricing based on quantity
- **Submit for approval** before orders are processed
- **Access time-bound stores** with start/end dates
- **Track opportunities** via CRM integration (NetSuite)

### Business Model

- **B2B Sales:** Direct sales to wrestling teams (schools, clubs, organizations)
- **Sales Rep Involvement:** Approval workflow requires sales rep review
- **Opportunity Tracking:** Each team store links to a NetSuite opportunity
- **Bulk Ordering:** Quantity-based pricing tiers for team orders
- **Custom Manufacturing:** Products require art approval before fulfillment

### Why It's Complex

1. **Multi-system Integration:** Shopify → Celigo → NetSuite → AWS Lambda
2. **Custom Approval Workflow:** Art approval status management
3. **Dynamic Pricing:** Tiered pricing based on quantity and customer price level
4. **Time-bound Stores:** Date-based open/close logic
5. **Custom Cart Logic:** Special handling for team store products
6. **Metaobject-driven:** Complex data structure via Shopify metaobjects

---

## Architecture & Components

### Core Theme Files

**Templates:**
- `product.team-store-pdp.json` - Team store product pages
- `collection.team-store-native.json` - Standard team store collection
- `collection.team-store-landing.json` - Team store landing page

**Sections:**
- `main-product-team-store.liquid` - Product page section
- `main-collection-team-store.liquid` - Collection page section
- `team-store-banner.liquid` - Status messages and date display
- `main-collection-product-grid-team-store.liquid` - Product grid
- `main-collection-product-grid-native-team-store.liquid` - Native grid

**Snippets:**
- `team-store-revision-form.liquid` - Approval status form
- `product-card-team-store.liquid` - Product card component
- `product-card-team-store-quick-order.liquid` - Quick order card

**JavaScript:**
- `team-product.js` - Product page logic (pricing, cart properties, validation)
- `team-store-redirect.js` - Opportunity number handling

**CSS:**
- `section-team-store-banner.css` - Banner styling
- `component-product-grid-team-store.css` - Grid styling
- `team-store-bar.css` - Status bar styling
- `template-team-pdp.css` - Product page styling

### Data Structure

**Product Metafields:**
- `custom.is_custom_team_blank` (boolean) - Triggers team store template
- `custom.team_gear_product` (boolean) - Marks product as team gear
- `custom.parent_sku` (text) - Parent SKU format: `{sku_prefix}{base_sku}`
- `custom.team_store_close_date` (date) - Product-level close date override

**Collection Metafields:**
- `custom.start_date` (date) - Store opening date (YYYY-MM-DD)
- `custom.end_date` (date) - Store closing date (YYYY-MM-DD)
- `custom.team_product_data` (JSON) - Team product configuration
- `custom.opportunity_number` (text) - Team opportunity identifier

**Customer/Location Metafields:**
- `customer.metafields.custom.sales_representative` (boolean) - Sales rep access
- `customer.current_location.metafields.custom.opportunity_number` (text) - Team opportunity
- `customer.current_location.metafields.custom.price_level.value[0]` (text) - Price tier

**Metaobject Type: `art_id`**
- **Handle Format:** `{parent_sku}_{opportunity_number}` (e.g., `VV-UNI-PO1176-M-CRB_OPP0025817`)
- **Purpose:** Stores team-specific product configuration, pricing, images, and approval status
- **Key Fields:**
  - `opportunity_id` - Team opportunity number
  - `proof_status` - Approval status ("Approved", "Pending Revision", "Declined", "Pending Approval")
  - `tier_pricing` (JSON) - Quantity-based pricing tiers
  - `price_override` (number) - Overrides all pricing
  - `upcharge_price` (number) - Additional embellishment cost
  - `min_order_qty` (number) - Minimum order quantity
  - `entry_sku` - Entry SKU reference
  - `personalization` - Enables name/number personalization
  - `include_default_images` - Controls default image display

---

## Data Flow & Integrations

### System Architecture

```
Shopify (Theme) 
    ↓ [GraphQL API]
Metaobjects (art_id)
    ↓ [Status Updates]
AWS Lambda (Art Approval Middleware)
    ↓ [Webhook]
Celigo Integration Platform
    ↓ [API Mapping]
NetSuite ERP
    ↓ [Order Processing]
Fulfillment
```

### Integration Points

1. **Shopify → Metaobjects:** GraphQL API fetches product configuration
2. **Shopify → AWS Lambda:** Status updates sent via HTTP POST
3. **AWS Lambda → NetSuite:** Art approval data sent to NetSuite endpoint
4. **Shopify → Celigo:** Order data exported via Celigo app
5. **Celigo → NetSuite:** Orders mapped to opportunities in NetSuite
6. **NetSuite → Shopify:** Product/inventory sync via Celigo

---

## Custom Cart Logic

### Cart Properties System

Team store products add **hidden input fields** to cart items for order processing. These properties are critical for order fulfillment and integration.

**Cart Property Fields:**
```javascript
// From team-product.js setCartItemProperties()
- $opportunity_id - Team opportunity number
- $price_level - Customer price level/tier
- $art_id - Metaobject handle
- $proof_status - Approval status
- $entry_sku - Entry SKU reference
- $image - Product image URL
- $price - Calculated price
- $price_tier - Tier pricing JSON
- $min_order_qty - Minimum order quantity
```

**Implementation:**
```javascript
// assets/team-product.js (lines 165-191)
setCartItemProperties() {
    // Loop through metaobject fields and set cart properties
    for (const [key, value] of Object.entries(this.metaobject)) {
        const inputElement = this.viewModel.cartProperties[`$${key}`];
        if (inputElement) {
            inputElement.value = value;
        }
    }
    
    // Set price level from customer data
    if (this.teamProductData?.priceLevel) {
        this.viewModel.cartProperties.$price_level.value = this.teamProductData.priceLevel;
    }
    
    // Set image URL from collection product data
    const collectionProductsData = this.teamProductData.teamStoreCollection.team_product_data;
    if (isJSON(collectionProductsData)) {
        const imageUrl = JSON.parse(collectionProductsData)[this.metaobject.entry_sku]?.imageLink;
        if (imageUrl) this.viewModel.cartProperties.$image.value = imageUrl;
    }
}
```

### Dynamic Pricing Logic

**Price Calculation Priority:**
1. `price_override` (if set, overrides everything)
2. `tier_pricing` (quantity-based tiers)
3. Base product price (fallback)

**Quantity-Based Pricing:**
```javascript
// assets/team-product.js (lines 83-98)
getPriceWithQuantityDiscount = (quantity) => {
    if (this.priceOverride) return +this.priceOverride;
    
    const { quantities, prices } = this.priceTier;
    const quantitiesArray = Object.values(quantities);
    const pricesArray = Object.values(prices);
    const maxQty = Math.max(...quantitiesArray);
    
    // Find appropriate tier for quantity
    const thresholdIndex = quantity >= maxQty
        ? Math.max(quantitiesArray.findIndex(q => (q - 1) >= quantity) - 1, 0);
    
    const adjustedPrice = this.calculatePrice(pricesArray[thresholdIndex]);
    this.setPriceToCartProperties(adjustedPrice);
    return adjustedPrice;
}
```

**Price Calculation:**
```javascript
calculatePrice = (basePrice) => {
    let price = +basePrice;
    
    // Apply upcharge if present
    if (this.upchargePrice) {
        price += +this.upchargePrice;
    }
    
    // Apply price level multiplier (if customer has price level)
    if (this.teamProductData?.priceLevel) {
        // Price level logic would go here
        // This may adjust price based on customer tier
    }
    
    return price;
}
```

### Cart Validation

**Personalization Validation:**
- Last name required (unless "No Last Name" checkbox checked)
- Number validation (if personalization enabled)
- Prevents add to cart if validation fails

**Minimum Quantity:**
- Enforced via `min_order_qty` from metaobject
- Cart validation checks quantity before adding

---

## Approval Workflow & Middleware

### Approval Status Flow

**Status States:**
1. **"Pending Approval"** - Initial state, awaiting review
2. **"Approved"** - Product ready for purchase
3. **"Pending Revision"** - Revision requested, awaiting changes
4. **"Declined"** - Product declined, not available

**Status Update Process:**

1. **User Action:** Team member or sales rep updates status via revision form
2. **Shopify Update:** Status saved to `art_id` metaobject `proof_status` field
3. **AWS Lambda Call:** HTTP POST to Lambda endpoint with status data
4. **Middleware Processing:** Lambda processes and formats data
5. **NetSuite Notification:** Data sent to NetSuite endpoint
6. **Celigo Sync:** Celigo may sync status back to Shopify

**Status Update API:**
```liquid
// snippets/team-store-revision-form.liquid (lines 163-201)
// HTTP POST to AWS Lambda endpoint
fetch('https://[lambda-endpoint].amazonaws.com/art-approval', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        opportunity_document_identifier: opportunityNumber,
        items: [{
            item_sku: parentSku,
            art_id: metaobjectHandle,
            revision_status: newStatus,
            comments: comments,
            netsuite_notified: true
        }]
    })
})
```

**Payload Structure:**
```json
{
    "OPP0025817": {
        "opportunity_document_identifier": "OPP0025817",
        "items": [
            {
                "item_sku": "VV-UNI-PO1176-M-CRB",
                "art_id": "T_D1_VV-UNI-PO1176-M-CRB_OPP0025817",
                "revision_status": "Pending Revision",
                "comments": "Need color change",
                "netsuite_notified": true
            }
        ]
    }
}
```

### AWS Lambda Middleware

**Purpose:** 
- Process art approval status updates
- Format data for NetSuite
- Send notifications to NetSuite endpoint
- Handle error cases and retries

**Known Issues (from JIRA):**
- "Art Task Middleware Not Working" (RUDS25-384)
- Some payloads not reaching NetSuite endpoint
- Opportunity number required in metaobject for proper routing
- Visibility/logging limitations in Lambda function

**Troubleshooting:**
- Check Lambda logs for payload structure
- Verify opportunity number is set in metaobject
- Confirm NetSuite endpoint is accessible
- Check Celigo connection status

---

## Celigo Integration

### What is Celigo?

**Celigo** is an integration platform (iPaaS) that connects Shopify with NetSuite ERP. It handles:
- **Order Export:** Shopify orders → NetSuite opportunities
- **Product Sync:** NetSuite products → Shopify catalog
- **Inventory Sync:** NetSuite inventory → Shopify stock levels
- **Data Mapping:** Transform Shopify data to NetSuite format

### Celigo Configuration

**App:** "NetSuite Integration by Celigo"  
**Type:** Backend/Admin integration (no theme code)  
**API Version:** Currently using 2024-04 or 2024-07 (deprecating September 25, 2025)

**Active Integration (from JIRA):**
- **Standalone Flow:** Custom flow built by Wendi
- **API Migration:** Updating to 2025-07 API version (RUDS25-444)

### Order Export Flow

**Team Store Orders:**
1. Order placed in Shopify with team store cart properties
2. Celigo detects order via webhook/polling
3. Celigo maps order to NetSuite opportunity (using `opportunity_number`)
4. Order line items exported as individual items (maintains existing mapping)
5. Order data synced to NetSuite opportunity

**Key Requirements (from JIRA):**
- Orders must export as **individual line items** (not bundles)
- Mapping must maintain Celigo workflow without significant changes
- Opportunity number must be correctly mapped
- Bundle products should integrate cleanly with Celigo → NetSuite flow

### Product Sync

**NetSuite → Shopify:**
- Product data synced via "Celigo Shopify Matrix Item Export" search in NetSuite
- Variant inventory levels updated
- Out of stock variants pushed to Shopify (may create null items if not configured properly)

**Known Issues:**
- "Out of Stock Variant, From NetSuite, Push to Shopify and populate null item on site" (RUDS25-336)
- Variants without "Add to Cart" button in NetSuite may cause sync issues

---

## NetSuite Integration

### What is NetSuite?

**NetSuite** is RUDIS's ERP system that handles:
- **Order Management:** Team store orders linked to opportunities
- **Inventory Management:** Product and variant stock levels
- **Product Data:** Product specifications, SKUs, pricing
- **Art Approval:** Approval status tracking for team store products
- **Opportunity Management:** Team store opportunities with product configurations

### NetSuite Data Structure

**Opportunities:**
- Each team store links to a NetSuite opportunity
- Opportunity number stored in Shopify as `opportunity_number`
- Orders exported to NetSuite are linked to opportunity

**Art Approval:**
- Art approval status stored in NetSuite
- Updates flow from Shopify → AWS Lambda → NetSuite
- NetSuite endpoint receives status updates via middleware

**Product Data:**
- Products managed in NetSuite
- Synced to Shopify via Celigo
- Variant data includes custom team store configurations

### Integration Points

**Shopify → NetSuite:**
1. Art approval status updates (via AWS Lambda)
2. Order data (via Celigo)
3. Customer data (via Celigo)

**NetSuite → Shopify:**
1. Product data sync (via Celigo)
2. Inventory levels (via Celigo)
3. Variant availability (via Celigo)

**Known Issues:**
- Order modification delays (RUDS25-385) - changes in Shopify don't update NetSuite quickly
- Reorder feature needed to pull all metafields from NetSuite (~2-3 weeks project)
- Art approval middleware visibility issues (hard to debug endpoint hits)

---

## Order Processing Flow

### Complete Order Journey

**1. Product Selection & Customization:**
- Customer views team store collection
- Selects product with team-specific configuration
- Customizes colors, logos, personalization (if enabled)
- Views approval status

**2. Approval Workflow:**
- Product status: "Pending Approval"
- Sales rep or team admin reviews
- Status updated to "Approved" (or "Pending Revision")
- Approval status saved to metaobject
- AWS Lambda notified
- NetSuite endpoint receives update

**3. Add to Cart:**
- Customer adds product to cart
- Custom cart properties added (opportunity_id, price_level, art_id, etc.)
- Dynamic pricing calculated based on quantity
- Minimum order quantity validated

**4. Checkout:**
- Cart properties passed to checkout
- Order created in Shopify
- Order contains team store metadata

**5. Order Export:**
- Celigo detects new order
- Maps order to NetSuite opportunity (using opportunity_number)
- Exports line items individually
- Links to opportunity in NetSuite

**6. Fulfillment:**
- Order processed in NetSuite
- Art approval verified
- Custom manufacturing/production initiated
- Fulfillment tracked in NetSuite

### Bulk Order Handling

**Team Store Bulk Orders:**
- Multiple products with quantity-based pricing
- Minimum order quantities enforced
- Tiered pricing applied automatically
- All items linked to same opportunity
- Order exported as individual line items (not bundled)

**Cart Properties Preserved:**
- Each line item maintains cart properties
- Opportunity number consistent across items
- Art approval status tracked per item
- Price level and tier pricing preserved

---

## Troubleshooting

### Common Issues

**1. Team Store Not Accessible**
- **Check:** Opportunity number in URL parameter
- **Check:** Customer has `sales_representative` metafield or correct `opportunity_number`
- **Check:** Collection template suffix is set correctly
- **Check:** Start/end dates are valid

**2. Products Not Displaying**
- **Check:** Product has `custom.team_gear_product = true`
- **Check:** Product is in team store collection
- **Check:** Metaobject exists with correct handle format
- **Check:** Collection start/end dates allow viewing

**3. Approval Status Not Updating**
- **Check:** AWS Lambda endpoint is accessible
- **Check:** Opportunity number is set in metaobject
- **Check:** NetSuite endpoint is receiving data
- **Check:** Celigo connection status
- **Review:** Lambda logs for payload structure

**4. Cart Properties Missing**
- **Check:** JavaScript loaded correctly (`team-product.js`)
- **Check:** Metaobject data is available
- **Check:** Cart properties inputs exist in DOM
- **Check:** Console for JavaScript errors

**5. Pricing Not Calculating**
- **Check:** Metaobject has `tier_pricing` data
- **Check:** Quantity is valid (meets minimum)
- **Check:** Price level is set correctly
- **Check:** JavaScript pricing logic is executing

**6. Orders Not Exporting to NetSuite**
- **Check:** Celigo app is active
- **Check:** Order has opportunity_number in cart properties
- **Check:** Celigo flow is configured correctly
- **Check:** NetSuite opportunity exists
- **Check:** Celigo API version is current (2025-07)

**7. Art Approval Middleware Not Working**
- **Check:** Lambda function is deployed and active
- **Check:** Lambda logs for errors
- **Check:** NetSuite endpoint is accessible
- **Check:** Payload structure matches expected format
- **Check:** Opportunity number is in metaobject

---

## Reference

### Related Documentation

- [Technical User Guide - Team Store](technical-user-guide.md#team-store-functionality)
- [Business User Guide - Team Stores](business-user-guide.md#team-stores-b2b)
- [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)
- [Data Guide - Team Store Metaobjects](data-guide.md#team-store-metaobjects)
- [Integrations - Celigo](integrations.md#celigo-integration)

### Key Files Reference

**Theme Files:**
- `sections/main-product-team-store.liquid` - Product page logic
- `sections/main-collection-team-store.liquid` - Collection page logic
- `assets/team-product.js` - JavaScript pricing and cart logic
- `snippets/team-store-revision-form.liquid` - Approval form

**Integration Points:**
- AWS Lambda: Art approval middleware endpoint
- Celigo: Order export and product sync
- NetSuite: ERP system for opportunities and fulfillment

### Data Flow Summary

```
1. User Views Team Store
   ↓
2. GraphQL Fetches Metaobject (art_id)
   ↓
3. Product Displayed with Team Configuration
   ↓
4. User Updates Approval Status
   ↓
5. Status Saved to Metaobject
   ↓
6. AWS Lambda Called with Status Data
   ↓
7. Lambda Sends to NetSuite Endpoint
   ↓
8. User Adds to Cart (with cart properties)
   ↓
9. Order Placed in Shopify
   ↓
10. Celigo Detects Order
    ↓
11. Celigo Maps to NetSuite Opportunity
    ↓
12. Order Exported to NetSuite
    ↓
13. Fulfillment Processed
```

---

**Last Updated:** November 4, 2025  
**Theme Version:** CQL Propel v3.0.0  
**Integration Status:** Active - Celigo API migration in progress (2025-07)

