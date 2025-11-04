# RUDIS Theme Architecture

**Last Updated:** October 31, 2025  
**Theme:** CQL Propel v3.0.0  
**Base:** Dawn OS 2.0 (Customized)

---

## Overview

The RUDIS Shopify Plus store uses a heavily customized version of the CQL Propel theme (v3.0.0), which is based on Shopify's Dawn OS 2.0 theme. The theme has been extensively modified to support RUDIS-specific features including team stores, athlete product highlights, auction functionality, and multiple product template variants.

---

## Theme Structure

### File Organization

**Total Files:**
- **Sections:** 124 files (including main templates and reusable components)
- **Snippets:** 183 files (reusable components, icons, integrations)
- **Templates:** 413 files (403 JSON templates, 10 Liquid templates)
- **Blocks:** 10 AI-generated blocks identified
- **Assets:** 182 files (126 CSS, 43 JS, 5 fonts, 8 other)

### Directory Structure

```
theme_export/
├── assets/          # CSS, JS, fonts, images (182 files)
├── blocks/          # AI-generated blocks (10 files)
├── config/          # Theme settings and configuration
├── layout/          # Theme layouts (4 files)
├── locales/         # Translation files (multi-language support)
├── sections/        # Theme sections (124 files)
├── snippets/        # Reusable components (183 files)
└── templates/       # Page templates (413 files)
```

---

## Key Sections

### Product Templates

**Main Product Templates:**
- `main-product.liquid` - Standard product template
- `main-product-shoe.liquid` - Shoe-specific product template
- `main-product-team-store.liquid` - Team store product template
- `main-product-bundles.liquid` - Bundle product template
- `main-product-auction.liquid` - Auction product template
- `main-product-new.liquid` - New product variant
- `main-shoe-product.liquid` - Alternative shoe template

**Specialized Product Sections:**
- `pdp-storytelling.liquid` - Product storytelling component
- `pdp-win-more.liquid` - Win-more product section
- `product-journey.liquid` - Product journey component
- `product-description.liquid` - Product description section
- `product-recommendations.liquid` - Product recommendations
- `related-products.liquid` - Related products section
- `specifications.liquid` - Product specifications

### Collection Templates

**Main Collection Templates:**
- `main-collection-product-grid.liquid` - Standard collection grid
- `main-collection-product-grid-native.liquid` - Native Shopify search
- `main-collection-product-grid-ss.liquid` - SearchSpring integration
- `main-collection-product-grid-team-store.liquid` - Team store collection
- `main-collection-team-store.liquid` - Team store collection page
- `main-collection-banner.liquid` - Collection banner section
- `main-collection-seo-content.liquid` - SEO content section
- `main-list-collections.liquid` - Collection listing page

**Collection Features:**
- `collection-list.liquid` - Collection list component
- `collection-pills.liquid` - Collection pills navigation
- `plp-recent-drops.liquid` - Recent drops section
- `featured-collections.liquid` - Featured collections
- `featured-collections-enhanced.liquid` - Enhanced featured collections

### Page Templates

**Main Page Templates:**
- `main-page.liquid` - Standard page template
- `main-page-styleguide.liquid` - Style guide page
- `main-page-yotpo-rewards.liquid` - Yotpo rewards page
- `page-content.liquid` - Page content section

**Specialized Pages:**
- `page.digioh-results.liquid` - Digioh results page
- Custom page templates for various content types

### Search Templates

**Search Components:**
- `main-search.liquid` - Standard search template
- `main-search-native.liquid` - Native Shopify search
- `predictive-search.liquid` - Predictive search component
- `search-no-results-boundary.liquid` - No results boundary
- `searchspring-recommendations.liquid` - SearchSpring recommendations

### Cart & Checkout

**Cart Components:**
- `main-cart-items.liquid` - Cart items section
- `main-cart-footer.liquid` - Cart footer
- `main-cart-add-ons.liquid` - Cart add-ons
- `cart-drawer.liquid` - Cart drawer component
- `cart-icon-bubble.liquid` - Cart icon with bubble
- `cart-notification-button.liquid` - Cart notification button
- `cart-notification-product.liquid` - Cart notification product
- `cart-recommendation.liquid` - Cart recommendations
- `cart-upsell.liquid` - Cart upsell section

### Header & Navigation

**Header Components:**
- `header.liquid` - Main header section
- `header-group.json` - Header group configuration
- `menu-bar.liquid` - Menu bar component
- `menu-drawer-list.liquid` - Menu drawer list
- `menu-header-drawer.liquid` - Menu header drawer
- `menu-link-item.liquid` - Menu link item
- `menu-list.liquid` - Menu list component
- `menu-search-modal.liquid` - Search modal
- `menu-search.liquid` - Search component

### Footer

**Footer Components:**
- `footer.liquid` - Main footer section
- `footer-group.json` - Footer group configuration

### Content Sections

**Banner & Hero:**
- `animated-hero.liquid` - Animated hero section
- `image-banner.liquid` - Image banner
- `image-banner-data.liquid` - Image banner with data
- `banner-grid.liquid` - Banner grid
- `email-signup-banner.liquid` - Email signup banner
- `promos-banner.liquid` - Promos banner
- `team-store-banner.liquid` - Team store banner

**Content Blocks:**
- `rich-text.liquid` - Rich text section
- `collapsible-content.liquid` - Collapsible content
- `info-accordion.liquid` - Info accordion
- `info-carousel.liquid` - Info carousel
- `multicolumn.liquid` - Multi-column section
- `multicolumn-cards.liquid` - Multi-column cards
- `multicolumn-data.liquid` - Multi-column with data
- `multicolumn-steps.liquid` - Multi-column steps
- `multirow.liquid` - Multi-row section
- `multirow-data.liquid` - Multi-row with data

**Product Display:**
- `featured-product.liquid` - Featured product
- `featured-products.liquid` - Featured products
- `featured-products-athlete.liquid` - Athlete featured products
- `dynamic-product-highlight.liquid` - Dynamic product highlight
- `product-recommendations.liquid` - Product recommendations
- `complete-the-look-icons.liquid` - Complete the look icons
- `shop-the-look.liquid` - Shop the look section

**Media:**
- `video.liquid` - Video section
- `uploaded-video.liquid` - Uploaded video
- `slideshow.liquid` - Slideshow section
- `spotlight.liquid` - Spotlight section
- `collage.liquid` - Collage section

**Special Features:**
- `feature-diagram.liquid` - Feature diagram
- `inset-feature-diagram.liquid` - Inset feature diagram
- `key-features.liquid` - Key features
- `features-list.liquid` - Features list
- `icon-list.liquid` - Icon list
- `social-media-feed.liquid` - Social media feed
- `news-press.liquid` - News and press section

---

## Key Snippets

### Integration Snippets

**Third-Party Integrations:**
- `klaviyo-modal.liquid` - Klaviyo email capture modal
- `contivio-scripts.liquid` - Contivio live chat
- `elevar-head.liquid` - Elevar analytics head
- `elevar-head-listener.liquid` - Elevar listener
- `elevar-body-end.liquid` - Elevar body end
- `elevar-checkout-end.liquid` - Elevar checkout end
- `cql-head-content.liquid` - CQL analytics head
- `searchspring-script.liquid` - SearchSpring script
- `hulkapps-wishlist-*.liquid` - HulkApps wishlist components
- `hulkappsWishlistPopup.liquid` - Wishlist popup
- `locksmith.liquid` - Locksmith access control
- `locksmith-variables.liquid` - Locksmith variables
- `locksmith-content-variables.liquid` - Locksmith content variables
- `realift.liquid` - Realift recommendations
- `yotpo-full-css.css` - Yotpo styling (in assets)

### Product Components

**Product Display:**
- `product-card.liquid` - Product card component
- `product-card-team-store.liquid` - Team store product card
- `product-card-featured-collections.liquid` - Featured collections card
- `product-media.liquid` - Product media gallery
- `product-media-gallery.liquid` - Product media gallery component
- `product-media-modal.liquid` - Product media modal
- `product-thumbnail.liquid` - Product thumbnail
- `product-options.liquid` - Product options
- `product-variant-options.liquid` - Variant options
- `product-variant-picker.liquid` - Variant picker
- `variant-matrix.liquid` - Variant matrix
- `buy-buttons.liquid` - Buy buttons
- `add-to-cart-b2b.liquid` - B2B add to cart
- `single-variant-product-form.liquid` - Single variant form
- `sticky-add-to-cart.liquid` - Sticky add to cart

**Product Features:**
- `complete-the-look-product.liquid` - Complete the look
- `dynamic-product-grid.liquid` - Dynamic product grid
- `digioh-card-product.liquid` - Digioh product card
- `digismoothie-giftbox.liquid` - Gift box integration

### Cart Components

**Cart Functionality:**
- `cart-drawer.liquid` - Cart drawer
- `cart-notification.liquid` - Cart notification
- `cart-notification-modal.liquid` - Cart notification modal
- `cart-gift-messaging.liquid` - Gift messaging
- `cart-upsell.liquid` - Cart upsell
- `rudis-plus-cart-drawer.liquid` - RUDIS Plus cart drawer

### Navigation & UI

**Navigation:**
- `breadcrumbs.liquid` - Breadcrumb navigation
- `menu-list.liquid` - Menu list
- `menu-list-image.liquid` - Menu list with images
- `menu-list-promos.liquid` - Menu list with promos
- `menu-list-activity.liquid` - Menu list activity
- `menu-link-item.liquid` - Menu link item
- `menu-search.liquid` - Search component
- `menu-search-modal.liquid` - Search modal

**UI Components:**
- `button.liquid` - Button component
- `icon-*.liquid` - Icon components (50+ icon files)
- `image.liquid` - Image component
- `scaled-image.liquid` - Scaled image
- `background-media.liquid` - Background media
- `loading-overlay.liquid` - Loading overlay
- `skeleton-loader.liquid` - Skeleton loader

### Forms & Inputs

**Form Components:**
- `contact-form.liquid` - Contact form
- `newsletter-form.liquid` - Newsletter form
- `addon-form.liquid` - Add-on form
- `gift-card-recipient-form.liquid` - Gift card recipient form
- `team-store-revision-form.liquid` - Team store revision form
- `last-name-option.liquid` - Last name option

### Utilities

**Helper Snippets:**
- `meta-tags.liquid` - Meta tags
- `money.liquid` - Money formatting
- `price.liquid` - Price display
- `description.liquid` - Description component
- `headline.liquid` - Headline component
- `eyebrow.liquid` - Eyebrow component
- `padding.liquid` - Padding utility
- `pagination.liquid` - Pagination
- `share-button.liquid` - Share button
- `social-icons.liquid` - Social icons
- `social-media.liquid` - Social media component

**Localization:**
- `language-localization.liquid` - Language localization
- `country-localization.liquid` - Country localization

**Feature Flags:**
- `feature-flag-content.liquid` - Feature flag content
- `function.is_menu_item_hidden.liquid` - Menu item visibility function

---

## Template Variants

### Product Templates

**Standard Templates:**
- `product.json` - Default product template
- `product.alternate.json` - Alternate product template
- `product.with-free-returns-text.json` - Free returns template
- `product.no-reviews.json` - No reviews template
- `product.default-product-reviews.json` - Default reviews template

**Shoe Templates:**
- `product.shoe-product.json` - Shoe product template
- `product.ecom-store-shoe-pdp.json` - Ecom store shoe PDP
- `product.ds-shoe-pdp.json` - DS shoe PDP
- `product.jb-shoe-pdp.json` - JB shoe PDP
- `product.ks-shoe-pdp.json` - KS shoe PDP
- `product.sh-wrestling-shoe.json` - Wrestling shoe template
- `product.one-of-one-wrestling-shoe.json` - One-of-one wrestling shoe

**Brand/Athlete Templates:**
- `product.kolat.json` - Kolat product template
- `product.rocky.json` - Rocky product template
- `product.hildebrandt.json` - Hildebrandt template
- `product.jb-ultra-ps.json` - JB Ultra PS template
- `product.jb-ultralite.json` - JB Ultralite template
- `product.chronicle-elite.json` - Chronicle Elite template
- `product.alpha-2-0-happy.json` - Alpha 2.0 template
- `product.tmnt.json` - TMNT template

**Specialized Templates:**
- `product.bundles.json` - Bundle products
- `product.bags.json` - Bag products
- `product.bag-gen3.json` - Bag gen 3
- `product.bag_gen4.json` - Bag gen 4
- `product.bag_cinch.json` - Bag cinch
- `product.shoe-bag-product.json` - Shoe bag product
- `product.pdp-shoe-bag.json` - PDP shoe bag
- `product.gift-card.json` - Gift card template
- `product.auction-pro-template.json` - Auction pro template
- `product.auction-pro-wrestle-gang.json` - Auction wrestle gang
- `product.daily-deals-temp.json` - Daily deals
- `product.jb-dailydeal-ps.json` - JB daily deal PS
- `product.jb-dailydeals-ps-eagle.json` - JB daily deals eagle
- `product.colorblock-collection.json` - Colorblock collection
- `product.colorblock-2.json` - Colorblock 2
- `product.usaw-domestic.json` - USAW domestic
- `product.extention-pad.json` - Extension pad
- `product.coming-soon.json` - Coming soon
- `product.newshoe0926.json` - New shoe template
- `product.team-store-pdp.json` - Team store PDP
- `product.pdp-team.json` - PDP team

### Page Templates

**Standard Pages:**
- `page.json` - Default page template

**Specialized Pages:**
- `page.yotpo-rewards.json` - Yotpo rewards page
- `page.digioh-results.liquid` - Digioh results page
- `page.styleguide.liquid` - Style guide page
- `page.signup-form.json` - Signup form
- `page.signup-form-02.json` - Signup form variant 2
- `page.signup-form-3.json` - Signup form variant 3
- `page.new-arrivals.json` - New arrivals page
- `page.new-to-rudis.json` - New to RUDIS page
- `page.womens-wrestling.json` - Women's wrestling page
- `page.kolat.json` - Kolat page
- `page.2024-sneak-peak.json` - 2024 sneak peak
- `page.all-in-styleguideunisex.json` - Style guide unisex

---

## Theme Configuration

### Settings Schema

**Theme Settings Structure:**
- Global animations settings
- Header configuration
- Footer configuration
- Color scheme settings
- Typography settings
- Product page settings
- Collection page settings
- Cart settings
- Checkout settings
- Third-party app integrations

### Key Settings

**Integrations:**
- Klaviyo account ID
- Live chat enable/disable
- Predictive search enable/disable
- Various third-party app configurations

**Customization:**
- Logo settings
- Favicon settings
- Color palette
- Font selections
- Animation preferences

---

## Custom Features

### Team Store Functionality

**Team Store Components:**
- Team store product templates
- Team store collection templates
- Team store cart drawer
- Team store banner
- Team store revision form
- Team info modal
- Team cart properties

### Athlete Features

**Athlete-Specific Components:**
- Featured products athlete section
- Athlete product highlights
- Custom product templates for athletes

### Auction Functionality

**Auction Components:**
- Auction product templates
- Auction-specific product pages

### Bundle Functionality

**Bundle Components:**
- Bundle product template
- Bundle-specific sections

---

## AI-Generated Blocks

**Identified Blocks:**
- `ai_gen_block_0ecfeb7.liquid`
- `ai_gen_block_13f7814.liquid`
- `ai_gen_block_1f1dcce.liquid`
- `ai_gen_block_23f8290.liquid`
- `ai_gen_block_2f228e6.liquid`
- `ai_gen_block_37287c4.liquid`
- `ai_gen_block_66d262d.liquid`
- `ai_gen_block_957da1c.liquid`
- `ai_gen_block_b81555d.liquid`
- `ai_gen_block_bf79238.liquid`

These blocks appear to be custom sections created for specific use cases. Review individual block files for specific functionality.

---

## Theme Customization Guide

### Adding New Sections

1. Create new section file in `sections/` directory
2. Add section schema with settings
3. Include section in template JSON files where needed
4. Test section functionality across device types

### Modifying Existing Components

1. Locate component in `sections/` or `snippets/` directory
2. Make modifications while preserving schema structure
3. Test changes in development environment
4. Deploy to staging for QA
5. Deploy to production after approval

### Adding Third-Party Integrations

1. Create snippet file in `snippets/` directory
2. Include snippet in `layout/theme.liquid` or relevant section
3. Add configuration settings to `config/settings_schema.json`
4. Test integration functionality
5. Document integration in theme architecture

---

## Maintenance Notes

### Backup Files

**Identified Backup Files:**
- `layout/giftbox-backup-20231113T191001Z-theme.liquid`
- `layout/giftbox-backup-20231212T141123Z-theme.liquid`
- `sections/giftbox-backup-*.liquid` files

These backup files should be reviewed and potentially removed if no longer needed.

### File Organization

**Recommendations:**
- Review and consolidate duplicate templates
- Remove unused backup files
- Document purpose of AI-generated blocks
- Organize snippets by functionality category

---

## References

- **Theme Code Location:** `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/`
- **Settings Schema:** `config/settings_schema.json`
- **Settings Data:** `config/settings_data.json`
- **Main Layout:** `layout/theme.liquid`

---

_This documentation is based on analysis of the exported theme code from October 29, 2025. All file counts and structure information are accurate as of the export date._

