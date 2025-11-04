# RUDIS Platform Data Guide

**Last Updated:** October 31, 2025  
**For:** Developers, Technical Team, Data Managers  
**Focus:** Complete documentation of metafields, metaobjects, and custom data structures

---

## Table of Contents

1. [Overview](#overview)
2. [Product Metafields](#product-metafields)
3. [Collection Metafields](#collection-metafields)
4. [Page Metafields](#page-metafields)
5. [Customer & Location Metafields](#customer--location-metafields)
6. [Variant Metafields](#variant-metafields)
7. [Metaobjects](#metaobjects)
8. [Third-Party Metafields](#third-party-metafields)
9. [Data Relationships](#data-relationships)
10. [Usage Guidelines](#usage-guidelines)

---

## Overview

The RUDIS platform uses an extensive metafield and metaobject system to extend Shopify's native data model. This guide documents all custom data structures, their purposes, data types, and usage patterns.

### Key Concepts

- **Metafields:** Custom data fields attached to Shopify resources (products, collections, pages, customers, variants)
- **Metaobjects:** Structured, reusable data objects that can be referenced by metafields
- **Namespaces:** Logical groupings of metafields (e.g., `custom`, `reviews`, `cql`)
- **Data Types:** single_line_text_field, multi_line_text_field, boolean, date, number_integer, number_decimal, json, metaobject_reference, file_reference, list types

---

## Product Metafields

### Team Store Metafields

**Namespace:** `custom`

| Metafield                      | Type                   | Required                  | Purpose                             | Usage                                                            |
| ------------------------------ | ---------------------- | ------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| `custom.team_gear_product`     | boolean                | Yes (team stores)         | Marks product as team gear          | Triggers team store functionality                                |
| `custom.is_custom_team_blank`  | boolean                | Yes (customizable blanks) | Marks product as customizable blank | Triggers `product.team-store-pdp.json` template                  |
| `custom.parent_sku`            | single_line_text_field | Yes (team stores)         | Parent SKU for team products        | Format: `{sku_prefix}{base_sku}` (e.g., `RUDIS12345_RUDIS67890`) |
| `custom.team_store_close_date` | date                   | No                        | Product-level store close date      | Overrides collection end date if earlier                         |

**Code Reference:**
```12:16:sections/main-product-team-store.liquid
{%- liquid
    assign isCustomTeamBlank = product.metafields.custom.is_custom_team_blank
    assign teamParentSku = product.metafields.custom.parent_sku
    assign customerIsRep = customer.metafields.custom.sales_representative | default: false
    assign customerOppNum = customer.current_location.metafields.custom.opportunity_number | default: '' | json
```

### Product Display & Content Metafields

| Metafield                  | Type                   | Purpose                                             | Usage                                             |
| -------------------------- | ---------------------- | --------------------------------------------------- | ------------------------------------------------- |
| `custom.product_story`     | multi_line_text_field  | Product narrative/description                       | Used in product storytelling sections             |
| `custom.product_features`  | single_line_text_field | Feature list (comma-separated)                      | Displayed on product pages                        |
| `custom.product_badge`     | single_line_text_field | Badge text (e.g., "New Arrival", "Limited Edition") | Displayed on product cards and PDPs               |
| `custom.promo_message`     | single_line_text_field | Promotional message                                 | Displayed on product pages                        |
| `custom.short_description` | multi_line_text_field  | Short product description                           | Used in collection banners and product cards      |
| `custom.color_name`        | single_line_text_field | Color name for product                              | Used for color filtering and display              |
| `custom.related_styles`    | single_line_text_field | Comma-separated list of related product handles     | Powers "Related Styles" or "More Colors" features |

**Code Reference:**
```18:21:snippets/product-card.liquid
{% assign related_styles =  product_card_product.metafields.custom.related_styles | split: ',' %}
{% assign number_of_handles = related_styles.size %}
{% assign more_colors = false %}
{% assign product_badge =  product_card_product.metafields.custom.product_badge %}
```

### Product Status Metafields

| Metafield                         | Type    | Purpose                                  | Usage                                           |
| --------------------------------- | ------- | ---------------------------------------- | ----------------------------------------------- |
| `custom.coming_soon`              | boolean | Marks product as coming soon             | Hides add to cart, shows coming soon message    |
| `custom.permanently_out_of_stock` | boolean | Marks product as permanently unavailable | Prevents restocking, shows out of stock message |
| `custom.outlet_product`           | boolean | Marks product as outlet/clearance        | May affect pricing or display                   |

### Product Specification Metafields

**Shoe/Footwear Specific:**
| Metafield                                | Type                   | Purpose                         |
| ---------------------------------------- | ---------------------- | ------------------------------- |
| `custom.outsole_type`                    | single_line_text_field | Outsole type description        |
| `custom.heel_to_toe_drop`                | single_line_text_field | Drop measurement (e.g., "8mm")  |
| `custom.cushioning`                      | single_line_text_field | Cushioning type/description     |
| `custom.weight`                          | single_line_text_field | Product weight                  |
| `custom.sizing`                          | single_line_text_field | Sizing information              |
| `custom.fit`                             | single_line_text_field | Fit description                 |
| `custom.upper_materials`                 | single_line_text_field | Upper material description      |
| `custom.shoe_lace_type`                  | single_line_text_field | Lace type                       |
| `custom.collar_height`                   | single_line_text_field | Collar height                   |
| `custom.tongue`                          | single_line_text_field | Tongue description              |
| `custom.lace_closure`                    | single_line_text_field | Closure type                    |
| `custom.tread_pattern`                   | single_line_text_field | Tread pattern description       |
| `custom.shoe_classification_headline`    | single_line_text_field | Shoe classification headline    |
| `custom.shoe_classification_description` | multi_line_text_field  | Shoe classification description |
| `custom.sap_shoe_type`                   | single_line_text_field | SAP shoe type classification    |

**Apparel/Clothing Specific:**
| Metafield                  | Type                   | Purpose                               |
| -------------------------- | ---------------------- | ------------------------------------- |
| `custom.garment_item_type` | single_line_text_field | Item type (e.g., "T-Shirt", "Hoodie") |
| `custom.gender`            | single_line_text_field | Gender designation                    |
| `custom.material`          | single_line_text_field | Material description                  |
| `custom.fabric_details`    | single_line_text_field | Fabric details                        |
| `custom.care_instructions` | single_line_text_field | Care instructions                     |
| `custom.stretch`           | single_line_text_field | Stretch information                   |
| `custom.fit_number`        | single_line_text_field | Fit number/classification             |
| `custom.dimensions`        | single_line_text_field | Product dimensions                    |
| `custom.volume`            | single_line_text_field | Volume/capacity                       |

**Bag/Backpack Specific:**
| Metafield                           | Type                   | Purpose                    |
| ----------------------------------- | ---------------------- | -------------------------- |
| `custom.harnessing_style`           | single_line_text_field | Harnessing style           |
| `custom.number_of_external_pockets` | single_line_text_field | External pocket count      |
| `custom.number_of_internal_pockets` | single_line_text_field | Internal pocket count      |
| `custom.laptop_sleeve`              | single_line_text_field | Laptop sleeve availability |

### Product Branding & Marketing Metafields

| Metafield                   | Type                   | Purpose                                         |
| --------------------------- | ---------------------- | ----------------------------------------------- |
| `custom.worn_by`            | single_line_text_field | Athlete who wears product (e.g., "Spencer Lee") |
| `custom.sub_brand`          | single_line_text_field | Sub-brand designation                           |
| `custom.special_collection` | single_line_text_field | Special collection name                         |
| `custom.generic_color`      | single_line_text_field | Generic color name for filtering                |

### Product Personalization Metafields

| Metafield                               | Type                   | Purpose                          |
| --------------------------------------- | ---------------------- | -------------------------------- |
| `custom.custom_sleeve_available`        | boolean                | Enables sleeve customization     |
| `custom.custom_back_available`          | boolean                | Enables back print customization |
| `custom.name_personalization_available` | boolean                | Enables name personalization     |
| `custom.customization_method`           | single_line_text_field | Customization method description |

### Product Metaobject References

| Metafield                           | Type                 | Metaobject Type       | Purpose                                      |
| ----------------------------------- | -------------------- | --------------------- | -------------------------------------------- |
| `custom.animated_hero`              | metaobject_reference | `animated_hero`       | Animated hero section data                   |
| `custom.image_banner`               | metaobject_reference | `image_banner`        | Image banner data                            |
| `custom.pdp_image_with_text`        | metaobject_reference | `pdp_image_with_text` | Product detail page image with text sections |
| `custom.multicolumn`                | metaobject_reference | `multicolumn`         | Multi-column section data                    |
| `custom.multirow`                   | metaobject_reference | `multirow`            | Multi-row section data                       |
| `custom.product_journey`            | metaobject_reference | `product_journey`     | Product journey/story data                   |
| `custom.breadcrumbs`                | metaobject_reference | `breadcrumbs`         | Custom breadcrumb navigation                 |
| `custom.complete_the_look_products` | metaobject_reference | `complete_the_look`   | Related products for "Complete the Look"     |
| `custom.key_features_metaobject`    | metaobject_reference | `key_features`        | Key product features data                    |
| `custom.shop_the_collection`        | metaobject_reference | `shop_the_collection` | Collection reference for cross-selling       |
| `custom.below_fold_story_section_1` | metaobject_reference | Story section         | Below-fold story section 1                   |
| `custom.below_fold_story_section_2` | metaobject_reference | Story section         | Below-fold story section 2                   |
| `custom.below_fold_story_section_3` | metaobject_reference | Story section         | Below-fold story section 3                   |

### Product Pricing Metafields

| Metafield                      | Type                   | Purpose                | Notes                                 |
| ------------------------------ | ---------------------- | ---------------------- | ------------------------------------- |
| `custom.moq`                   | single_line_text_field | Minimum order quantity | Used for B2B pricing                  |
| `custom.sales_rep_floor_price` | single_line_text_field | Sales rep floor price  | Team store pricing tier               |
| `custom.manager_floor_price`   | single_line_text_field | Manager floor price    | Team store pricing tier               |
| `custom.listed_catalog_price`  | single_line_text_field | Listed catalog price   | Base catalog price                    |
| `custom.base_price_msrp_`      | single_line_text_field | Base MSRP price        | Manufacturer's suggested retail price |

### Product CQL Namespace Metafields

**Namespace:** `cql`

| Metafield                    | Type                   | Purpose                  |
| ---------------------------- | ---------------------- | ------------------------ |
| `cql.product_headline`       | single_line_text_field | CQL product headline     |
| `cql.short_description`      | single_line_text_field | CQL short description    |
| `cql.featured_image_mobile`  | file_reference         | Mobile featured image    |
| `cql.addon_product`          | product_reference      | Add-on product reference |
| `cql.seo_collection_heading` | single_line_text_field | SEO collection heading   |
| `cql.seo_collection_image`   | file_reference         | SEO collection image     |
| `cql.json_swatches`          | json                   | JSON swatch data         |
| `cql.related_images`         | json                   | Related images JSON data |

### Product Shopify Standard Metafields

**Namespace:** `shopify`

These are Shopify's standard product metafields for structured data (e.g., `shopify.color-pattern`, `shopify.size`, `shopify.fabric`, etc.). See Shopify's documentation for complete list.

---

## Collection Metafields

### Team Store Collection Metafields

**Namespace:** `custom`

| Metafield                      | Type                   | Required | Purpose                         | Format                                    |
| ------------------------------ | ---------------------- | -------- | ------------------------------- | ----------------------------------------- |
| `custom.start_date`            | date                   | Yes      | Store opening date              | YYYY-MM-DD                                |
| `custom.end_date`              | date                   | Yes      | Store closing date              | YYYY-MM-DD                                |
| `custom.team_product_data`     | json                   | Yes      | Team product configuration data | JSON object with pricing and product info |
| `custom.opportunity_number`    | single_line_text_field | No       | Team opportunity identifier     | Used for access control                   |
| `custom.store_closing_message` | single_line_text_field | No       | Custom closing message          | Displayed when store closes               |

**Code Reference:**
```5:16:sections/main-collection-team-store.liquid
{% assign team_store_is_open = false %}
{% assign team_store_is_closed = false %}
{% assign today_date = "now" | date: "%s" | minus: 0 %}
{% assign start_date = collection.metafields.custom.start_date | date: "%s" | minus: 0 %}
{% assign close_date = collection.metafields.custom.end_date | date: "%s" | minus: 0 %}
{% if today_date > start_date and today_date < close_date %}
  {% assign team_store_is_open = true %}
{% endif %}

{% if today_date > close_date and collection.metafields.custom.end_date != blank %}
  {% assign team_store_is_closed = true %}
{% endif %}
```

### Collection Display Metafields

| Metafield                        | Type                      | Purpose                                  |
| -------------------------------- | ------------------------- | ---------------------------------------- |
| `custom.short_description`       | multi_line_text_field     | Collection description                   | Used in collection banners |
| `custom.collection_pills`        | list.collection_reference | Related collections for pills navigation |
| `custom.subcategory_type`        | single_line_text_field    | Subcategory type                         |
| `custom.subcategory_title`       | single_line_text_field    | Subcategory title                        |
| `custom.subcategory_caption`     | single_line_text_field    | Subcategory caption                      |
| `custom.subcategory_image`       | file_reference            | Subcategory image                        |
| `custom.subcategory_collections` | list.collection_reference | Collections in subcategory               |

### Collection CQL Namespace Metafields

| Metafield                    | Type                   | Purpose                |
| ---------------------------- | ---------------------- | ---------------------- |
| `cql.seo_collection_heading` | single_line_text_field | SEO collection heading |
| `cql.seo_collection_image`   | file_reference         | SEO collection image   |
| `cql.short_description`      | single_line_text_field | CQL short description  |

---

## Page Metafields

### Page Navigation Metafields

**Namespace:** `custom`

| Metafield                               | Type                      | Purpose                                       |
| --------------------------------------- | ------------------------- | --------------------------------------------- |
| `custom.page_pills_related_collections` | list.collection_reference | Related collections for page pills navigation |
| `custom.breadcrumbs`                    | metaobject_reference      | Custom breadcrumb navigation data             |

### Page Content Metafields

**Namespace:** `custom`

| Metafield                | Type                 | Purpose                    |
| ------------------------ | -------------------- | -------------------------- |
| `custom.animated_hero`   | metaobject_reference | Animated hero section data |
| `custom.image_banner`    | metaobject_reference | Image banner data          |
| `custom.multicolumn`     | metaobject_reference | Multi-column section data  |
| `custom.product_journey` | metaobject_reference | Product journey data       |

---

## Customer & Location Metafields

### Customer Metafields

**Namespace:** `custom`

| Metafield                     | Type                   | Purpose                       | Usage                              |
| ----------------------------- | ---------------------- | ----------------------------- | ---------------------------------- |
| `custom.sales_representative` | boolean                | Grants sales rep access       | Used for team store access control |
| `custom.sales_rep_contact`    | single_line_text_field | Sales rep contact information | Displayed in team stores           |

**Code Reference:**
```51:51:sections/main-product-team-store.liquid
        teamProductData.isTeamAdmin = {{ customerIsRep }} || {{ customerOppNum }} === teamProductData.opportunityNumber;
```

### Customer Location Metafields

**Namespace:** `custom`

| Metafield                                                        | Type                        | Purpose                 | Usage                                                       |
| ---------------------------------------------------------------- | --------------------------- | ----------------------- | ----------------------------------------------------------- |
| `customer.current_location.metafields.custom.opportunity_number` | single_line_text_field      | Team opportunity number | Used for team store access control                          |
| `customer.current_location.metafields.custom.price_level`        | list.single_line_text_field | Price tier/level        | Used for team store pricing (e.g., "Sales Rep Floor Price") |

**Code Reference:**
```16:17:sections/main-product-team-store.liquid
    assign customerOppNum = customer.current_location.metafields.custom.opportunity_number | default: '' | json
    assign priceLevel = customer.current_location.metafields.custom.price_level.value[0] | default: 'Sales Rep Floor Price' | json
```

---

## Variant Metafields

### Variant Custom Metafields

**Namespace:** `custom`

| Metafield                                                                                                 | Type | Purpose |
| --------------------------------------------------------------------------------------------------------- | ---- | ------- |
| (Variant-specific custom metafields are typically minimal - most product data is stored at product level) |

### Variant Third-Party Metafields

**Namespace:** `mm-google-shopping`

| Metafield                           | Type                   | Purpose                        |
| ----------------------------------- | ---------------------- | ------------------------------ |
| `mm-google-shopping.custom_label_0` | single_line_text_field | Google Shopping custom label 0 |
| `mm-google-shopping.custom_label_1` | single_line_text_field | Google Shopping custom label 1 |
| `mm-google-shopping.custom_label_2` | single_line_text_field | Google Shopping custom label 2 |
| `mm-google-shopping.custom_label_3` | single_line_text_field | Google Shopping custom label 3 |
| `mm-google-shopping.custom_label_4` | single_line_text_field | Google Shopping custom label 4 |
| `mm-google-shopping.size_system`    | single_line_text_field | Size system                    |
| `mm-google-shopping.size_type`      | single_line_text_field | Size type                      |
| `mm-google-shopping.mpn`            | single_line_text_field | Manufacturer part number       |
| `mm-google-shopping.gender`         | single_line_text_field | Gender                         |
| `mm-google-shopping.condition`      | single_line_text_field | Product condition              |
| `mm-google-shopping.age_group`      | single_line_text_field | Age group                      |

**Namespace:** `mczr`

| Metafield          | Type | Purpose                |
| ------------------ | ---- | ---------------------- |
| `mczr.variant_ref` | id   | MCZR variant reference |

**Namespace:** `avalara`

| Metafield         | Type                   | Purpose          |
| ----------------- | ---------------------- | ---------------- |
| `avalara.taxcode` | single_line_text_field | Avalara tax code |

**Namespace:** `abconvert`

| Metafield                   | Type                   | Purpose                          |
| --------------------------- | ---------------------- | -------------------------------- |
| `abconvert.price-test-info` | single_line_text_field | ABConvert price test information |

---

## Metaobjects

### Team Store Metaobjects

**Type:** `art_id`

**Handle Format:** `{parent_sku}_{opportunity_number}` (e.g., `RUDIS12345_67890`)

**Purpose:** Stores team store product configuration, pricing, images, and approval status.

**Key Fields:**
| Field                              | Type                 | Purpose                                                                          |
| ---------------------------------- | -------------------- | -------------------------------------------------------------------------------- |
| `opportunity_id`                   | text                 | Team opportunity number                                                          |
| `proof_status`                     | text                 | Approval status ("Approved", "Pending Revision", "Declined", "Pending Approval") |
| `include_default_images`           | boolean/string       | Controls default image display                                                   |
| `personalization`                  | boolean/string       | Enables name/number personalization                                              |
| `tier_pricing`                     | json                 | Pricing tiers with quantity breaks                                               |
| `upcharge_price`                   | number               | Additional embellishment cost                                                    |
| `price_override`                   | number               | Overrides all other pricing                                                      |
| `min_order_qty`                    | number               | Minimum order quantity                                                           |
| `entry_sku`                        | text                 | Entry SKU reference                                                              |
| `team_store_collection`            | collection_reference | Reference to team store collection                                               |
| `design_number`                    | text                 | Design version number                                                            |
| `customization_embellishment_type` | text                 | Embellishment type                                                               |
| `display_name`                     | text                 | Display name                                                                     |
| `back_print`                       | text                 | Back print option                                                                |
| `sleeve_print`                     | text                 | Sleeve print option                                                              |

**Code Reference:**
```53:84:sections/main-product-team-store.liquid
            const metaobjectHandle = `${teamProductData.teamParentSku}_${teamProductData.opportunityNumber}`
            const graphqlQuery = `
              {
                metaobject(
                  handle: {handle: "${metaobjectHandle}", type: "art_id"}
                ) { 
                  fields {
                    value
                    key
                    type
                  }
                  team_store_collection: field(key: "team_store_collection") {
                    reference {
                      ... on Collection {
                        id
                        onlineStoreUrl
                        metafields(
                          identifiers: [
                            {namespace: "custom", key: "start_date"},
                            {namespace: "custom", key: "end_date"}
                            {namespace: "custom", key: "team_product_data"}
                          ]) {
                            value
                            key
                          }
                        }
                      }
                    }
                  }
              }
            `;
```

### Content Metaobjects

**Type:** `animated_hero`

**Purpose:** Stores animated hero section configuration with scroll-based image sequences.

**Note:** The `animated-hero.liquid` section uses section settings, not metaobject fields. If an `animated_hero` metaobject is referenced, it may be used for storing additional configuration data. The section itself reads from `section.settings` rather than metaobject fields.

**Section Settings (when used as section):**
- `filename_prefix` (text) - Prefix for image files (e.g., "hero-2024")
- `number_of_images` (number) - Total number of images in sequence (0-50)
- `global_step_value` (text) - Scroll sensitivity (pixels per frame)
- Story blocks with images and text
- Color and positioning settings

**Code Reference:**
```40:48:sections/animated-hero.liquid
{% if section.settings.filename_prefix != blank %}
  {% for i in (0..50) %}
    {% if use_jpg == true %}
      <link rel="preload" as="image" href="https://www.rudis.com/cdn/shop/files/{{ jpg_file_name }}.jpg">
    {% elsif use_png == true %}
      <link rel="preload" as="image" href="https://www.rudis.com/cdn/shop/files/{{ png_file_name }}.png">
    {% endif %}
  {% endfor %}
{% endif %}
```

---

**Type:** `product_journey`

**Purpose:** Stores product journey/story data for storytelling sections with interactive feature diagrams.

**Key Fields:**
| Field                      | Type                      | Purpose                                             |
| -------------------------- | ------------------------- | --------------------------------------------------- |
| `heading`                  | single_line_text_field    | Main heading text                                   |
| `description`              | multi_line_text_field     | Description text below heading                      |
| `heading_color`            | color                     | Heading text color (default: #ffffff)               |
| `description_color`        | color                     | Description text color (default: #ffffff)           |
| `background_color`         | color                     | Section background color (default: #000000)         |
| `image`                    | file_reference            | Main product image displayed in feature diagram     |
| `headline_animation`       | single_line_text_field    | Animation type for headline (e.g., "fadeInUp")      |
| `headline_animation_time`  | single_line_text_field    | Animation duration (e.g., "0.2s")                   |
| `slide_animation`          | single_line_text_field    | Animation type for slides (e.g., "fadeInLeft")      |
| `image_animation_time`     | single_line_text_field    | Image animation duration                            |
| `slider_text_time`         | single_line_text_field    | Slider text animation duration                      |
| `image_hover`              | single_line_text_field    | Image hover effect (e.g., "easein")                 |
| `selector_dots_color`      | color                     | Color for feature selector dots                     |
| `selector_dots_text_color` | color                     | Text color for selector dots                        |
| `carousel_nav_color`       | color                     | Carousel navigation arrow color                     |
| `features`                 | list.metaobject_reference | List of feature items (see Feature Structure below) |

**Feature Structure (within `features` list):**
Each feature item contains:
- `detail_image` (file_reference) - Feature detail image
- `title` (single_line_text_field) - Feature title
- `description` (multi_line_text_field) - Feature description
- `image_hover` (single_line_text_field) - Hover effect for feature image

**Code Reference:**
```18:26:sections/product-journey.liquid
{% assign metafield_shorthand = template_object.metafields.custom.product_journey.value %}

{% for block in metafield_shorthand.features.value %}
  {% assign metaobjectSize = metaobjectSize | plus: 1 %}
{% endfor %}
```

---

**Type:** `image_banner`

**Purpose:** Stores image banner configuration with desktop and mobile images.

**Key Fields:**
| Field              | Type                   | Purpose                                          |
| ------------------ | ---------------------- | ------------------------------------------------ |
| `desktop_image`    | file_reference         | Desktop banner image                             |
| `mobile_image`     | file_reference         | Mobile banner image                              |
| `heading`          | single_line_text_field | Banner heading text                              |
| `description`      | multi_line_text_field  | Banner description text                          |
| `button_label`     | single_line_text_field | CTA button label                                 |
| `button_link`      | url_reference          | CTA button URL                                   |
| `content_position` | single_line_text_field | Content position (top-left, middle-center, etc.) |
| `overlay_opacity`  | number_decimal         | Overlay opacity (0-100)                          |

**Note:** Specific field structure may vary. See `sections/image-banner.liquid` for implementation details.

---

**Type:** `pdp_image_with_text`

**Purpose:** Stores product detail page image-with-text section data.

**Key Fields:**
| Field            | Type                   | Purpose                     |
| ---------------- | ---------------------- | --------------------------- |
| `image`          | file_reference         | Main image                  |
| `heading`        | single_line_text_field | Section heading             |
| `text`           | multi_line_text_field  | Content text                |
| `image_position` | single_line_text_field | Image position (left/right) |
| `button_label`   | single_line_text_field | Optional button label       |
| `button_link`    | url_reference          | Optional button URL         |

**Note:** Specific field structure may vary. See `sections/image-with-text.liquid` for implementation details.

---

**Type:** `multicolumn`

**Purpose:** Stores multi-column section data with cards, images, and text.

**Key Fields:**
| Field     | Type                      | Purpose                                           |
| --------- | ------------------------- | ------------------------------------------------- |
| `heading` | single_line_text_field    | Section heading                                   |
| `columns` | list.metaobject_reference | List of column items (see Column Structure below) |

**Column Structure (within `columns` list):**
Each column item contains:
- `image` (file_reference) - Column image
- `title` (single_line_text_field) - Column title
- `text` (multi_line_text_field) - Column description text
- `link_label` (single_line_text_field) - Link button label
- `link` (url_reference) - Link URL

**Note:** Specific field structure may vary. See `sections/multicolumn.liquid` for implementation details.

---

**Type:** `multirow`

**Purpose:** Stores multi-row section data.

**Key Fields:**
| Field     | Type                      | Purpose           |
| --------- | ------------------------- | ----------------- |
| `heading` | single_line_text_field    | Section heading   |
| `rows`    | list.metaobject_reference | List of row items |

**Row Structure (within `rows` list):**
Each row item contains:
- `image` (file_reference) - Row image
- `title` (single_line_text_field) - Row title
- `text` (multi_line_text_field) - Row description
- `link` (url_reference) - Optional row link

**Note:** Specific field structure may vary. See `sections/multirow.liquid` for implementation details.

---

**Type:** `complete_the_look`

**Purpose:** Stores "Complete the Look" product recommendations.

**Key Fields:**
| Field         | Type                   | Purpose                      |
| ------------- | ---------------------- | ---------------------------- |
| `heading`     | single_line_text_field | Section heading              |
| `products`    | list.product_reference | List of recommended products |
| `description` | multi_line_text_field  | Optional description text    |

**Note:** Specific field structure may vary. See `sections/complete-the-look-icons.liquid` or `sections/shop-the-look.liquid` for implementation details.

---

**Type:** `key_features`

**Purpose:** Stores key product features data.

**Key Fields:**
| Field      | Type                      | Purpose               |
| ---------- | ------------------------- | --------------------- |
| `heading`  | single_line_text_field    | Section heading       |
| `features` | list.metaobject_reference | List of feature items |

**Feature Structure (within `features` list):**
Each feature item contains:
- `icon` (file_reference) - Feature icon image
- `title` (single_line_text_field) - Feature title
- `description` (multi_line_text_field) - Feature description

**Note:** Specific field structure may vary. See `sections/key-features.liquid` for implementation details.

---

**Type:** `shop_the_collection`

**Purpose:** Stores collection reference for cross-selling.

**Key Fields:**
| Field         | Type                   | Purpose                 |
| ------------- | ---------------------- | ----------------------- |
| `collection`  | collection_reference   | Reference to collection |
| `heading`     | single_line_text_field | Section heading         |
| `description` | multi_line_text_field  | Optional description    |

---

**Type:** `breadcrumbs`

**Purpose:** Stores custom breadcrumb navigation data.

**Key Fields:**
| Field   | Type                      | Purpose                  |
| ------- | ------------------------- | ------------------------ |
| `items` | list.metaobject_reference | List of breadcrumb items |

**Breadcrumb Item Structure (within `items` list):**
Each item contains:
- `label` (single_line_text_field) - Breadcrumb label text
- `url` (url_reference) - Breadcrumb link URL
- `is_active` (boolean) - Whether this is the current page (no link)

**Note:** Specific field structure may vary. See `sections/breadcrumbs.liquid` for implementation details.

---

**Important Notes:**
- Metaobject field structures are defined in Shopify Admin under **Settings > Custom Data > Metaobjects**
- Field types and names may vary - always verify in Shopify Admin
- Code references show how metaobjects are accessed in Liquid templates
- Some metaobjects may be used as section settings rather than metaobject references

---

## Third-Party Metafields

### Reviews Metafields

**Namespace:** `reviews`

| Metafield              | Type           | Purpose                          |
| ---------------------- | -------------- | -------------------------------- |
| `reviews.rating`       | rating         | Product rating value (0-5 stars) |
| `reviews.rating_count` | number_integer | Number of reviews                |

**Code Reference:**
```77:88:snippets/product-card.liquid
      {%- if show_rating and product_card_product.metafields.reviews.rating.value != blank -%}
        {% liquid
          assign rating_decimal = 0
          assign decimal = product_card_product.metafields.reviews.rating.value.rating | modulo: 1
          if decimal >= 0.3 and decimal <= 0.7
            assign rating_decimal = 0.5
          elsif decimal > 0.7
            assign rating_decimal = 1
          endif
        %}
        <div class="rating" role="img" aria-label="{{ 'accessibility.star_reviews_info' | t: rating_value: product_card_product.metafields.reviews.rating.value, rating_max: product_card_product.metafields.reviews.rating.value.scale_max }}">
          <span aria-hidden="true" class="rating-star color-icon-{{ settings.accent_icons }}" style="--rating: {{ product_card_product.metafields.reviews.rating.value.rating | floor }}; --rating-max: {{ product_card_product.metafields.reviews.rating.value.scale_max }}; --rating-decimal: {{ rating_decimal }};"></span>
```

### Yotpo Metafields

**Namespace:** `yotpo`

| Metafield                | Type                   | Purpose                  |
| ------------------------ | ---------------------- | ------------------------ |
| `yotpo.reviews_count`    | single_line_text_field | Yotpo review count       |
| `yotpo.reviews_average`  | single_line_text_field | Yotpo average rating     |
| `yotpo.richsnippetshtml` | single_line_text_field | Yotpo rich snippets HTML |

### Google Shopping Metafields

**Namespace:** `mm-google-shopping`

| Metafield                                    | Type    | Purpose                 |
| -------------------------------------------- | ------- | ----------------------- |
| `mm-google-shopping.google_product_category` | string  | Google product category |
| `mm-google-shopping.custom_product`          | boolean | Custom product flag     |
| `mm-google-shopping.age_group`               | string  | Age group               |

### HulkApps Wishlist Metafields

**Namespace:** `hulkapps_wishlist`

| Metafield                                         | Type                 | Purpose                             |
| ------------------------------------------------- | -------------------- | ----------------------------------- |
| `hulkapps_wishlist.hulkapps_wishlist_buttonstyle` | metaobject_reference | Wishlist button style configuration |

### SEO Metafields

**Namespace:** `seo`

| Metafield    | Type                | Purpose                    |
| ------------ | ------------------- | -------------------------- |
| `seo.hidden` | list.number_integer | Hidden product IDs for SEO |

---

## Data Relationships

### Product Relationships

**Product → Metaobjects:**
- `custom.animated_hero` → `animated_hero` metaobject
- `custom.product_journey` → `product_journey` metaobject
- `custom.image_banner` → `image_banner` metaobject
- `custom.pdp_image_with_text` → `pdp_image_with_text` metaobject
- `custom.multicolumn` → `multicolumn` metaobject
- `custom.multirow` → `multirow` metaobject
- `custom.complete_the_look_products` → `complete_the_look` metaobject
- `custom.key_features_metaobject` → `key_features` metaobject
- `custom.shop_the_collection` → `shop_the_collection` metaobject

**Team Store Product Relationships:**
- Product with `custom.is_custom_team_blank = true` → `art_id` metaobject (handle: `{parent_sku}_{opportunity_number}`)
- `art_id` metaobject → Collection (via `team_store_collection` field)

### Collection Relationships

**Team Store Collection:**
- Collection → `art_id` metaobjects (via opportunity number)
- Collection → Products (via `custom.team_gear_product = true`)
- Collection → Customer Locations (via `custom.opportunity_number`)

**Collection Navigation:**
- `custom.collection_pills` → Related collections
- `custom.subcategory_collections` → Subcategory collections

### Page Relationships

**Page → Collections:**
- `custom.page_pills_related_collections` → Related collections for navigation

**Page → Metaobjects:**
- `custom.animated_hero` → `animated_hero` metaobject
- `custom.image_banner` → `image_banner` metaobject
- `custom.multicolumn` → `multicolumn` metaobject
- `custom.product_journey` → `product_journey` metaobject

### Customer Relationships

**Customer → Team Stores:**
- `customer.metafields.custom.sales_representative` → Access to all team stores
- `customer.current_location.metafields.custom.opportunity_number` → Access to specific team store

---

## Usage Guidelines

### Setting Metafields

**In Shopify Admin:**
1. Navigate to the resource (Product, Collection, Page, Customer)
2. Scroll to **Metafields** section
3. Select or create metafield
4. Enter value according to type
5. Save

**Via API:**
- Use Shopify Admin API or Storefront API
- Metafields follow format: `{namespace}.{key}`
- Use GraphQL for metaobjects

### Best Practices

**Data Type Selection:**
- Use `single_line_text_field` for short text (< 255 chars)
- Use `multi_line_text_field` for longer content
- Use `boolean` for true/false flags
- Use `date` for dates (YYYY-MM-DD format)
- Use `number_integer` or `number_decimal` for numeric values
- Use `json` for complex structured data
- Use `metaobject_reference` for reusable structured content
- Use `list` types for multiple values

**Naming Conventions:**
- Use `snake_case` for metafield keys
- Keep names descriptive and consistent
- Use namespaces to group related metafields

**Team Store Specific:**
- Always set `custom.parent_sku` in format: `{sku_prefix}{base_sku}`
- Ensure `art_id` metaobject handle matches: `{parent_sku}_{opportunity_number}`
- Set `custom.start_date` and `custom.end_date` on collection before store opens
- Configure `team_product_data` JSON with all required product information

**Metaobject References:**
- Create metaobject first, then reference via metafield
- Use consistent handle naming for metaobjects
- Update metaobject to update all references

### Common Issues

**Team Store Not Working:**
- Check `custom.is_custom_team_blank = true` on product
- Verify `custom.parent_sku` format matches metaobject handle
- Ensure `art_id` metaobject exists with correct handle
- Check collection `custom.start_date` and `custom.end_date` are set

**Images Not Displaying:**
- Verify metaobject `include_default_images` field
- Check product images have correct `data-image-index` values (10-19 for model shots, 30-39 for detail shots)
- Ensure custom images are uploaded to `/cdn/shop/files/` with correct naming

**Pricing Not Calculating:**
- Check `tier_pricing` JSON structure in metaobject
- Verify `price_level` on customer location matches tier pricing keys
- Ensure `price_override` is empty if tier pricing should apply

---

## Reference

**Data Export Location:** `data/AD-EVERYTHING-Export_2025-10-22_131917/`

**Metaobjects Export:** `data/AD-EVERYTHING-Export_2025-10-22_131917/Metaobjects.csv`

**Products Export:** `data/AD-EVERYTHING-Export_2025-10-22_131917/Products.csv`

**Theme Code Location:** `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/`

---

**For detailed implementation information, see:**
- [Technical User Guide](technical-user-guide.md) - Team Store functionality and code references
- [Business User Guide](business-user-guide.md) - Content management workflows

