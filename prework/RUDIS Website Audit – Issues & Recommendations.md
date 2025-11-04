# RUDIS Website Audit – Issues & Recommendations

This handoff document summarizes the performance and accessibility issues identified during the audit of **RUDIS.com** (homepage, “Faith Over Fear” collection page and “Faith Over Fear T‑Shirt” product page). Each issue includes a short description, technical details to assist developers in remediation and a recommended priority.

## Issues & Recommendations

### 1. Optimize Hero & Banner Images
- **Description:** The homepage hero banner (and other large promotional images) is extremely large (~2800 px wide) and not optimized. This results in a Largest Contentful Paint (LCP) around 3.6 s on mobile, causing the Core Web Vitals assessment to fail.
- **Technical Details:**
  - Compress hero and banner images using WebP or AVIF formats.
  - Resize images to serve device‑appropriate dimensions.
  - Implement `loading="lazy"` on non‑critical images and explicitly preload the LCP image using `<link rel="preload" as="image" href="...">`.
  - Consider using a responsive `<picture>` element with multiple sources for different viewport sizes.
- **Priority:** **Do now** – improving LCP will directly impact user‑perceived performance and SEO.

### 2. Missing Descriptive Alt Text
- **Description:** Across the site, many images (hero banners, category thumbnails, product images) use empty `alt=""` attributes. This fails WCAG 2.2 AA requirements for non‑text content and harms screen‑reader accessibility.
- **Technical Details:**
  - For each image conveying content (e.g., “KOLAT wrestling shoes” banner, product photos), provide meaningful `alt` text describing the product or message.
  - For purely decorative images, keep `alt=""` but ensure they are truly decorative.
  - In a templating environment, map `alt` tags to product names and color variants automatically.
- **Priority:** **Do now** – essential for accessibility and SEO.

### 3. Deep & Overloaded Navigation
- **Description:** The mega‑menu contains numerous categories and sub‑links, leading to cognitive overload and potential keyboard navigation difficulties.
- **Technical Details:**
  - Reduce the number of top‑level links displayed by collapsing secondary categories behind progressive disclosure (e.g., “More categories…”).
  - Ensure each menu item is reachable via `Tab` key; add `role="menu"`, `role="menuitem"` and appropriate ARIA attributes.
  - Implement skip‑links and visible focus outlines for keyboard users.
- **Priority:** **Do next** – improves usability and accessibility but is secondary to major performance fixes.

### 4. Cookie Banner Accessibility
- **Description:** The cookie consent banner appears on initial load. It may not be fully keyboard‑accessible (focus may not move into the banner) and lacks explicit labels.
- **Technical Details:**
  - Ensure that when the banner is visible, it traps focus until the user makes a choice; use `aria-modal="true"` on the dialog container.
  - Add `aria-label` or text to the accept/decline buttons (e.g., “Accept cookies”).
  - Allow dismissal with the `Esc` key and ensure focus returns to the triggering element after dismissal.
- **Priority:** **Do next** – required for compliance with accessibility laws.

### 5. Sorting & Filter Controls on Collection Page
- **Description:** The “Sort” and “Filter” dropdowns on the collection page have minimal ARIA support and may not announce state changes to screen readers.
- **Technical Details:**
  - Use semantic `<button>` and `<select>` elements or add `role="button"`, `aria-haspopup="listbox"` and `aria-expanded` attributes.
  - When the dropdown is open, set focus to the first option and allow navigation via arrow keys.
  - Provide labels (e.g., “Sort products”).
- **Priority:** **Do next** – necessary for accessible ecommerce navigation.

### 6. Semantic Heading Structure
- **Description:** Some pages reuse generic `<div>` elements for headings; the collection name is not an `<h1>` and product sections lack proper heading levels.
- **Technical Details:**
  - Use `<h1>` for the main page title (e.g., “Faith Over Fear” collection).
  - Use subsequent headings (`<h2>`, `<h3>`, etc.) to denote sections such as “Products,” “Product Overview,” and “Reviews.”
  - Screen‑reader users rely on heading navigation; correct structure greatly improves usability.
- **Priority:** **Do later** – improves accessibility but doesn’t block usage.

### 7. Accessible Size & Option Selectors on Product Page
- **Description:** Size buttons (XS, SM, MD, etc.) and the “Add to cart” button lack explicit ARIA roles/states and focus styles.
- **Technical Details:**
  - For size selection, use `<button>` with `aria-pressed` to indicate selection state.
  - Ensure each button has a discernible label (e.g., “Size XS”).
  - Provide a visible focus outline using CSS (e.g., `:focus-visible` pseudo‑class).
  - For “Add to cart,” use `aria-label="Add Faith Over Fear T‑Shirt to cart"` to describe action.
- **Priority:** **Do next** – essential for accessible purchasing flows.

### 8. Product Overview Accordion Accessibility
- **Description:** The product page’s “Product Overview” collapsible panel may not indicate its expanded/collapsed state to assistive technologies.
- **Technical Details:**
  - Use `<button>` for the accordion header with `aria-expanded="true/false"` and `aria-controls` linking to the panel content `id`.
  - Provide keyboard interaction (Enter/Space toggles the panel).
  - Ensure the panel content is announced when expanded and hidden from the accessibility tree when collapsed (`hidden` attribute).
- **Priority:** **Do later** – valuable but lower priority compared to more critical issues.

### 9. Maintain Current Optimization of Collection & Product Pages
- **Description:** The collection and product pages currently pass Core Web Vitals, with LCP ≤ 2.1 s and CLS = 0. This is a strength to maintain.
- **Technical Details:**
  - Continue to compress and lazy‑load images.
  - Preload the LCP image (main product image) and critical CSS.
  - Monitor performance with tools like Lighthouse or real‑user monitoring to catch regressions.
- **Priority:** **Don’t do (no action)** – just monitor; no change needed now.

## Priority Summary
- **Do now:** Optimize hero images; add meaningful alt text.
- **Do next:** Improve navigation accessibility; fix cookie banner; make sort/filter controls accessible; fix size selectors; improve add‑to‑cart and interactive controls.
- **Do later:** Enhance semantic headings; refine accordion ARIA support.
- **Don’t do:** Changes that could compromise current good performance on collection/product pages; instead maintain and monitor.

---

This document should give developers clear, actionable steps to enhance RUDIS’s site performance and accessibility.
