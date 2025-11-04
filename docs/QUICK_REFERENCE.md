# RUDIS Quick Reference Guide

**Last Updated:** October 31, 2025

---

## Platform Overview

- **Platform:** Shopify Plus
- **Theme:** CQL Propel v3.0.0 (Customized Dawn OS 2.0)
- **Store URL:** https://www.rudis.com

---

## Key Metrics

### Performance (Field Data - 75th Percentile)

| Page Type  | LCP   | CLS  | INP   | Status           |
| ---------- | ----- | ---- | ----- | ---------------- |
| Product    | 1.66s | 0.04 | 192ms | ✅ Passing        |
| Collection | 2.07s | 0.11 | 160ms | ⚠️ CLS Near Limit |
| Homepage   | 3.77s | 0.00 | 178ms | ❌ LCP Failing    |
| Search     | 1.99s | 0.40 | 176ms | ❌ CLS Failing    |

### Accessibility

- **Current Score:** ~90% (Target: ≥ 95%)
- **WCAG 2.2 AA Compliance:** 4 perceivable violations, 2 operable violations

---

## Critical Issues

### Do Now (Priority 1)

1. **Homepage LCP:** 3.77s exceeds threshold
   - Optimize hero images (WebP/AVIF, responsive sizing)
   - Preload LCP image

2. **Missing Alt Text:** Many images lack descriptive alt text
   - Add alt text to product images, hero banners, category thumbnails

3. **Collection CLS:** 0.11 slightly exceeds threshold
   - Reserve layout space for product grid
   - Debounce filter/sort events

### Do Next (Priority 2)

1. **Product PDP Mobile:** LCP 8.71s (synthetic)
   - Optimize product gallery images
   - Fix layout shifts from reviews/CTAs
   - Reduce main-thread blocking

2. **Search CLS:** 0.40 significantly exceeds threshold
   - Reserve layout space for search results
   - Optimize SearchSpring integration

3. **Accessibility Improvements:**
   - Fix cookie banner keyboard accessibility
   - Add ARIA labels to modal galleries
   - Implement focus management for variant selection

---

## Theme Structure

- **Sections:** 124 files
- **Snippets:** 183 files
- **Templates:** 413 files
- **Blocks:** 10 AI-generated blocks

**Key Locations:**
- Main Layout: `layout/theme.liquid`
- Product Templates: `sections/main-product*.liquid`
- Collection Templates: `sections/main-collection*.liquid`
- Integration Snippets: `snippets/` (klaviyo, yotpo, searchspring, etc.)

---

## Third-Party Integrations

### Marketing & Email
- **Klaviyo** - Email marketing
- **Yotpo** - Reviews and rewards

### Search & Recommendations
- **SearchSpring** - Advanced search
- **Native Shopify Search** - Predictive search

### Access Control
- **Locksmith** - Content protection

### Analytics
- **Elevar** - Data layer
- **CQL** - Custom analytics

### Customer Service
- **Contivio** - Live chat
- **Zendesk** - Support widget

### E-commerce
- **HulkApps Wishlist** - Wishlist functionality
- **Digioh** - Digital gift cards
- **Loop Returns** - Returns management
- **Realift** - Product recommendations

---

## Content Structure

- **Products:** 4,517 active (14,079 total including variants)
- **Collections:** 7,768 total (1,205 smart, 6,563 custom)
- **Pages:** 200 content pages
- **Blog Posts:** 91 posts
- **Redirects:** 3,459 redirect rules

---

## Documentation Files

- **README.md** - Static memory file (complete project context)
- **docs/theme-architecture.md** - Theme structure documentation
- **docs/performance.md** - Performance baseline and optimization
- **docs/accessibility.md** - WCAG compliance and remediation

---

## Quick Actions

### Optimize Homepage Performance
1. Convert hero images to WebP/AVIF
2. Implement responsive `<picture>` elements
3. Preload LCP image in `<head>`
4. Reduce image sizes to device-appropriate dimensions

### Improve Accessibility
1. Add alt text to all images
2. Fix cookie banner keyboard navigation
3. Add ARIA labels to interactive elements
4. Implement focus management for variants

### Fix Collection Page CLS
1. Reserve layout space for product grid
2. Implement skeleton loaders
3. Debounce filter/sort events
4. Preload product thumbnails

---

## Contact & Support

**Maintained by:** Arcadia Digital  
**Documentation Date:** October 2025  
**GitHub Repository:** https://github.com/petebuzzell-ad/rudis-documentation

---

_This quick reference guide provides essential information for immediate use. For detailed documentation, see the full documentation files._

