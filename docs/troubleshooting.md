# Troubleshooting Guide

**Last Updated:** October 31, 2025  
**For:** Developers, Content Managers, Operations Teams

This guide provides solutions to common issues encountered when working with the RUDIS Shopify Plus platform.

---

## Table of Contents

1. [Template Issues](#template-issues)
2. [Team Store Issues](#team-store-issues)
3. [Metafield Issues](#metafield-issues)
4. [Image Issues](#image-issues)
5. [Performance Issues](#performance-issues)
6. [Integration Issues](#integration-issues)
7. [Content Issues](#content-issues)
8. [Accessibility Issues](#accessibility-issues)

---

## Template Issues

### Template Not Displaying Correctly

**Symptoms:**
- Product/collection/page uses wrong template
- Custom template sections not appearing
- Layout looks different than expected

**Solution:**

1. **Verify Template Suffix:**
   - Navigate to product/collection/page in Shopify Admin
   - Go to **Search engine listing** section
   - Check **Template suffix** dropdown
   - Ensure correct suffix is selected (e.g., `team-store-pdp`, `shoe-product`)

2. **Check Template File Exists:**
   - Verify template file exists in theme: `templates/product.{suffix}.json`
   - Check theme code location: `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/templates/`

3. **Clear Cache:**
   - Save changes in Shopify Admin
   - Hard refresh browser (Cmd/Ctrl + Shift + R)
   - Check in incognito/private window

**Reference:**
- [Template Assignment System](technical-user-guide.md#template-assignment-system)
- [Business User Guide - Template Management](business-user-guide.md#product-template-management)

---

### Template Suffix Not Saving

**Symptoms:**
- Template suffix dropdown shows but selection doesn't save
- Page reverts to default template after saving

**Solution:**

1. **Check Permissions:**
   - Verify user has edit permissions for products/collections/pages
   - Check Shopify account permissions

2. **Try Different Browser:**
   - Clear browser cache and cookies
   - Try different browser or incognito mode

3. **Verify Template File:**
   - Template file must exist in theme for suffix to appear in dropdown
   - If template file was deleted, suffix won't appear

4. **Check Theme Status:**
   - Ensure theme is published (not just saved)
   - Verify you're editing in the correct theme

---

## Team Store Issues

### Team Store Not Accessible

**Symptoms:**
- Team store page shows 404 or access denied
- Opportunity number parameter doesn't work
- Customer can't see team store products

**Solution:**

1. **Verify Collection Template Suffix:**
   ```
   Collection settings → Search engine listing → Template suffix
   Should be: `team-store-native` or `team-store-landing`
   ```

2. **Check Collection Metafields:**
   - `custom.start_date` - Store open date
   - `custom.end_date` - Store close date
   - `custom.team_product_data` - Team product configuration
   - Verify dates are set correctly (not in past for closed stores)

3. **Verify Customer Access:**
   - Check customer location metafield: `custom.opportunity_number`
   - Verify opportunity number matches collection configuration
   - Check URL parameter: `?opportunity_number={number}`

4. **Check Product Metafields:**
   - Products must have `custom.team_gear_product = true`
   - Blank products need `custom.is_custom_team_blank = true`
   - Verify `custom.parent_sku` is set correctly

**Reference:**
- [Team Store Setup](technical-user-guide.md#team-stores)
- [Business User Guide - Team Stores](business-user-guide.md#team-stores-b2b)

---

### Team Store Products Not Displaying

**Symptoms:**
- Team store page loads but no products show
- Product cards missing or broken
- Pricing not displaying correctly

**Solution:**

1. **Check Product Metafields:**
   ```liquid
   custom.team_gear_product = true (required)
   custom.is_custom_team_blank = true (for blank products)
   custom.parent_sku = "{sku_prefix}{base_sku}" (format must match)
   ```

2. **Verify Collection Assignment:**
   - Products must be added to team store collection
   - Collection template suffix must be `team-store-native` or `team-store-landing`

3. **Check Metaobject:**
   - `art_id` metaobject must exist with handle: `{parent_sku}_{opportunity_number}`
   - Verify metaobject has required fields populated
   - Check `include_default_images` field if images missing

4. **Pricing Issues:**
   - Verify `tier_pricing` JSON structure in metaobject
   - Check customer `price_level` matches tier pricing keys
   - Ensure `price_override` is empty if tier pricing should apply

**Reference:**
- [Data Guide - Team Store Metafields](data-guide.md#team-store-metafields)
- [Data Guide - Common Issues](data-guide.md#common-issues)

---

### Team Store Images Not Loading

**Symptoms:**
- Product images show broken/placeholder
- Custom team images not displaying
- Image naming errors in console

**Solution:**

1. **Verify Image Naming:**
   - Format: `{sku_prefix}{opportunity_number}_{base_sku}__P{1-3}.webp`
   - Example: `RUDIS12345_67890_RUDIS90123__P1.webp`
   - Images must be in `/cdn/shop/files/` directory

2. **Check Metaobject Settings:**
   - `include_default_images` field controls default image display
   - Verify `custom_images` field references correct image paths

3. **Verify Product Image Index:**
   - Default images: `data-image-index` values 10-19 (model shots), 30-39 (detail shots)
   - Custom images: Use `__P1`, `__P2`, `__P3` suffix

4. **Check Browser Console:**
   - Look for 404 errors on image URLs
   - Verify image paths are correct
   - Check network tab for failed requests

**Reference:**
- [Technical User Guide - Team Store Images](technical-user-guide.md#team-store-images)

---

## Metafield Issues

### Metafield Not Saving

**Symptoms:**
- Metafield value disappears after saving
- Metafield doesn't appear in admin
- Wrong value displays on frontend

**Solution:**

1. **Check Metafield Definition:**
   - Verify metafield exists in Shopify Admin: **Settings → Custom Data**
   - Check namespace and key match exactly (case-sensitive)
   - Verify metafield type matches (text, number, JSON, etc.)

2. **Verify Value Format:**
   - JSON metafields must be valid JSON
   - Number metafields must be numeric only
   - Date metafields must be in correct format

3. **Check Permissions:**
   - Verify user has edit permissions
   - Check if metafield is locked/read-only

4. **Clear Cache:**
   - Save changes and wait 1-2 minutes
   - Hard refresh browser
   - Check in different browser/incognito

**Reference:**
- [Data Guide - Metafield Reference](data-guide.md)

---

### Metafield Not Displaying on Frontend

**Symptoms:**
- Metafield saved but doesn't show on site
- Liquid code shows empty value
- Conditional logic not working

**Solution:**

1. **Verify Liquid Syntax:**
   ```liquid
   {% comment %} Correct syntax {% endcomment %}
   {{ product.metafields.custom.field_name.value }}
   
   {% comment %} Check for null/blank {% endcomment %}
   {% if product.metafields.custom.field_name.value != blank %}
   ```

2. **Check Metafield Scope:**
   - Product metafields: `product.metafields`
   - Collection metafields: `collection.metafields`
   - Customer metafields: `customer.metafields`
   - Ensure correct scope is used

3. **Verify Value Exists:**
   - Check Shopify Admin to confirm value is saved
   - Use `{% debug %}` to inspect available metafields
   - Check browser console for Liquid errors

4. **Check Theme Code:**
   - Verify metafield is referenced in correct section/snippet
   - Check if conditional logic is blocking display
   - Look for typos in metafield namespace/key

**Reference:**
- [Technical User Guide - Metafield Usage](technical-user-guide.md#data-reference)

---

## Image Issues

### Animated Hero Images Not Displaying

**Symptoms:**
- Animated Hero section shows empty/broken
- Images don't animate on scroll
- Filename prefix not working

**Solution:**

1. **Verify Image Naming:**
   - Format: `{filename_prefix}__{number}.{extension}`
   - Example: `hero-2024__0.jpg`, `hero-2024__1.jpg`
   - Must be sequential: `__0`, `__1`, `__2`, etc.

2. **Check Section Settings:**
   - `filename_prefix` must match image file names (without `__` and number)
   - `number_of_images` must match actual number of images
   - Verify images are uploaded to `/cdn/shop/files/`

3. **Verify Image Path:**
   - Full path: `https://www.rudis.com/cdn/shop/files/{filename_prefix}__{number}.jpg`
   - Check image URLs in browser network tab
   - Verify images are published/accessible

4. **Check Browser Console:**
   - Look for JavaScript errors
   - Verify animation script is loading
   - Check for 404 errors on image requests

**Reference:**
- [Technical User Guide - Animated Hero](technical-user-guide.md#animated-hero)
- [Business User Guide - Animated Hero](business-user-guide.md#animated-hero)

---

### Product Images Not Loading

**Symptoms:**
- Product images show broken/placeholder
- Images missing on product pages
- Wrong images displaying

**Solution:**

1. **Check Image Upload:**
   - Verify images uploaded to Shopify Admin
   - Check image file size (should be optimized)
   - Ensure images are published (not draft)

2. **Verify Image Alt Text:**
   - Check if alt text is set (accessibility requirement)
   - Missing alt text may cause display issues

3. **Check Product Settings:**
   - Verify featured image is set
   - Check variant images are assigned correctly
   - Ensure product is published

4. **Theme Code Issues:**
   - Check if custom image logic is interfering
   - Verify `data-image-index` values are correct
   - Look for JavaScript errors in console

**Reference:**
- [Image Specifications](technical-user-guide.md#image-specifications)
- [Business User Guide - Media Assets](business-user-guide.md#media-asset-specifications)

---

## Performance Issues

### Slow Page Load Times

**Symptoms:**
- Pages take long to load
- Core Web Vitals failing
- Poor user experience

**Solution:**

1. **Check Core Web Vitals:**
   - LCP (Largest Contentful Paint): Target < 2.5s
   - CLS (Cumulative Layout Shift): Target < 0.10
   - INP (Interaction to Next Paint): Target < 200ms
   - Use Chrome DevTools → Lighthouse

2. **Optimize Images:**
   - Convert to WebP/AVIF format
   - Use responsive image sizes
   - Implement lazy loading
   - Preload LCP image

3. **Reduce JavaScript:**
   - Defer non-critical scripts
   - Remove unused third-party scripts
   - Minimize bundle size

4. **Check Third-Party Apps:**
   - Review app performance impact
   - Disable unused apps
   - Optimize app loading strategy

**Reference:**
- [Performance Documentation](performance.md)
- [Quick Reference - Performance](QUICK_REFERENCE.md#key-metrics)

---

### High Cumulative Layout Shift (CLS)

**Symptoms:**
- Page elements shift during load
- Layout instability
- Poor user experience

**Solution:**

1. **Reserve Layout Space:**
   - Set explicit dimensions for images
   - Use aspect-ratio CSS property
   - Reserve space for dynamic content

2. **Fix Dynamic Content:**
   - Reserve space for product grids
   - Use skeleton loaders
   - Preload critical content

3. **Optimize Fonts:**
   - Preload critical fonts
   - Use font-display: swap
   - Avoid invisible text during font load

4. **Check SearchSpring:**
   - SearchSpring collections may cause CLS
   - Reserve minimum height for search results
   - Use loading skeletons

**Reference:**
- [Performance Documentation - CLS](performance.md#cumulative-layout-shift-cls)

---

## Integration Issues

### SearchSpring Not Working

**Symptoms:**
- SearchSpring search not functioning
- Filters not applying
- Results not displaying

**Solution:**

1. **Verify App Installation:**
   - Check SearchSpring app is installed
   - Verify app is active/enabled
   - Check app subscription status

2. **Check Collection Template:**
   - Collection must have template suffix: `searchspring`
   - Template file: `templates/collection.searchspring.json`
   - Verify section: `main-collection-product-grid-ss`

3. **Verify JavaScript:**
   - Check `searchspring.bundle.js` is loading
   - Look for JavaScript errors in console
   - Verify script snippet is included

4. **Check Configuration:**
   - Verify SearchSpring dashboard settings
   - Check collection is configured in SearchSpring
   - Verify API credentials

**Reference:**
- [Integrations - SearchSpring](integrations.md#searchspring)
- [Technical User Guide - SearchSpring](technical-user-guide.md#searchspring)

---

### Klaviyo Not Sending Emails

**Symptoms:**
- Back-in-stock notifications not sending
- Email capture not working
- Klaviyo events not firing

**Solution:**

1. **Verify Klaviyo ID:**
   - Check theme settings: `settings.klaviyo_id`
   - Verify Klaviyo Public Key is correct
   - Check if script is loading: `https://static.klaviyo.com/onsite/js/klaviyo.js`

2. **Check Product Settings:**
   - Verify `custom.coming_soon` metafield (should be null or false)
   - Check variant availability
   - Ensure "Notify Me" button is visible

3. **Check JavaScript:**
   - Look for Klaviyo errors in console
   - Verify `klaviyo-bis-trigger` button exists
   - Check modal is rendering correctly

4. **Verify Klaviyo Dashboard:**
   - Check flow is active
   - Verify customer is subscribed
   - Check email delivery status

**Reference:**
- [Integrations - Klaviyo](integrations.md#klaviyo-email-marketing--sms)

---

### Elevar Tracking Not Working

**Symptoms:**
- Analytics events not firing
- Data layer empty
- GTM not receiving data

**Solution:**

1. **Verify Elevar Snippets:**
   - Check snippets are included: `elevar-head.liquid`, `elevar-body-end.liquid`
   - Verify GTM container ID: `GTM-TQVF78L9`
   - Check script is loading

2. **Check Browser Console:**
   - Look for Elevar errors
   - Verify `dataLayer` exists
   - Check event configuration

3. **Verify Event Configuration:**
   - Check `event_config` in Elevar settings
   - Ensure events are enabled
   - Verify tracking is active

4. **Check Locksmith Integration:**
   - Locksmith may exclude products from tracking
   - Verify product access is not restricted
   - Check `locksmith-variables` snippet

**Reference:**
- [Integrations - Elevar](integrations.md#elevar-conversion-tracking)

---

## Content Issues

### Section Not Showing in Customizer

**Symptoms:**
- Section not available in theme customizer
- Can't add section to page
- Section settings missing

**Solution:**

1. **Check Template:**
   - Verify section is included in template JSON
   - Check template file exists
   - Ensure section name matches

2. **Verify Section File:**
   - Section file must exist: `sections/{section-name}.liquid`
   - Check section schema is defined
   - Verify section is enabled

3. **Check Section Schema:**
   - Verify `settings_schema` is defined
   - Check block types are configured
   - Ensure section is not deprecated

4. **Clear Cache:**
   - Save theme changes
   - Refresh customizer
   - Try different browser

**Reference:**
- [Technical User Guide - Customizer Sections](technical-user-guide.md#customizer-sections)

---

### Content Not Updating

**Symptoms:**
- Changes saved but not showing on site
- Content appears outdated
- Cache not clearing

**Solution:**

1. **Verify Publishing:**
   - Ensure changes are published (not just saved)
   - Check draft status
   - Verify theme is published

2. **Clear Browser Cache:**
   - Hard refresh: Cmd/Ctrl + Shift + R
   - Clear browser cache
   - Try incognito/private window

3. **Check CDN Cache:**
   - Shopify CDN may cache content
   - Wait 5-10 minutes for cache to clear
   - Check if changes appear in different region

4. **Verify Template:**
   - Ensure correct template is assigned
   - Check if conditional logic is blocking content
   - Verify section is in template

---

## Accessibility Issues

### Missing Alt Text Warnings

**Symptoms:**
- Accessibility audit shows missing alt text
- Images lack descriptions
- Screen reader warnings

**Solution:**

1. **Add Alt Text:**
   - Navigate to image in Shopify Admin
   - Add descriptive alt text
   - Use meaningful descriptions (not "image1.jpg")

2. **Bulk Update:**
   - Use Shopify bulk editor for multiple images
   - Export/import with alt text column
   - Use apps for bulk alt text management

3. **Check Theme Code:**
   - Verify `alt` attribute is included in image tags
   - Check if alt text is being stripped
   - Ensure dynamic images have alt text

**Reference:**
- [Accessibility Documentation](accessibility.md)
- [Accessibility Remediation](accessibility.md#remediation-guide)

---

### Keyboard Navigation Issues

**Symptoms:**
- Can't navigate with keyboard
- Focus traps
- Tab order incorrect

**Solution:**

1. **Check Focus Management:**
   - Verify all interactive elements are keyboard accessible
   - Check for `tabindex` attributes
   - Ensure focus is visible

2. **Fix Focus Traps:**
   - Check modal/dialog focus management
   - Verify escape key closes modals
   - Ensure focus returns to trigger after closing

3. **Test Navigation:**
   - Use Tab key to navigate
   - Check Shift+Tab for reverse navigation
   - Verify Enter/Space activates buttons

**Reference:**
- [Accessibility Documentation - Operable](accessibility.md#operable-violations)

---

## General Troubleshooting Tips

### Always Check First

1. **Browser Console:**
   - Open DevTools (F12)
   - Check Console tab for errors
   - Look for JavaScript errors
   - Check Network tab for failed requests

2. **Shopify Admin:**
   - Verify settings are saved
   - Check product/collection is published
   - Ensure correct template is assigned
   - Verify metafields are set

3. **Theme Code:**
   - Check code references in documentation
   - Verify file paths are correct
   - Check for typos in Liquid syntax
   - Ensure conditional logic is correct

4. **Cache:**
   - Clear browser cache
   - Wait for CDN cache to clear
   - Try different browser/device
   - Check in incognito mode

### When to Escalate

- **Theme Code Errors:** If issue requires code changes, escalate to developer
- **Third-Party App Issues:** Contact app support directly
- **Shopify Platform Issues:** Contact Shopify Plus support
- **Complex Integration Problems:** Escalate to technical team

---

## Additional Resources

- [Technical User Guide](technical-user-guide.md) - Complete technical documentation
- [Business User Guide](business-user-guide.md) - Content management workflows
- [Data Guide](data-guide.md) - Complete metafield reference
- [Integrations Guide](integrations.md) - Third-party app documentation
- [Performance Guide](performance.md) - Performance optimization
- [Quick Reference](QUICK_REFERENCE.md) - Quick lookup guide

---

**Last Updated:** October 31, 2025  
**For Support:** See [README](README.md) for contact information

