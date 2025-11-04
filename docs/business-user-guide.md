# RUDIS Platform Documentation - Business User Guide

**Last Updated:** October 31, 2025  
**For:** Content Managers, Marketing Team, Business Users  
**Focus:** RUDIS-specific features and configurations

---

## Table of Contents

1. [Understanding RUDIS-Specific Features](#understanding-rudis-specific-features)
2. [Team Stores (B2B)](#team-stores-b2b)
3. [Product Template Management](#product-template-management)
4. [Collection Configuration](#collection-configuration)
5. [Page Template Assignments](#page-template-assignments)
6. [Custom Sections & RUDIS-Specific Components](#custom-sections--rudis-specific-components)
7. [Metafields & Custom Data](#metafields--custom-data)
8. [Media Asset Specifications](#media-asset-specifications)
9. [Making Site Updates](#making-site-updates)
10. [Troubleshooting](#troubleshooting)
11. [Data Reference](#data-reference)

---

## Understanding RUDIS-Specific Features

The RUDIS platform includes several custom features that are not part of standard Shopify functionality. Understanding these is essential for managing content effectively.

### Key Custom Features

1. **Team Stores** - B2B functionality for wrestling teams (pseudo B2B micro-sites)
2. **Product Template Variants** - Specialized templates for different product types
3. **Athlete-Specific Features** - Templates and features for athlete-branded products
4. **Auction Functionality** - Special product templates for auctions
5. **Bundle Products** - Custom bundle product handling
6. **SearchSpring Integration** - Advanced search and filtering on collection pages

---

## Team Stores (B2B)

### Overview

Team Stores are a unique micro-site concept built into the theme that acts as a pseudo B2B site for wrestling teams. Each team gets their own store where they can customize products with team colors, logos, and personalization.

### How Team Stores Work

**Team Store Structure:**
- Each team store is a **Collection** with the template suffix `team-store-native` or `team-store-landing`
- Team stores have **start dates** and **end dates** (managed via [collection metafields](data-guide.md#team-store-collection-metafields))
- Products in team stores are marked with [`custom.team_gear_product = true`](data-guide.md#team-store-metafields) metafield
- Products that are customizable blanks are marked with [`custom.is_custom_team_blank = true`](data-guide.md#team-store-metafields) metafield
- Team stores can be **open** or **closed** based on dates
- Team stores require **approval workflow** before ordering

### Setting Up a Team Store

**1. Create the Team Store Collection**

1. Go to **Products** > **Collections**
2. Create a new collection for the team
3. Set the **Template suffix** to `team-store-native`
4. Add collection metafields (see [Data Guide - Team Store Collection Metafields](data-guide.md#team-store-collection-metafields)):
   - `custom.start_date` - When the store opens
   - `custom.end_date` - When the store closes
   - `custom.team_product_data` - JSON data for team products

**2. Configure Team Store Products**

Products in team stores must have specific metafields (see [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)):

- `custom.team_gear_product` = `true` (boolean) - Marks product as team gear
- `custom.is_custom_team_blank` = `true` (boolean) - Marks product as a customizable blank
- `custom.parent_sku` = Parent SKU for the team product (text)
- `custom.team_store_close_date` = Date when team store closes (date)

**3. Team Store Product Pages**

- Team store products use template: `product.team-store-pdp.json` or automatically when `custom.is_custom_team_blank = true`
- Products display custom image galleries managed via [metaobjects](data-guide.md#team-store-metaobjects) (type: `art_id`)
- Include personalization options (name, number)
- Show approval status messages
- Include team-specific pricing from [metaobjects](data-guide.md#team-store-metaobjects)

**4. Team Store Collection Pages**

- Template: `collection.team-store-native.json` or `collection.team-store-landing.json`
- Display status messages via "Status Key Messages" block:
  - **Approved:** "YOUR GEAR LOOKS GREAT: Your sale's rep will contact you soon to order."
  - **Action Required:** "ACTION REQUIRED: Update the status on ALL products to proceed with your order."
  - **In Revision:** "REVISIONS IN PROGRESS: You will be notified when action is required."

### Team Store Workflow

1. **Setup Phase:**
   - Create collection with team store template
   - Set start/end dates
   - Add products with team gear metafields
   - Configure team-specific pricing

2. **Active Phase:**
   - Team members can view products
   - Customize products (colors, logos, personalization)
   - Submit for approval

3. **Approval Phase:**
   - Products show approval status
   - Team admin can approve/reject items
   - Status messages guide users

4. **Closed Phase:**
   - Store closes on end date
   - Products show "This team store has officially closed" message
   - No new orders accepted

### Team Store Access

- Team stores are accessible via URL with `opportunity_number` parameter
- The opportunity number is stored in `localStorage` and collection metafields
- Access is controlled by [customer metafields](data-guide.md#customer-metafields):
  - `custom.sales_representative` (boolean) - Sales rep access
  - `custom.opportunity_number` (text) - Team opportunity number (stored in [customer location metafields](data-guide.md#customer-location-metafields))
- Team stores are hidden on Canada site (US only) - "Custom Team Gear" menu link is hidden via `function.is_menu_item_hidden.liquid`

### Managing Team Store Content

**Adding Products to Team Store:**
1. Products must be assigned to the team store collection
2. Set [`custom.team_gear_product = true`](data-guide.md#team-store-metafields) metafield
3. For customizable blanks, set [`custom.is_custom_team_blank = true`](data-guide.md#team-store-metafields)
4. Set [`custom.parent_sku`](data-guide.md#team-store-metafields) to link to parent product
5. Configure team-specific pricing in [metaobjects](data-guide.md#team-store-metaobjects) (type: `art_id`)

**Updating Team Store Dates:**
- Edit [collection metafields](data-guide.md#team-store-collection-metafields): `custom.start_date` and `custom.end_date`
- Dates control when store is open/closed
- Store automatically closes after end date

**Team Store Status Messages:**
- Managed in collection template customizer via "Status Key Messages" block (type: `status_key_messages`)
- Edit messages for: Approved, Action Required, In Revision
- Messages display based on product approval status in team store workflow

---

## Product Template Management

### Understanding Product Templates

RUDIS uses specialized product templates for different product types. The template assignment determines how products are displayed and what features are available.

### Standard Product Templates

**Default Template (`product.json`)**
- Used for: Most standard products
- No special requirements
- Standard product display

### Specialized Product Templates

**Shoe Products (`product.shoe-product.json`)**
- **Usage:** All wrestling shoes and footwear
- **Assignment:** Manual - Set template suffix to `shoe-product` in Shopify Admin
- **Features:** Shoe-specific sizing, features display, specialized media gallery
- **Requirements:** 
  - Set template suffix to `shoe-product` in product settings
  - Product type should indicate footwear (for organization, not template assignment)

**Team Store Products (`product.team-store-pdp.json`)**
- **Usage:** Team store products (customizable blanks)
- **Assignment:** Manual - Set template suffix to `team-store-pdp` in Shopify Admin
- **Layout Detection:** Theme code checks [`custom.is_custom_team_blank = true`](data-guide.md#team-store-metafields) metafield for conditional layout rendering (e.g., noindex robots tag), but template suffix must be set manually
- **Features:** Custom image galleries (managed via [metaobjects](data-guide.md#team-store-metaobjects)), personalization options, approval workflow, team-specific pricing
- **Requirements:** 
  - Set template suffix to `team-store-pdp` in product settings
  - Must have [`custom.team_gear_product = true`](data-guide.md#team-store-metafields) and [`custom.is_custom_team_blank = true`](data-guide.md#team-store-metafields) metafields set

**Bundle Products (`product.bundles.json`)**
- **Usage:** Product bundles and sets
- **Assignment:** Manual - Set template suffix to `bundles` in Shopify Admin
- **Features:** Bundle component selection, bundle pricing
- **Requirements:** 
  - Set template suffix to `bundles` in product settings
  - Products must be configured as bundles in Shopify

**Auction Products (`product.auction-pro-template.json`)**
- **Usage:** Auction and special event products
- **Features:** Countdown timers, bid functionality
- **Requirements:** Auction-specific metafields configured

**Athlete Brand Templates:**
- `product.kolat.json` - Kolat brand products
- `product.rocky.json` - Rocky brand products
- `product.hildebrandt.json` - Hildebrandt products
- `product.jb-ultra-ps.json` - Jordan Burroughs Ultra
- `product.jb-ultralite.json` - Jordan Burroughs Ultralite

### Template Assignment

**Important:** All template suffixes must be set **manually** in Shopify Admin. Shopify does not automatically assign templates based on product type, metafields, or configuration.

**Setting Template Suffixes:**
1. Navigate to product/collection/page settings
2. Scroll to **Search engine listing** section
3. Find **Template suffix** dropdown
4. Select desired template suffix
5. Save

**Template Suffix vs Layout Conditionals:**
- **Template Suffix:** Determines which template file is used (set in Shopify Admin)
- **Layout Conditionals:** Theme code can conditionally render different layouts based on metafields (e.g., team store products get noindex robots tag), but this does not change the template file

**See Also:** [Technical User Guide - Template Assignment System](technical-user-guide.md#template-assignment-system) for complete documentation

### Product Template Requirements

**For Shoe Products:**
- Product type should indicate footwear
- May require shoe-specific metafields

**For Team Store Products:**  
Required metafields (see [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields) for complete documentation):
- `custom.team_gear_product = true` (boolean)
- `custom.is_custom_team_blank = true` (boolean) - For customizable blanks
- `custom.parent_sku` (text) - Parent product SKU
- `custom.team_store_close_date` (date) - Optional, product-level close date

**For Bundle Products:**
- Products configured as bundles in Shopify
- Bundle components linked

**For Auction Products:**
- Auction-specific metafields configured
- Auction dates set

---

## Collection Configuration

### Collection Types

**Standard Collections**
- Use default `collection.json` template
- Standard product grid display
- Native Shopify filtering and sorting

**SearchSpring Collections**
- **Template Suffix:** `searchspring` (creates `collection.searchspring.json` template)
- **Usage:** Collections using SearchSpring search/filter integration
- **Features:** Enhanced search, advanced filtering, SearchSpring recommendations
- **Configuration:**
  1. Set collection template suffix to `searchspring` in Shopify Admin
  2. Ensure SearchSpring app is installed and configured
  3. Collection automatically uses SearchSpring-powered product grid
- **See Also:** [Integrations Guide - SearchSpring](integrations.md#searchspring) for detailed setup instructions

**Team Store Collections**
- **Template Suffixes:**
  - `team-store-native` → Creates `collection.team-store-native.json` template
  - `team-store-landing` → Creates `collection.team-store-landing.json` template
- **Usage:** `team-store-native` for standard team store collections, `team-store-landing` for landing pages
- **Features:** Custom team store functionality, approval workflow with status messages
- **Configuration:** Date-based open/close via [`custom.start_date` and `custom.end_date`](data-guide.md#team-store-collection-metafields) metafields
- **Setting:** Set template suffix in collection settings → Search engine listing → Template suffix dropdown

### Collection Metafields

**Team Store Collections Require:**  
Required metafields (see [Data Guide - Team Store Collection Metafields](data-guide.md#team-store-collection-metafields) for complete documentation):
- `custom.start_date` (date) - Store opening date
- `custom.end_date` (date) - Store closing date
- `custom.team_product_data` (JSON) - Team product configuration data
- `custom.opportunity_number` (text) - Optional, team opportunity identifier

**Collection Configuration:**
- Metafields are set in collection settings
- Dates control store availability
- Team product data contains pricing and product information

---

## Page Template Assignments

### Standard Page Templates

**Default Page (`page.json`)**
- Used for: Most content pages
- Fully customizable with all sections
- Standard page functionality

### Specialized Page Templates

**Yotpo Rewards Page (`page.yotpo-rewards.json`)**
- **Usage:** Yotpo loyalty rewards program page
- **Features:** Yotpo rewards integration

**Technique Library Pages:**
- `page.technique-library.json` - General technique library
- `page.technique-library-kennedy.json` - Kennedy Blades techniques
- `page.technique-library-kolat.json` - Cary Kolat techniques
- **Usage:** Wrestling technique content pages

**Athlete Pages:**
- `page.spencer.json` - Spencer Lee athlete page
- `page.kolat.json` - Kolat athlete page
- **Usage:** Individual athlete profile pages

**Signup Forms:**
- `page.signup-form.json`
- `page.signup-form-02.json`
- `page.signup-form-3.json`
- **Usage:** Email signup pages

**Style Guide (`page.styleguide.liquid`)**
- **Usage:** Design system reference page

---

## Custom Sections & RUDIS-Specific Components

### RUDIS Custom Sections

**Animated Hero (`animated-hero.liquid`)**
- **Purpose:** Hero sections with animated content
- **Usage:** Homepage, landing pages
- **Special Features:** Filename prefix system for dynamic images
- **Image Requirements:** Images follow naming convention with prefix

**Team Store Banner (`team-store-banner.liquid`)**
- **Purpose:** Banner for team store pages
- **Usage:** Team store collections
- **Special Features:** Team-specific messaging, date display, status messages, disclaimer

**PDP Storytelling (`pdp-storytelling.liquid`)**
- **Purpose:** Product storytelling sections
- **Usage:** Product detail pages
- **Special Features:** Custom product narrative display

**Product Journey (`product-journey.liquid`)**
- **Purpose:** Product journey visualization
- **Usage:** Product detail pages
- **Special Features:** Step-by-step product story

### Understanding Section Usage

**Standard Shopify Sections:**
- Image Banner, Rich Text, Multi-Column, Video, etc.
- These work as expected with standard Shopify functionality

**RUDIS Custom Sections:**
- Animated Hero, Team Store Banner, PDP Storytelling, etc.
- These require specific configurations or metafields
- See Technical User Guide for complete settings

---

## Metafields & Custom Data

**Note:** For complete metafield documentation including field types, usage, and code references, see the [Data Guide](data-guide.md).

**Commonly Used Metafields:**

**Team Store Products:**
- `custom.team_gear_product` (boolean) - Marks product as team gear
- `custom.is_custom_team_blank` (boolean) - Marks product as customizable blank
- `custom.parent_sku` (text) - Parent SKU for team products
- See [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields) for complete reference

**Team Store Collections:**
- `custom.start_date` (date) - Store opening date
- `custom.end_date` (date) - Store closing date
- `custom.team_product_data` (JSON) - Team product configuration data
- See [Data Guide - Team Store Collection Metafields](data-guide.md#team-store-collection-metafields) for complete reference

**Product Content:**
- `custom.product_story` - Product narrative
- `custom.product_features` - Feature list
- `custom.product_badge` - Badge text
- `custom.worn_by` - Athlete name
- See [Data Guide - Product Metafields](data-guide.md#product-metafields) for complete reference

### Managing Metafields

**Where to Set Metafields:**
1. **Products:** In product settings, scroll to **Metafields** section
2. **Collections:** In collection settings, scroll to **Metafields** section
3. **Pages:** In page settings, scroll to **Metafields** section

**Important Metafields for Content Updates:**
- Product metafields control template behavior
- Collection metafields control team store functionality
- Page metafields control custom page features

---

## Media Asset Specifications

### Product Images

**Standard Product Images:**
- **Recommended Size:** Minimum 2048px width (up to 4096px supported)
- **Aspect Ratio:** Preserved (square, portrait, or landscape all supported)
- **Format:** JPG or PNG
- **File Size:** Optimize to <500KB when possible
- **Responsive Breakpoints:** Images are automatically served at 550px, 1100px, 1445px, 1680px, 2048px, 2200px, 2890px, 4096px widths

**Product Card Images:**
- **Display Size:** Responsive (165px, 360px, 533px, 720px, 940px, 1066px widths)
- **Default Display:** 533px width
- **Aspect Ratio:** Preserved from original image
- **Secondary Image:** Same specifications (for hover effects)

**Product Swatches/Color Variants:**
- **Small Swatches:** 37px × 37px (square)
- **Large Swatches:** 150px × 150px (square)
- **Format:** JPG or PNG
- **Usage:** Color variant selection displays

### Team Store Product Images

**Image Naming Convention:**
Team store products use a specific image naming and indexing system:

1. **Custom Images (First Priority):**
   - Images with no `data-image-index` attribute
   - Display first in gallery
   - Managed via metaobjects

2. **Model Shots (Second Priority):**
   - Images with `data-image-index` values **0010-0019** (10-19)
   - Display after custom images
   - Used for model/lifestyle shots

3. **Detail Shots (Third Priority):**
   - Images with `data-image-index` values **0030-0039** (30-39)
   - Display after model shots
   - Used for product detail shots

**Important:** Images with index numbers outside the 0010-0019 and 0030-0039 ranges are automatically hidden on team store product pages.

**Image Gallery Control:**
- Managed via metaobject (`art_id` type)
- `include_default_images` field controls whether default images are shown
- If `include_default_images = false`: Only custom images display
- If `include_default_images = true`: Custom images + model shots (0010-0019) + detail shots (0030-0039)

**Image Requirements:**
- Same specifications as standard product images
- Images must be uploaded to Shopify Files
- Image index is set via `data-image-index` attribute in product media

### Animated Hero Images

**Filename Prefix System:**
The Animated Hero section uses a dynamic filename prefix system for scroll-based animations.

**File Naming Convention:**
- **Format:** `{filename_prefix}__{number}.{extension}`
- **Example:** `hero-2024__0.jpg`, `hero-2024__1.jpg`, `hero-2024__2.jpg`, etc.
- **Extension:** JPG or PNG (section auto-detects which format exists)
- **Number Range:** 0-50 (up to 51 images per hero section)

**File Location:**
- Images must be uploaded to: `/cdn/shop/files/`
- Full path format: `https://www.rudis.com/cdn/shop/files/{filename_prefix}__{number}.jpg`

**Image Specifications:**
- **Recommended Size:** 1920px × 1080px (16:9 aspect ratio) or larger
- **Format:** JPG or PNG (section determines which to use)
- **File Size:** Optimize each frame to <500KB when possible
- **Number of Images:** Up to 51 images (0-50) per hero section

**Story Block Images (Within Animated Hero):**
- Embedded images in story blocks
- Display at natural aspect ratio
- No specific size requirements, but recommended to match hero dimensions

**Setup:**
1. Upload images with consistent naming: `{prefix}__0.jpg`, `{prefix}__1.jpg`, etc.
2. Set `filename_prefix` in section settings (e.g., `hero-2024`)
3. Set `number_of_images` to match your image count
4. Set `global_step_value` for scroll animation sensitivity

### Image Banner Section

**Desktop Images:**
- **Standard Desktop:** Up to 2800px width
- **Desktop Large (Wide Screens):** Up to 2800px width (for screens wider than 1650px)
- **Aspect Ratio:** Flexible (16:9 recommended for banners)
- **Format:** JPG or PNG
- **File Size:** <500KB recommended

**Mobile Images:**
- **Mobile:** Up to 1100px width
- **Aspect Ratio:** Flexible (9:16 portrait recommended for mobile banners)
- **Format:** JPG or PNG
- **File Size:** <200KB recommended

**Best Practices:**
- Always provide separate mobile images for optimal mobile experience
- Use desktop large image for ultra-wide screens (2560px+)
- Maintain aspect ratio consistency across desktop and mobile versions

### Collection Banner Images

**Collection Banner Section:**
- **Desktop Max Height:** Configurable (default: 650px)
- **Recommended Width:** 1920px
- **Aspect Ratio:** Flexible, but height is controlled by `desktop_max_height` setting
- **Format:** JPG or PNG

### Footer Images

**Footer Logo/Social Images:**
- **Recommended Size:** 400px width
- **Format:** PNG with transparency (for logos)
- **Aspect Ratio:** Preserved

### Video Cover Images

**Video Section:**
- **Desktop Cover:** 1920px × 1080px (16:9 ratio)
- **Mobile Cover:** 750px × 422px (16:9 ratio)
- **Format:** JPG or PNG
- **File Size:** <300KB recommended

### General Image Guidelines

**File Formats:**
- **JPG:** Best for photographs and complex images
- **PNG:** Best for graphics with transparency or simple graphics
- **WebP:** Supported but not required (theme will use JPG/PNG)

**Optimization:**
- Always optimize images before upload
- Use image compression tools
- Target file sizes:
  - Desktop images: <500KB
  - Mobile images: <200KB
  - Product images: <500KB (can be larger for high-quality product photos)

**Aspect Ratios:**
- Product images: Any aspect ratio (preserved)
- Banner images: 16:9 recommended for desktop, 9:16 for mobile
- Square images: 1:1 (for product cards, swatches)
- Portrait images: 4:5 or 3:4 (for product displays)

**Responsive Images:**
- Theme automatically generates multiple sizes for responsive display
- Images are served at appropriate sizes based on device and viewport
- No manual resizing needed - upload at highest quality, theme handles optimization

### Image Upload Locations

**Shopify Files (for Animated Hero):**
- Upload to: **Content** > **Files** in Shopify admin
- Access via: `/cdn/shop/files/` path
- Used for: Animated Hero images with filename prefix system

**Product Images:**
- Upload via: **Products** > **Product** > **Media** in Shopify admin
- Stored in: Shopify CDN
- Used for: Product galleries, product cards, collections

**Theme Assets:**
- Upload to: **Online Store** > **Themes** > **Customize** > **Theme files** > **Assets**
- Used for: Theme-specific images, icons, logos

---

## Making Site Updates

### Adding a New Product

**Standard Product:**
1. Create product in Shopify admin
2. Set product type (determines template)
3. Add product images
4. Set variants and pricing
5. Product will use appropriate template automatically

**Team Store Product:**
1. Create product in Shopify admin
2. Set metafields (see [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)):
   - `custom.team_gear_product = true` (boolean)
   - `custom.is_custom_team_blank = true` (boolean, if customizable blank)
   - `custom.parent_sku = [parent SKU]` (text)
   - `custom.team_store_close_date` (date, optional)
3. Add to team store collection (collection with template suffix `team-store-native` or `team-store-landing`)
4. Configure team-specific pricing in [metaobjects](data-guide.md#team-store-metaobjects) (metaobject type: `art_id`)

**Shoe Product:**
1. Create product in Shopify admin
2. Set product type to indicate footwear
3. Add shoe-specific metafields if needed
4. Product will use shoe template automatically

### Updating Collection Content

**Standard Collection:**
1. Add/remove products from collection
2. Update collection description
3. Set collection image

**Team Store Collection:**
1. Set collection template suffix to `team-store-native` or `team-store-landing`
2. Configure collection metafields (see [Data Guide - Team Store Collection Metafields](data-guide.md#team-store-collection-metafields)):
   - `custom.start_date` (date)
   - `custom.end_date` (date)
   - `custom.team_product_data` (JSON)
   - `custom.opportunity_number` (text, optional)
3. Add team store products (products with [`custom.team_gear_product = true`](data-guide.md#team-store-metafields))
4. Configure status messages in template customizer via "Status Key Messages" block

**SearchSpring Collection:**
1. Ensure SearchSpring app is configured
2. Collection will use SearchSpring automatically
3. Configure SearchSpring settings in app

### Creating/Updating Pages

**Standard Page:**
1. Create page in Shopify admin
2. Use theme customizer to add sections
3. Standard sections work as expected

**Specialized Page:**
1. Create page in Shopify admin
2. Set template suffix (e.g., `yotpo-rewards`, `technique-library`)
3. Add content using customizer
4. Configure page-specific metafields if needed

### Updating Team Store Status

**Changing Team Store Dates:**
1. Go to team store collection
2. Edit [collection metafields](data-guide.md#team-store-collection-metafields)
3. Update `custom.start_date` and `custom.end_date`
4. Store will open/close automatically based on dates

**Updating Status Messages:**
1. Go to collection in Shopify admin
2. Click **Customize**
3. Find "Status Key Messages" block
4. Edit messages for Approved, Action Required, In Revision

### Managing Product Images

**Standard Product Images:**
- Upload in product settings
- Standard Shopify image handling

**Team Store Product Images:**
- See [Media Asset Specifications - Team Store Product Images](#team-store-product-images) section for detailed requirements
- Custom images managed via [metaobjects](data-guide.md#team-store-metaobjects) (metaobject type: `art_id`)
- Image gallery controlled by `include_default_images` field in [metaobject](data-guide.md#team-store-metaobjects)
- Image order: Custom images first (if `include_default_images = false`), then model shots (images with `data-image-index` 0010-0019), then detail shots (images with `data-image-index` 0030-0039)
- Image naming convention: Images must have `data-image-index` attribute set to 0010-0019 for model shots or 0030-0039 for detail shots

---

## Troubleshooting

### Team Store Not Showing Products

**Check:**
- Collection template suffix is set to `team-store-native` or `team-store-landing`
- Products have [`custom.team_gear_product = true`](data-guide.md#team-store-metafields) metafield
- [Collection metafields](data-guide.md#team-store-collection-metafields) are set: `custom.start_date`, `custom.end_date`, `custom.team_product_data`
- Products are in the collection

### Product Using Wrong Template

**Check:**
- Product [metafields](data-guide.md#product-metafields) (team gear triggers team store template)
- Product type (footwear automatically uses shoe template)
- Verify automatic assignment logic is working

### Team Store Not Opening/Closing

**Check:**
- [Collection metafields](data-guide.md#team-store-collection-metafields) `custom.start_date` and `custom.end_date` are set (date type)
- Dates are in correct format (YYYY-MM-DD)
- Current date is between start and end dates (store opens when current date > start_date and closes when current date > end_date)

### Custom Images Not Showing on Team Products

**Check:**
- Product has [`custom.is_custom_team_blank = true`](data-guide.md#team-store-metafields) metafield
- [Metaobject](data-guide.md#team-store-metaobjects) (type: `art_id`, handle format: `{parent_sku}_{opportunity_number}`) is configured with image data
- `include_default_images` field in [metaobject](data-guide.md#team-store-metaobjects) is set correctly
- Images have correct `data-image-index` values:
  - Model shots: 0010-0019 (10-19)
  - Detail shots: 0030-0039 (30-39)
  - Images outside these ranges are hidden
- Custom images (no index) display first

### Status Messages Not Displaying

**Check:**
- Collection template suffix is `team-store-native` or `team-store-landing`
- "Status Key Messages" block (type: `status_key_messages`) is added in template customizer
- Messages are configured in block settings: `approved`, `action_required`, `in_revision`
- Product approval status is set in team store workflow

### SearchSpring Not Working

**Check:**
- SearchSpring app is installed and configured
- Collection is set up for SearchSpring
- SearchSpring settings in app dashboard

---

## Quick Reference

### Team Store Setup Checklist

- [ ] Create collection with template suffix `team-store-native` or `team-store-landing`
- [ ] Set [collection metafields](data-guide.md#team-store-collection-metafields): `custom.start_date`, `custom.end_date`, `custom.team_product_data`
- [ ] Add products to collection
- [ ] Set product [metafields](data-guide.md#team-store-metafields): `custom.team_gear_product = true`
- [ ] For customizable blanks: `custom.is_custom_team_blank = true`
- [ ] Set `custom.parent_sku` for team products
- [ ] Configure team product pricing in [metaobjects](data-guide.md#team-store-metaobjects) (type: `art_id`)
- [ ] Configure status messages in template customizer (Status Key Messages block)
- [ ] Test team store access with opportunity number parameter

### Product Template Quick Reference

| Product Type | Template Suffix        | Assignment | Metafields Required                                                                                                             |
| ------------ | ---------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Standard     | (none)                 | Manual     | None                                                                                                                            |
| Shoes        | `shoe-product`         | Manual     | None (product type for organization only)                                                                                       |
| Team Store   | `team-store-pdp`       | Manual     | `custom.team_gear_product = true`, `custom.is_custom_team_blank = true` (see [Data Guide](data-guide.md#team-store-metafields)) |
| Bundles      | `bundles`              | Manual     | Bundle configuration in Shopify                                                                                                 |
| Auction      | `auction-pro-template` | Manual     | Auction-specific metafields                                                                                                     |

**Note:** All template suffixes must be set manually in Shopify Admin. See [Template Assignment](##template-assignment) section for instructions.

### Collection Template Quick Reference

| Collection Type | Template Suffix                             | Assignment | Metafields Required                                                                                                                   |
| --------------- | ------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Standard        | (none)                                      | Manual     | None                                                                                                                                  |
| Team Store      | `team-store-native` or `team-store-landing` | Manual     | `custom.start_date`, `custom.end_date`, `custom.team_product_data` (see [Data Guide](data-guide.md#team-store-collection-metafields)) |
| SearchSpring    | `searchspring`                              | Manual     | SearchSpring app configured                                                                                                           |

**Note:** All template suffixes must be set manually in Shopify Admin. See [Template Assignment](##template-assignment) section for instructions.

---

## Data Reference

For comprehensive documentation of all metafields and metaobjects used in the RUDIS platform, see the **[Data Guide](data-guide.md)**. The Data Guide provides complete reference documentation for all custom data structures, including metafields organized by resource type (Products, Collections, Pages, Customers) and metaobjects with field-level documentation.

---

## Support Resources

- **Technical Documentation:** See [Technical User Guide](technical-user-guide.md) for developers
- **Data Documentation:** See [Data Guide](data-guide.md) for complete metafield and metaobject reference
- **Theme Code:** Located in `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/`
- **Data Exports:** Located in `data/AD-EVERYTHING-Export_2025-10-22_131917/`

**For Advanced Customization:** Refer to Technical User Guide for complete section documentation and customizer options.

---

**Remember:** This guide focuses on RUDIS-specific features. For standard Shopify functionality, refer to Shopify's help documentation.
