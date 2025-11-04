# Third-Party Integrations

**Last Updated:** October 31, 2025  
**Total Installed Apps:** 51

This document provides comprehensive documentation for all third-party integrations in the RUDIS Shopify Plus platform. Integrations are organized by category and include code references, configuration details, and usage guidelines.

---

## Table of Contents

- [Email & Marketing](#email--marketing)
- [Search & Discovery](#search--discovery)
- [Analytics & Tracking](#analytics--tracking)
- [Reviews & Social Proof](#reviews--social-proof)
- [Customer Support](#customer-support)
- [E-commerce Enhancements](#e-commerce-enhancements)
- [Access Control](#access-control)
- [Tax & Compliance](#tax--compliance)
- [Apps Without Code Integration](#apps-without-code-integration)

---

## Email & Marketing

### Klaviyo: Email Marketing & SMS

**Purpose:** Email marketing automation, SMS campaigns, and back-in-stock notifications.

**Integration Type:** Theme code integration with custom snippet and settings.

**Code References:**
- **Snippet:** `snippets/klaviyo-modal.liquid`
- **Settings:** `config/settings_schema.json` (lines 660-697)
- **Product Integration:** `sections/main-product.liquid` (lines 1460-1473)
- **Global Script:** `layout/theme.liquid` (line 49)
- **JavaScript:** `assets/global.js` (lines 953-957)

**Configuration:**

**Theme Settings:**
- `settings.klaviyo_id` - Klaviyo Public Key (required)
- `settings.show_klaviyo` - Enable/disable out-of-stock messaging (default: true)
- `settings.klaviyo_label` - Button text for "Notify Me" (default: "Notify Me")
- `settings.klaviyo_modal_label` - Modal button text
- `settings.klaviyo_modal_content` - Modal body content
- `settings.klaviyo_success` - Success message text
- `settings.klaviyo_coming_soon_text` - Coming soon message text

**How It Works:**

1. **Back-in-Stock Notifications:**
   - Button appears on product pages when variant is out of stock
   - Only shows if `custom.coming_soon` metafield is null or false
   - Hidden for team store products (`custom.is_custom_team_blank`)
   - Uses Klaviyo OnSite API for email capture

2. **Integration Points:**
   ```liquid
   {% if settings.show_klaviyo and product.metafields.custom.coming_soon.value == null or settings.show_klaviyo and product.metafields.custom.coming_soon.value == false %}
     {% unless isCustomTeamBlank %}
       <button class="klaviyo-bis-trigger product-form__submit button button--full-width button--primary" {% if product.selected_or_first_available_variant.available == true %}style="display:none;"{% endif %}>{{ settings.klaviyo_label }}</button>
       {% render 'klaviyo-modal', ... %}
     {% endunless %}
   {% endif %}
   ```

3. **JavaScript Integration:**
   - Button visibility controlled by `global.js` based on variant availability
   - Toggles between "Add to Cart" and "Notify Me" buttons dynamically

**Usage Notes:**
- Klaviyo script loads globally in theme head
- Modal styling is customizable via snippet
- Integrates with Shopify customer data automatically
- Back-in-stock triggers are handled by Klaviyo platform

---

## Search & Discovery

### SearchSpring

**Purpose:** Advanced site search, filtering, and product recommendations.

**Integration Type:** Deep theme integration with custom sections, templates, and JavaScript bundle.

**Code References:**
- **Main Bundle:** `assets/searchspring.bundle.js`
- **Script Snippet:** `snippets/searchspring-script.liquid`
- **Collection Template:** `templates/collection.searchspring.json`
- **Product Grid Section:** `sections/main-collection-product-grid-ss.liquid`
- **Recommendations Section:** `sections/searchspring-recommendations.liquid`
- **IntelliSuggest:** Loaded in product sections (lines 1919 in main-product.liquid)

**Configuration:**

**SearchSpring Script Integration:**
```liquid
{% render 'searchspring-script' %}
```

**Collection Context:**
- Collection ID, name, and handle passed to SearchSpring
- Customer data passed for personalization
- Template type and search page detection
- Prefetch enabled for collection and search pages

**Product Recommendations:**

**Section:** `sections/searchspring-recommendations.liquid`

**Features:**
- Multiple recommendation profiles (up to 4 blocks)
- Tabbed interface for switching between profiles
- Customizable heading, colors, and padding
- Filters out team store products (`ss_mfield_custom_team_gear_product = false`)
- SKU seeding support for product-specific recommendations

**Configuration Options:**
- `profile_id` - SearchSpring recommendation profile ID
- `seed_profile` - Enable SKU seed data (boolean)
- `max_recommendations` - Maximum products to display (default: 8)
- `tab_title` - Tab label (for multi-profile sections)
- `heading` - Section heading text
- `heading_size` - Typography size
- `content_alignment` - Left, center, or right
- `background_color` - Section background
- `text_color` - Text color
- Padding controls for desktop and mobile

**Code Reference:**
```23:38:sections/searchspring-recommendations.liquid
<script type="searchspring/personalized-recommendations" profile="{{ block.settings.profile_id }}">
  options = {
    limit: {{ block.settings.max_recommendations }},
    filters: [
      {
        type: 'value',
        field: 'ss_mfield_custom_team_gear_product',
        value: false
      }
    ]
  };

  {% if block.settings.seed_profile %}
    seed = "{{ product.variants[0].sku }}";
  {% endif %}
</script>
```

**Collection Pages:**
- Uses `main-collection-product-grid-ss` section for SearchSpring-powered collections
- Replaces native Shopify filtering with SearchSpring filtering
- Loading skeleton displayed while SearchSpring content loads
- Minimum height: 400px for loading state

**IntelliSuggest (Autocomplete):**
- Loaded on all product pages
- Tracks product SKU for autocomplete suggestions
- Integrated with SearchSpring search infrastructure

**Usage Notes:**
- Team store products are automatically filtered out of recommendations
- SearchSpring metafields use `ss_mfield_` prefix for filtering
- Custom styling can override SearchSpring default styles
- Recently viewed carousel auto-hides if empty (after 3.5s delay)

---

## Analytics & Tracking

### Elevar Conversion Tracking

**Purpose:** Enhanced e-commerce tracking for Google Tag Manager (GTM) with automated data layer population.

**Integration Type:** Multiple snippet files for head, body, and checkout tracking.

**Code References:**
- **Head Script:** `snippets/elevar-head.liquid`
- **Body End:** `snippets/elevar-body-end.liquid`
- **Head Listener:** `snippets/elevar-head-listener.liquid`
- **Checkout End:** `snippets/elevar-checkout-end.liquid`

**Configuration:**

**GTM Container ID:** `GTM-TQVF78L9`

**Elevar Configuration:**
```json
{
  "gtm_id": "GTM-TQVF78L9",
  "event_config": {
    "cart_reconcile": true,
    "cart_view": true,
    "checkout_complete": true,
    "checkout_step": true,
    "collection_view": true,
    "defers_collection_loading": false,
    "defers_search_results_loading": false,
    "product_add_to_cart": false,
    "product_add_to_cart_ajax": true,
    "product_remove_from_cart": true,
    "product_select": true,
    "product_view": true,
    "search_results_view": true,
    "user": true,
    "save_order_notes": false
  },
  "gtm_suite_script": "https://shopify-gtm-suite.getelevar.com/shops/82ca28e24ef2aa3fdcc6bdd97d416701ee408877/3.8.0/gtm-suite.js",
  "consent_enabled": false,
  "apex_domain": null
}
```

**Tracked Events:**

1. **Product View:**
   - Default variant data
   - All variant data
   - Product metadata (brand, category, type)
   - Inventory levels
   - Pricing (price, compare at price)

2. **Collection View:**
   - All products in collection
   - Product positions
   - SKU or product ID as item identifier
   - Locksmith integration for access-controlled products

3. **Search Results View:**
   - All search result products
   - Variant-level tracking
   - Search query context

4. **Cart Events:**
   - **Cart View:** Full cart contents with attributes
   - **Add to Cart (AJAX):** Tracks AJAX add-to-cart actions
   - **Remove from Cart:** Tracks item removals
   - **Cart Reconcile:** Reconciles cart attributes with data layer

5. **Checkout Events:**
   - **Checkout Step:** Tracks checkout progress
   - **Checkout Complete:** Full order data including:
     - Order ID/name
     - Revenue, tax, shipping
     - Discounts and coupons
     - Customer data
     - Line items with full details

6. **User Data:**
   - Customer ID, email, name
   - Address information
   - Customer tags
   - Only fires if `event_config.user` is enabled

**Data Layer Structure:**

**Product Data:**
- `id`: SKU (preferred) or variant ID
- `name`: Product title
- `brand`: Vendor
- `category`: Product type
- `variant`: Variant title
- `price`: Final price (converted to dollars)
- `compareAtPrice`: Compare at price
- `productId`: Shopify product ID
- `variantId`: Shopify variant ID
- `image`: Product image URL
- `inventory`: Inventory quantity

**Cart Data:**
- `attributes`: Cart attributes
- `cartTotal`: Total price (dollars)
- `currencyCode`: Currency ISO code
- `items`: Array of cart items with full product data

**Order Data:**
- `actionField`: Order metadata (ID, revenue, tax, shipping, discounts)
- `customer`: Full customer data
- `items`: Line items array
- `landingSite`: Landing site reference

**Integration Points:**

**Locksmith Compatibility:**
- Elevar tracks products through Locksmith access control
- Products hidden by Locksmith are excluded from collection/search tracking
- Uses `locksmith-variables` snippet to check access

**Custom Transform Function:**
- Supports `window.ElevarTransformFn` for custom data transformation
- Must return object or error is logged
- Applied to all data layer pushes

**Usage Notes:**
- Elevar files are auto-generated and should not be edited directly
- Version: 3.8.0 (as of export date)
- Data layer queue system ensures events fire in correct order
- Email capture utility included for lead tracking
- Consent mode supported (currently disabled)

---

## Reviews & Social Proof

### Yotpo Product Reviews

**Purpose:** Product review collection and display, star ratings, and review widgets.

**Integration Type:** Widget-based integration with custom CSS and section components.

**Code References:**
- **CSS:** `assets/yotpo-full-css.css`
- **Global Script:** `layout/theme.liquid` (line 193)
- **Carousel Section:** `sections/Yotpo_Carousel.liquid`
- **Rewards Page Template:** `templates/page.yotpo-rewards.json`
- **Rewards Page Section:** `sections/main-page-yotpo-rewards.liquid`
- **Product CSS Overrides:** `assets/section-main-product.css` (lines 328, 1743-1746)

**Configuration:**

**Global Yotpo Loader:**
```liquid
<script src="https://cdn-widgetsrepository.yotpo.com/v1/loader/nX3YNyQzezbigg8irJ3LIg" async></script>
```

**Carousel Widget:**
- Instance ID: `536440`
- Language-aware loading (uses `localization.language.iso_code`)
- Customizable via Yotpo merchant admin

**Metafields:**
- `reviews.rating` - Product rating (0-5 stars)
- `reviews.rating_count` - Number of reviews
- `yotpo.reviews_count` - Yotpo review count (text)
- `yotpo.reviews_average` - Yotpo average rating (text)
- `yotpo.richsnippetshtml` - Rich snippets HTML

**Product Page Integration:**
- Star ratings widget displayed on product pages
- CSS overrides for font consistency
- Hotfix styles for rating display

**Usage Notes:**
- Yotpo widgets load asynchronously
- Ratings display on product cards and product pages
- Rich snippets included for SEO
- Carousel section available for customizer
- Rewards page template for Yotpo Loyalty program

### Yotpo Loyalty & Rewards

**Purpose:** Customer loyalty program, points, rewards, and referral system.

**Integration Type:** Custom page template with dedicated section.

**Code References:**
- **Template:** `templates/page.yotpo-rewards.json`
- **Section:** `sections/main-page-yotpo-rewards.liquid`

**Usage Notes:**
- Dedicated page template for loyalty program
- Integrated with Yotpo platform
- Customer-facing rewards dashboard

---

## Customer Support

### Contivio (Live Chat)

**Purpose:** Live chat support for customer service.

**Integration Type:** Conditional script loading with mobile visibility control.

**Code References:**
- **Script Snippet:** `snippets/contivio-scripts.liquid`
- **Theme Integration:** `layout/theme.liquid` (lines 61-63)

**Configuration:**

**Theme Setting:**
- `settings.enable_live_chat` - Toggle live chat on/off

**Integration:**
```liquid
{% if settings.enable_live_chat %}
  {% render 'contivio-scripts' %}
{% endif %}
```

**Mobile Visibility:**
- Chat can be hidden on mobile via `settings.hide_live_chat_mobile`
- Uses CSS media query to hide bubble on screens ≤749px

**Code Reference:**
```7:15:snippets/contivio-scripts.liquid
{% if settings.hide_live_chat_mobile %}
  <style>
    @media screen and (max-width: 749px) {
      #chat-button.bubble {
        display: none !important;
        visibility: hidden !important;
      }
    }
  </style>
{% endif %}
```

**Scripts Loaded:**
- Contivio Chat Plugin
- Contivio Configuration Plugin
- Custom stylesheet

**Usage Notes:**
- Chat bubble appears in bottom-right corner
- Fully configurable via Contivio admin panel
- Mobile visibility can be toggled per theme settings

---

## E-commerce Enhancements

### HulkApps Wishlist

**Purpose:** Advanced wishlist functionality for customers.

**Integration Type:** Theme-level initialization with app block support.

**Code References:**
- **Theme Integration:** `layout/theme.liquid` (lines 86-90)
- **Popup Snippet:** `hulkappsWishlistPopup` (rendered in theme)

**Configuration:**

**Initialization:**
```javascript
if(typeof window.hulkappsWishlist === 'undefined') {
  window.hulkappsWishlist = {};
  window.hulkappsWishlist.baseURL = '/apps/advanced-wishlist/api';
  window.hulkappsWishlist.hasAppBlockSupport = '1';
}
```

**Metafields:**
- `hulkapps_wishlist.hulkapps_wishlist_buttonstyle` - Metaobject reference for button style configuration

**Usage Notes:**
- App block support enabled
- Wishlist popup rendered in theme
- API endpoint: `/apps/advanced-wishlist/api`
- Button styles configurable via metaobject

### Realift (RealSize)

**Purpose:** Size recommendation and measurement tracking for apparel.

**Integration Type:** JavaScript integration with Google Analytics tracking.

**Code References:**
- **JavaScript:** `assets/realift-cart.js`

**Configuration:**

**Local Storage:**
- `realift:hasMeasurements` - Boolean flag indicating if customer has completed measurements

**Google Analytics Integration:**
- Sends events to GA4 property: `G-24765BCH66`
- Events:
  - `realsize_add_total` - Cart total when measurements exist
  - `realsize_add_transaction` - Transaction count when measurements exist

**Code Reference:**
```4:21:assets/realift-cart.js
if (localStorage.getItem("realift:hasMeasurements") == "true") {
  if (typeof window.gtag === "function") {
    gtag("event", "realsize_add_total", {
      event_category: "RealSize",
      event_label: "RealSize Add Total",
      value: newCartTotal,
      send_to: "G-24765BCH66",
      use_beacon: true,
    });
    gtag("event", "realsize_add_transaction", {
      event_category: "RealSize",
      event_label: "RealSize Add Transaction",
      value: 1,
      send_to: "G-24765BCH66",
      use_beacon: true,
    });
  }
}
```

**Usage Notes:**
- Tracks when customers with measurements add items to cart
- Integrates with Google Analytics for conversion tracking
- Measurement data stored in Realift platform

### Auction Pro

**Purpose:** Auction functionality for one-of-a-kind products.

**Integration Type:** Custom product template.

**Code References:**
- **Template:** `templates/product.auction-pro-template.json`
- **Page Template:** `templates/page.one-of-one-wrestling-shoe.json` (example auction page)

**Usage Notes:**
- Custom product template for auction items
- "Place a Bid" functionality
- Used for limited edition/one-of-one products
- Example: One-of-One Wrestling Shoe collection

### Simple Bundles & Kits / Bundles

**Purpose:** Product bundling for creating product sets and kits.

**Integration Type:** Custom product template and CSS styling.

**Code References:**
- **Template:** `templates/product.bundles.json`
- **Section:** `sections/main-product-bundles.liquid`
- **CSS:** `assets/section-main-product.css` (lines 1872-1883)

**Usage Notes:**
- Custom bundle product template
- Bundle price messaging
- Component selection interface
- Bundle-specific styling

---

## Access Control

### Locksmith

**Purpose:** Advanced access control for products, collections, and pages.

**Integration Type:** Deep theme integration with automatic snippet injection.

**Code References:**
- **Core Snippet:** `snippets/locksmith.liquid`
- **Variables Snippet:** `snippets/locksmith-variables.liquid`
- **Integration:** Used throughout theme for access control

**How It Works:**

1. **Automatic Integration:**
   - Locksmith snippets automatically injected into theme
   - Access checks performed on product, collection, and page level
   - Remote and manual lock support

2. **Access Control:**
   - Products/collections can be locked to specific customer tags
   - Password protection available
   - Time-based access control
   - Purchase-based access

3. **Theme Compatibility:**
   - Works with Elevar tracking (excludes locked products from analytics)
   - Compatible with collection/product loops
   - Access denied content fully styled

**Code Reference:**
```205:206:snippets/elevar-body-end.liquid
{%- comment %}<locksmith:476b>{% endcomment -%}
{%- capture var %}{% render 'locksmith-variables', scope: 'subject', subject: product, subject_parent: collection, variable: 'transparent' %}{% endcapture %}{% if var == "true" %}{% else %}{% continue %}{% endif -%}
{%- comment %}</locksmith:476b>{% endcomment -%}
```

**Usage Notes:**
- Locksmith-managed files should not be edited directly
- Access control configured in Locksmith app admin
- SEO: Locked content automatically set to `noindex` if configured
- Spinner and loading states included for remote locks

---

## Tax & Compliance

### Avalara AvaTax / Avalara Tax Compliance

**Purpose:** Automated tax calculation and compliance.

**Integration Type:** Metafield-based integration.

**Metafields:**
- `avalara.taxcode` - Single line text field for Avalara tax code

**Usage Notes:**
- Tax codes configured at variant level
- Automatic tax calculation during checkout
- Compliance with tax regulations

---

## Metafield-Based Integrations

### ABConvert

**Purpose:** A/B testing for product pricing.

**Metafields:**
- `abconvert.price-test-info` - Single line text field for price test information

**Usage Notes:**
- Price testing configuration stored in metafields
- Used for pricing experiments

### MCZR (Managed Markets)

**Purpose:** Marketplace integration and variant management.

**Metafields:**
- `mczr.variant_ref` - ID field for MCZR variant reference

**Usage Notes:**
- Links Shopify variants to MCZR marketplace variants
- Used for multi-channel inventory management

### Google Shopping (Managed Markets)

**Purpose:** Google Shopping feed and product data.

**Metafields:**
- `mm-google-shopping.custom_label_0` through `custom_label_4` - Custom labels
- `mm-google-shopping.size_system` - Size system
- `mm-google-shopping.size_type` - Size type
- `mm-google-shopping.mpn` - Manufacturer part number
- `mm-google-shopping.gender` - Gender
- `mm-google-shopping.condition` - Product condition
- `mm-google-shopping.age_group` - Age group
- `mm-google-shopping.google_product_category` - Product category
- `mm-google-shopping.custom_product` - Custom product flag

**Usage Notes:**
- Metafields used for Google Shopping feed generation
- Product data optimized for Google Merchant Center
- See [Data Guide - Third-Party Metafields](data-guide.md#third-party-metafields) for complete reference

---

## Apps Without Code Integration

The following apps are installed but do not have theme code integration. They operate via Shopify app blocks, checkout extensions, or backend APIs:

### Backend/Admin Only
- **Matrixify** - Data import/export
- **Coefficient for Sheets & Excel** - Data management
- **Knowledge Base** - Documentation
- **Filey** - File management
- **NetSuite Integration by Celigo** - ERP integration *(See [Team Store/B2B Documentation](team-store-b2b.md#celigo-integration) for complete integration details)*
- **Fivetran** - Data pipeline
- **integrator.io** - Integration platform

### Checkout/Post-Purchase
- **Checkout Blocks** - Checkout customization
- **Checkout Plus** - Checkout enhancements
- **Loop Returns & Exchanges** - Returns management
- **AfterShip Tracking** - Shipping tracking
- **AfterShip Personalization** - Personalization
- **Notify Me!™** - Back-in-stock (alternative to Klaviyo)

### Marketing & Analytics
- **Kickflip** - Marketing automation
- **Delighted** - Customer surveys
- **GSC Countdown Timer** - Countdown timers
- **TripleWhale** - Analytics
- **Glew Analytics** - Business intelligence
- **Audiences** - Customer segmentation

### Other Services
- **Launchpad** - Scheduled sales
- **Regios Discounts** - Discount management
- **Crazy Egg** - Heat mapping
- **Translate & Adapt** - Translation
- **ShipStation** - Shipping management
- **SheerID Community Verification** - Identity verification
- **Zendesk** - Customer support
- **Loyal** - Loyalty program
- **GRIN Influencer Marketing** - Influencer management
- **Gift Card Factory** - Gift cards
- **In-Cart Rating & Fulfillment** - Rating system
- **Theme Access** - Theme management
- **Shopify GraphiQL App** - API testing
- **Browser Icon & Title Animation** - Browser enhancements
- **Flow** - Shopify Flow automation
- **Fraud Control** - Fraud prevention
- **ShipperHQ: All-In-One Solution** - Shipping calculator

**Note:** These apps may have metafields or app blocks that are not visible in theme code. Check Shopify admin for app-specific configurations.

---

## Integration Best Practices

### Adding New Integrations

1. **Code Organization:**
   - Create snippets for reusable integration code
   - Use theme settings for configuration
   - Keep integration logic separate from theme logic

2. **Performance:**
   - Load scripts asynchronously when possible
   - Use `defer` for non-critical scripts
   - Minimize third-party script bloat

3. **Error Handling:**
   - Always check for script availability before calling functions
   - Log errors to console for debugging
   - Provide fallbacks when integrations fail

4. **Testing:**
   - Test integrations in development theme first
   - Verify all tracked events fire correctly
   - Test with ad blockers and privacy tools
   - Verify mobile compatibility

### Troubleshooting

**Common Issues:**

1. **Scripts Not Loading:**
   - Check network tab for failed requests
   - Verify script URLs are correct
   - Check for ad blocker interference

2. **Events Not Firing:**
   - Verify integration is initialized
   - Check browser console for errors
   - Verify data layer structure matches requirements

3. **Styling Conflicts:**
   - Use CSS specificity to override third-party styles
   - Scope custom styles to integration containers
   - Test across different screen sizes

---

## References

- [Technical User Guide](technical-user-guide.md) - Theme architecture and customization
- [Team Store/B2B Documentation](team-store-b2b.md) - Complete Team Store system including Celigo and NetSuite integrations
- [Data Guide](data-guide.md) - Complete metafield reference
- [Business User Guide](business-user-guide.md) - Content management workflows

---

**Last Updated:** October 31, 2025  
**Theme Version:** CQL Propel v3.0.0  
**Export Date:** October 29, 2025

