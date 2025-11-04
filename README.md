# RUDIS Technical Documentation

**Client:** RUDIS  
**Platform:** Shopify Plus  
**Theme:** CQL Propel v3.0.0  
**Documentation Date:** October 2025  
**Methodology:** ARCDIG-DOCS v1.2.0

---

## Repository Overview

This repository contains comprehensive technical documentation for the RUDIS Shopify Plus eCommerce platform. The documentation follows Arcadia Digital's ARCDIG-DOCS methodology, providing evidence-based technical documentation designed for multiple audiences: developers, operations teams, business users, and AI assistants.

**Repository Purpose:** Complete technical documentation for RUDIS Shopify Plus platform  
**Target Audience:** Developers, operations teams, business users, AI assistants  
**Documentation Philosophy:** Business-first approach with technical depth, evidence-based documentation  
**Document Type:** Complete technical knowledge base with architecture, performance, accessibility, and operational guides

---

## Project Knowledge Base

This README serves as the **static memory file** for the RUDIS technical documentation. It contains all essential information needed for any developer, AI assistant, or team member to understand, maintain, and extend the RUDIS platform without requiring additional context or handoff meetings.

**Key Knowledge Areas:**
- Complete platform architecture overview
- Theme structure and organization
- Third-party integrations and apps
- Performance baseline and optimization roadmap
- Accessibility compliance and remediation guide
- Operational procedures and troubleshooting
- Developer handoff materials

---

## Platform Overview

### Technical Stack

**Platform:** Shopify Plus  
**Theme:** CQL Propel v3.0.0 (Customized)  
**Theme Base:** Dawn OS 2.0  
**Architecture:** Single-store Shopify Plus instance

### Content Structure

- **Products:** 4,517 active products (14,079 total including variants)
- **Collections:** 7,768 total (1,205 smart collections, 6,563 custom collections)
- **Pages:** 200 content pages
- **Blog Posts:** 91 blog posts
- **Redirects:** 3,459 redirect rules
- **Metaobjects:** 45,175 metaobjects
- **Menus:** 29 navigation menus

### Theme Architecture

**File Structure:**
- **Sections:** 124 section files (including main templates and reusable components)
- **Snippets:** 183 snippet files (reusable components, icons, integrations)
- **Templates:** 413 template files (403 JSON templates, 10 Liquid templates)
- **Blocks:** 10 AI-generated blocks identified
- **Assets:** 182 files (126 CSS, 43 JS, 5 fonts, 8 other)

**Key Theme Sections:**
- Product templates: Multiple PDP variants (shoe products, team store, bundles, auctions)
- Collection templates: Native, SearchSpring, team store variants
- Custom sections: Featured products, athlete highlights, storytelling, product journey
- Specialized components: Cart drawer, wishlist, product recommendations

---

## Third-Party Integrations

### Marketing & Email

- **Klaviyo** - Email marketing and customer segmentation
  - Account ID configured in theme settings
  - Back-in-stock notifications
  - Modal integration for email capture

- **Yotpo** - Reviews and rewards program
  - Rewards widget integration
  - Review carousel components
  - Customer loyalty features

### Search & Recommendations

- **SearchSpring** - Advanced search and recommendations
  - IntelliSuggest recommendations
  - Search bundle integration
  - Product recommendations on PDP

- **Native Shopify Search** - Predictive search enabled
  - Custom search templates
  - Search results optimization

### Access Control & Security

- **Locksmith** - Access control and content protection
  - Product/content gating
  - Customer access management
  - Variable initialization in theme

### Analytics & Tracking

- **Elevar** - Data layer and analytics
  - Head and checkout tracking
  - Data layer management

- **CQL** - Custom analytics integration
  - Head content injection
  - Custom tracking scripts

### Customer Service

- **Contivio** - Live chat integration
  - Conditional loading based on theme settings
  - Chat widget integration

- **Zendesk** - Support widget
  - Support chat integration on product pages

### E-commerce Enhancements

- **HulkApps Wishlist** - Wishlist functionality
  - Header wishlist icon
  - Collection/product/cart wishlist buttons
  - Wishlist popup modal

- **Digioh** - Digital gift cards and results pages
  - Lightbox integration
  - Results page template

- **Digismoothie** - Gift box functionality
  - Gift box cart integration

- **Loop Returns** - Returns management
  - Returns widget on checkout and cart

- **Realift** - Product recommendations
  - Category-specific recommendations
  - Product injection script

### Promotions & Discounts

- **Limoniapps Discount Ninja** - Discount management
  - Context signature and status tracking

### Communications

- **SMSBump** - SMS marketing
  - Checkout marketing subscription

---

## Performance Baseline

### Core Web Vitals (Field Data - 75th Percentile)

**Homepage (Index):**
- **LCP:** 3.77s (Target: < 2.5s) ❌ FAILING
- **CLS:** 0.00 (Target: < 0.10) ✅ PASSING
- **INP:** 178ms (Target: < 200ms) ✅ PASSING
- **FCP:** 1.58s ✅ PASSING
- **TTFB:** 544ms ✅ PASSING

**Product Pages:**
- **LCP:** 1.66s (Mobile) ✅ PASSING
- **CLS:** 0.04 (Target: < 0.10) ✅ PASSING
- **INP:** 192ms (Target: < 200ms) ✅ PASSING
- **Page Loads:** 56.6% of total traffic

**Collection Pages:**
- **LCP:** 2.07s (Target: < 2.5s) ✅ PASSING (Near limit)
- **CLS:** 0.11 (Target: < 0.10) ❌ FAILING
- **INP:** 160ms ✅ PASSING
- **Page Loads:** 31.2% of total traffic

**Search Pages:**
- **LCP:** 1.99s ✅ PASSING
- **CLS:** 0.40 (Target: < 0.10) ❌ FAILING
- **INP:** 176ms ✅ PASSING

### Performance Issues Identified

1. **Homepage LCP:** 3.77s exceeds threshold (hero image optimization needed)
2. **Collection CLS:** 0.11 slightly exceeds threshold (layout stability improvements needed)
3. **Search CLS:** 0.40 significantly exceeds threshold (search results layout needs optimization)
4. **Product PDP Mobile:** LCP 8.71s (synthetic) - requires immediate attention

### Performance Optimization Roadmap

**Priority 1 (Do Now):**
- Optimize homepage hero images (WebP/AVIF conversion, responsive sizing)
- Fix collection page layout shifts (reserve space for dynamic content)
- Optimize search results layout (reduce CLS from 0.40)

**Priority 2 (Do Next):**
- Optimize product PDP mobile performance (LCP from 8.71s)
- Implement lazy loading for non-critical images
- Defer non-critical JavaScript bundles

**Priority 3 (Do Later):**
- Review third-party widget loading strategies
- Optimize font loading (preload critical fonts)
- Audit and optimize CSS delivery

---

## Accessibility Compliance

### Current Status

**Overall Accessibility Score:** ~90% (Target: ≥ 95%)

### WCAG 2.2 AA Violations

**Perceivable (4 violations):**
- Missing alt text on hero and product images
- Modal image carousels missing ARIA labeling
- Product images missing alt text in lazy-load templates

**Operable (2 violations):**
- Cookie banner focus traps
- Focus loss when switching variants or opening size chart
- Filter/sort dropdowns lack ARIA states

**Robust (1 violation):**
- Duplicate IDs detected within review widget
- Inconsistent ARIA roles in navigation

### Accessibility Remediation Guide

**Priority 1 (Do Now):**
- Add meaningful alt attributes to all images (hero, product, category)
- Implement ARIA labels for modal galleries
- Fix cookie banner keyboard accessibility

**Priority 2 (Do Next):**
- Add ARIA roles to filter/sort controls
- Implement focus management for variant selection
- Fix duplicate IDs in review widget

**Priority 3 (Do Later):**
- Enhance semantic heading structure
- Refine accordion ARIA support
- Improve navigation ARIA consistency

---

## Documentation Workflow

### Documentation Creation Process

**Important:** Documentation is drafted in Markdown and converted to HTML only after final review and approval.

**Workflow Steps:**

1. **Draft in Markdown** - All new documentation is created as `.md` files in the `docs/` directory
   - Markdown files are for drafting, review, and iteration
   - No markdown files should be linked in `index.html` or navigation

2. **Review & Approval** - Markdown files are reviewed for:
   - Content accuracy and completeness
   - Code references and technical details
   - Business user clarity
   - Formatting and structure

3. **Convert to HTML** - Once approved, markdown files are converted to HTML:
   - HTML files use the shared template structure
   - Include dynamic header/footer loading
   - Maintain consistent styling via `arcadia-style.css`

4. **Add to Navigation** - After HTML conversion:
   - Add link to `index.html` in the appropriate section
   - Update `header.html` navigation menu to include the new page
   - Ensure all HTML pages share the same header navigation

**Key Principles:**
- Markdown = Draft/Review state
- HTML = Published/Final state
- Never link markdown files in HTML navigation
- All HTML pages share consistent header navigation

---

## Documentation Structure

### For Developers

1. **Theme Architecture** - Complete theme structure documentation
2. **Integration Guides** - Third-party app integration details
3. **Customization Guide** - How to modify theme components
4. **Performance Optimization** - Technical performance improvements
5. **Accessibility Implementation** - WCAG compliance fixes

### For Operations

1. **Performance Monitoring** - Core Web Vitals tracking procedures
2. **Troubleshooting Guide** - Common issues and solutions
3. **Maintenance Procedures** - Regular maintenance tasks
4. **Content Management** - Managing products, collections, pages

### For Business Users

1. **Platform Overview** - High-level platform description
2. **Performance Metrics** - Current performance status
3. **Accessibility Status** - Compliance overview
4. **Navigation Hub** - Documentation directory

### For AI Assistants

1. **This README** - Complete static memory file
2. **Architecture Documentation** - Technical system details
3. **Evidence-Based Documentation** - All documentation based on actual codebase

---

## Key Files Reference

### Theme Code
- **Location:** `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/`
- **Layout:** `layout/theme.liquid` - Main theme layout
- **Sections:** `sections/` - 124 section files
- **Snippets:** `snippets/` - 183 snippet files
- **Templates:** `templates/` - 413 template files
- **Config:** `config/settings_schema.json` - Theme settings

### Data Exports
- **Location:** `data/AD-EVERYTHING-Export_2025-10-22_131917/`
- **Products:** Products.csv (4,517 active)
- **Collections:** Custom Collections.csv, Smart Collections.csv
- **Pages:** Pages.csv (200 pages)
- **Redirects:** Redirects.csv (3,459 redirects)

### Performance Reports
- **Location:** `data/shopify-reports/`
- **LCP Reports:** Largest Contentful Paint (LCP) by page type
- **CLS Reports:** Cumulative Layout Shift (CLS) by page type
- **INP Reports:** Interaction to Next Paint (INP) by page type

### Prework Audits
- **Location:** `prework/`
- **Homepage Audit:** `rudis-homepage-audit.md`
- **PLP Audit:** `rudis-plp-audit.md`
- **PDP Audit:** `rudis-pdp-audit.md`
- **Issues & Recommendations:** `RUDIS Website Audit – Issues & Recommendations.md`

---

## Methodology

This documentation follows the **ARCDIG-DOCS v1.2.0** methodology:

- **Evidence-Based Documentation:** All documentation based on actual theme code, data exports, and performance reports
- **Business-First Approach:** Written for business users with technical depth available
- **Multi-Audience Support:** Different documentation paths for different user types
- **Client Ownership:** Designed for seamless handoff and long-term maintenance

---

## Contact & Support

**Maintained by:** Arcadia Digital  
**Documentation Date:** October 2025  
**Last Updated:** October 31, 2025

For questions or updates to this documentation:
- Review prework audits for detailed findings
- Reference theme code exports for technical details
- Check performance reports for current metrics
- Follow ARCDIG-DOCS methodology for updates

---

_This README serves as a static memory file for developers, AI assistants, and team members working with the RUDIS platform. It provides complete context for understanding, maintaining, and extending the RUDIS Shopify Plus store._

