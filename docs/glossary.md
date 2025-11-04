# Glossary

**Last Updated:** October 31, 2025

This glossary defines key terms, abbreviations, and concepts used throughout the RUDIS documentation.

---

## A

### Animated Hero
A custom section that displays a sequence of images that animate based on scroll position. Uses a filename prefix system for dynamic image loading.

**Related:** [Technical User Guide - Animated Hero](technical-user-guide.md#animated-hero)

---

### ARCDIG-DOCS
Arcadia Digital's documentation methodology (v1.2.0) used for creating evidence-based technical documentation. Focuses on business-first approach with technical depth.

---

### Art ID (Metaobject)
A metaobject type used for team store product configuration. Contains pricing tiers, custom images, and product specifications. Handle format: `{parent_sku}_{opportunity_number}`.

**Related:** [Data Guide - Art ID Metaobject](data-guide.md#art_id-metaobject)

---

## C

### CLS (Cumulative Layout Shift)
A Core Web Vital metric measuring visual stability. CLS quantifies how much visible content shifts during page load. Target: < 0.10.

**Related:** [Performance Documentation](performance.md#cumulative-layout-shift-cls)

---

### Coming Soon (Metafield)
A product metafield (`custom.coming_soon`) that indicates if a product is coming soon. When set to `true`, Klaviyo "Notify Me" button is hidden.

---

### Core Web Vitals
Google's user experience metrics: LCP (Largest Contentful Paint), CLS (Cumulative Layout Shift), and INP (Interaction to Next Paint). Used to measure page performance.

**Related:** [Performance Documentation](performance.md#core-web-vitals)

---

### Customizer
Shopify's theme editor where sections, blocks, and settings can be configured without code. Accessible via Shopify Admin → Online Store → Themes → Customize.

---

## D

### Dawn OS 2.0
The base theme that CQL Propel v3.0.0 is built upon. Dawn is Shopify's reference theme.

---

## E

### Elevar
Third-party analytics integration that provides enhanced e-commerce tracking for Google Tag Manager. Automates data layer population.

**Related:** [Integrations - Elevar](integrations.md#elevar-conversion-tracking)

---

## F

### Filename Prefix
A naming convention used in Animated Hero sections. Images are named `{prefix}__{number}.{extension}` (e.g., `hero-2024__0.jpg`).

**Related:** [Technical User Guide - Filename Prefix System](technical-user-guide.md#filename-prefix-system)

---

## I

### INP (Interaction to Next Paint)
A Core Web Vital metric measuring interactivity. INP quantifies responsiveness to user interactions. Target: < 200ms.

**Related:** [Performance Documentation](performance.md#interaction-to-next-paint-inp)

---

### IntelliSuggest
SearchSpring's autocomplete feature that provides search suggestions as users type. Integrated on product pages.

**Related:** [Integrations - SearchSpring](integrations.md#searchspring)

---

### Is Custom Team Blank (Metafield)
A product metafield (`custom.is_custom_team_blank`) that marks a product as a customizable team store blank. Required for team store products.

**Related:** [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)

---

## K

### Klaviyo
Email marketing and SMS platform integrated with RUDIS. Handles back-in-stock notifications and email capture.

**Related:** [Integrations - Klaviyo](integrations.md#klaviyo-email-marketing--sms)

---

## L

### LCP (Largest Contentful Paint)
A Core Web Vital metric measuring loading performance. LCP marks when the largest content element becomes visible. Target: < 2.5s.

**Related:** [Performance Documentation](performance.md#largest-contentful-paint-lcp)

---

### Locksmith
Access control app that gates products, collections, and pages. Used for team store access control and product restrictions.

**Related:** [Integrations - Locksmith](integrations.md#locksmith)

---

## M

### Metaobject
A reusable data structure in Shopify that can be referenced across multiple resources. RUDIS uses metaobjects for content (e.g., `animated_hero`, `product_journey`) and team store configuration (e.g., `art_id`).

**Related:** [Data Guide - Metaobjects](data-guide.md#metaobjects)

---

### Metafield
Custom data fields in Shopify that extend product, collection, page, customer, and other resource data. RUDIS uses metafields extensively for custom functionality.

**Related:** [Data Guide - Metafields](data-guide.md#metafields)

---

## O

### Opportunity Number
A unique identifier for team store access. Stored in customer location metafields (`custom.opportunity_number`) and passed via URL parameter (`?opportunity_number={number}`).

**Related:** [Technical User Guide - Team Store Access](technical-user-guide.md#team-store-access)

---

## P

### Parent SKU (Metafield)
A product metafield (`custom.parent_sku`) that links team store products to their parent/base product. Format: `{sku_prefix}{base_sku}`.

**Related:** [Data Guide - Parent SKU](data-guide.md#parent_sku)

---

### PDP (Product Detail Page)
The product page template. RUDIS has multiple PDP variants: standard, shoe-product, team-store-pdp, bundles, auction-pro-template.

**Related:** [Technical User Guide - Product Templates](technical-user-guide.md#product-templates)

---

### PLP (Product Listing Page)
Another term for collection page. Displays a grid of products from a collection.

**Related:** [Technical User Guide - Collection Templates](technical-user-guide.md#collection-templates)

---

## S

### SearchSpring
Advanced search and filtering platform integrated with RUDIS. Provides enhanced search functionality, filtering, and product recommendations on collection pages.

**Related:** [Integrations - SearchSpring](integrations.md#searchspring)

---

### Section
A reusable theme component in Shopify. Sections can be added to templates via the customizer. RUDIS has 124 section files.

**Related:** [Technical User Guide - Customizer Sections](technical-user-guide.md#customizer-sections)

---

### Snippet
A reusable Liquid code fragment in Shopify themes. Snippets are included via `{% render %}`. RUDIS has 183 snippet files.

**Related:** [Technical User Guide - Snippets](technical-user-guide.md#snippets)

---

## T

### Team Gear Product (Metafield)
A product metafield (`custom.team_gear_product`) that marks a product as part of a team store. Required for team store products.

**Related:** [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)

---

### Team Store
A B2B micro-site concept built into the RUDIS theme. Each team store is a collection with custom template suffixes (`team-store-native` or `team-store-landing`) that provides a customized shopping experience for wrestling teams.

**Related:** [Technical User Guide - Team Stores](technical-user-guide.md#team-stores)

---

### Template
A Liquid template file that defines the structure of a page type (product, collection, page). Templates are JSON files that reference sections.

**Related:** [Technical User Guide - Template Assignment System](technical-user-guide.md#template-assignment-system)

---

### Template Suffix
A Shopify feature that allows multiple template variants for the same resource type. Templates are named `{type}.{suffix}.json` (e.g., `product.team-store-pdp.json`). Suffixes are set manually in Shopify Admin.

**Related:** [Technical User Guide - Template Suffixes](technical-user-guide.md#understanding-template-suffixes)

---

### Tier Pricing
A pricing structure in team stores where prices vary based on customer price level. Configured in `art_id` metaobject via `tier_pricing` JSON field.

**Related:** [Data Guide - Tier Pricing](data-guide.md#tier-pricing)

---

## W

### WCAG (Web Content Accessibility Guidelines)
Accessibility standards published by W3C. RUDIS targets WCAG 2.2 AA compliance.

**Related:** [Accessibility Documentation](accessibility.md)

---

## Y

### Yotpo
Reviews and rewards platform integrated with RUDIS. Provides product reviews, star ratings, and loyalty program features.

**Related:** [Integrations - Yotpo](integrations.md#yotpo-product-reviews)

---

## Abbreviations

| Abbreviation | Full Term                            |
| ------------ | ------------------------------------ |
| **B2B**      | Business-to-Business                 |
| **CLS**      | Cumulative Layout Shift              |
| **FCP**      | First Contentful Paint               |
| **GTM**      | Google Tag Manager                   |
| **INP**      | Interaction to Next Paint            |
| **LCP**      | Largest Contentful Paint             |
| **PDP**      | Product Detail Page                  |
| **PLP**      | Product Listing Page                 |
| **SKU**      | Stock Keeping Unit                   |
| **TTFB**     | Time to First Byte                   |
| **WCAG**     | Web Content Accessibility Guidelines |

---

## RUDIS-Specific Terms

### Team Store Types

- **Team Store Native:** Collection template suffix (`team-store-native`) for standard team stores
- **Team Store Landing:** Collection template suffix (`team-store-landing`) for team store landing pages
- **Team Store PDP:** Product template suffix (`team-store-pdp`) for team store product pages

### Product Types

- **Shoe Product:** Product template suffix (`shoe-product`) for footwear products
- **Bundle Product:** Product template suffix (`bundles`) for bundle/kits
- **Auction Product:** Product template suffix (`auction-pro-template`) for auction items

### Content Metaobjects

- **Animated Hero:** Hero section with scroll-based image animation
- **Product Journey:** Product storytelling component
- **Image Banner:** Image banner section
- **Multi-Column:** Multi-column content layout
- **Multi-Row:** Multi-row content layout
- **Complete the Look:** Product recommendation section
- **Key Features:** Product features section
- **Shop the Collection:** Collection recommendation section
- **Breadcrumbs:** Navigation breadcrumb component

---

## Shopify Terms

### Theme Structure

- **Layout:** Main theme wrapper (`theme.liquid`)
- **Template:** Page type template (product, collection, page)
- **Section:** Reusable theme component
- **Snippet:** Reusable Liquid code fragment
- **Asset:** Static file (CSS, JS, images, fonts)

### Customizer

- **Section:** Theme section added to template
- **Block:** Configurable content block within a section
- **Settings:** Section/block configuration options

### Data

- **Metafield:** Custom data field
- **Metaobject:** Reusable data structure
- **Namespace:** Metafield grouping (e.g., `custom`, `reviews`)

---

## Performance Terms

### Core Web Vitals

- **LCP (Largest Contentful Paint):** Loading performance metric
- **CLS (Cumulative Layout Shift):** Visual stability metric
- **INP (Interaction to Next Paint):** Interactivity metric
- **FCP (First Contentful Paint):** Initial rendering metric
- **TTFB (Time to First Byte):** Server response time metric

### Performance Targets

- **LCP:** < 2.5 seconds (good)
- **CLS:** < 0.10 (good)
- **INP:** < 200ms (good)
- **FCP:** < 1.8 seconds (good)
- **TTFB:** < 800ms (good)

**Related:** [Performance Documentation](performance.md)

---

## Integration Terms

### Analytics

- **Elevar:** Enhanced e-commerce tracking
- **GTM:** Google Tag Manager
- **Data Layer:** JavaScript object for tracking data

### Marketing

- **Klaviyo:** Email marketing platform
- **Back-in-Stock:** Product availability notifications

### Search

- **SearchSpring:** Advanced search platform
- **IntelliSuggest:** Autocomplete search feature

### Reviews

- **Yotpo:** Reviews and ratings platform
- **Rich Snippets:** Structured data for search engines

---

## Documentation Terms

### File Types

- **Markdown (.md):** Draft documentation format
- **HTML (.html):** Published documentation format

### Documentation Workflow

- **Draft:** Markdown files in `docs/` directory
- **Review:** Content accuracy and completeness check
- **Publish:** Convert to HTML and add to navigation

**Related:** [Documentation Creation Process](README.md#documentation-creation-process)

---

## Additional Resources

- [Technical User Guide](technical-user-guide.md) - Complete technical documentation
- [Business User Guide](business-user-guide.md) - Content management workflows
- [Data Guide](data-guide.md) - Complete metafield and metaobject reference
- [Quick Reference](QUICK_REFERENCE.md) - Quick lookup guide

---

**Last Updated:** October 31, 2025  
**Suggestions:** If you encounter a term not defined here, please suggest it for addition to this glossary.

