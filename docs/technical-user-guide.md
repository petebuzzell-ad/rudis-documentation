# RUDIS Platform Documentation - Technical User Guide

**Last Updated:** October 31, 2025  
**Theme:** CQL Propel v3.0.0  
**Base:** Dawn OS 2.0 (Customized)

---

## Table of Contents

1. [Template Assignment System](#template-assignment-system)
2. [Page Types & Templates](#page-types--templates)
3. [Customizer Sections](#customizer-sections)
   - [Content Sections](#content-sections)
   - [Product Sections](#product-sections)
   - [Collection Sections](#collection-sections)
   - [Media Sections](#media-sections)
   - [Navigation Sections](#navigation-sections)
3. [Image Specifications](#image-specifications)
4. [Custom Features](#custom-features)
   - [Team Store Functionality](#team-store-functionality) *(See [Team Store/B2B Documentation](team-store-b2b.md) for complete system documentation)*
5. [Template Variants](#template-variants)
6. [Data Reference](#data-reference)

---

## Template Assignment System

### Understanding Template Suffixes

In Shopify, templates are assigned using **template suffixes** - a system where template files follow the naming pattern `{template-type}.{suffix}.json`. The suffix determines which template file is used for a specific product, collection, or page.

### How Template Suffixes Work

**Template File Naming:**
- Standard template: `product.json` (no suffix)
- Template with suffix: `product.team-store-pdp.json` (suffix: `team-store-pdp`)
- Collection template: `collection.searchspring.json` (suffix: `searchspring`)

**Assignment Process:**
1. **Manual Assignment:** Template suffixes are set manually in Shopify Admin:
   - Products: Product settings → **Template suffix** dropdown
   - Collections: Collection settings → **Template suffix** dropdown
   - Pages: Page settings → **Template suffix** dropdown

2. **Theme-Level Detection:** Theme code can conditionally render different layouts based on metafields or other conditions, but this does **not** change the template file used. It only affects how the template renders.

### Template Assignment vs Layout Conditionals

**Important Distinction:**
- **Template Suffix:** Determines which `.json` template file is used (set in Shopify Admin)
- **Layout Conditionals:** Theme code (`layout/theme.liquid`) can conditionally render different layouts based on metafields

**Example - Team Store Products:**
```17:17:layout/theme.liquid
    {% if collection.template_suffix == 'team-store-landing' or product.metafields.custom.is_custom_team_blank %}
```

This code:
- Checks if collection has `team-store-landing` template suffix **OR**
- Checks if product has `is_custom_team_blank` metafield
- If either condition is true, theme applies special layout (e.g., noindex robots tag)

**However:** The product still needs `product.team-store-pdp.json` template suffix set manually in Shopify Admin to use the correct template file.

### Automatic vs Manual Assignment

**Reality:** Shopify does **not** automatically assign template suffixes based on product type or metafields. All template suffix assignments are **manual** in Shopify Admin.

**What Appears "Automatic":**
1. **Team Store Products:** Theme code checks `is_custom_team_blank` metafield to conditionally render layout, but template suffix `product.team-store-pdp.json` must still be set manually
2. **Shoe Products:** No automatic assignment exists - `product.shoe-product.json` template suffix must be set manually
3. **Bundle Products:** No automatic assignment exists - `product.bundles.json` template suffix must be set manually

**Best Practice:**
- Set template suffix in Shopify Admin when creating/editing products, collections, or pages
- Use metafields to trigger conditional layout logic, not template assignment
- Document template suffix requirements for each product type

### Setting Template Suffixes

**In Shopify Admin:**

1. **For Products:**
   - Navigate to **Products** → Select product
   - Scroll to **Search engine listing** section
   - Find **Template suffix** dropdown
   - Select desired template (e.g., `team-store-pdp`, `shoe-product`)
   - Save

2. **For Collections:**
   - Navigate to **Products** → **Collections** → Select collection
   - Scroll to **Search engine listing** section
   - Find **Template suffix** dropdown
   - Select desired template (e.g., `team-store-native`, `searchspring`)
   - Save

3. **For Pages:**
   - Navigate to **Online Store** → **Pages** → Select page
   - Scroll to **Search engine listing** section
   - Find **Template suffix** dropdown
   - Select desired template (e.g., `yotpo-rewards`, `technique-library`)
   - Save

### Template Suffix Reference

**Product Templates:**
- `product.json` - Default (no suffix)
- `product.team-store-pdp.json` - Team store products
- `product.shoe-product.json` - Shoe products
- `product.bundles.json` - Bundle products
- `product.auction-pro-template.json` - Auction products
- See [Template Variants](#template-variants) for complete list

**Collection Templates:**
- `collection.json` - Default (no suffix)
- `collection.team-store-native.json` - Native team store
- `collection.team-store-landing.json` - Team store landing page
- `collection.searchspring.json` - SearchSpring-powered collections

**Page Templates:**
- `page.json` - Default (no suffix)
- `page.yotpo-rewards.json` - Yotpo rewards page
- `page.technique-library.json` - Technique library pages
- See [Page Templates](#page-templates) section for complete list

---

## Page Types & Templates

### Product Pages

#### Standard Product Template (`product.json`)
- **Usage:** Default product template for most products
- **Template Sections:** Uses `main-product.liquid`
- **Key Features:**
  - Standard product media gallery
  - Variant selection
  - Add to cart functionality
  - Product information blocks

#### Specialized Product Templates

**Shoe Products (`product.shoe-product.json`)**
- **Usage:** Wrestling shoes and footwear
- **Template:** `main-product-shoe.liquid`
- **Special Features:**
  - Shoe-specific sizing information
  - Shoe-specific product features
  - Specialized media gallery for footwear

**Team Store Products (`product.team-store-pdp.json`)**
- **Usage:** Team store custom products
- **Template:** `main-product-team-store.liquid`
- **Special Features:**
  - Team store customization options
  - Personalization fields (name, number)
  - Team store approval workflow
  - Custom image gallery management

**Bundle Products (`product.bundles.json`)**
- **Usage:** Product bundles and sets
- **Template:** `main-product-bundles.liquid`
- **Special Features:**
  - Bundle component selection
  - Bundle pricing display
  - Bundle-specific add to cart

**Auction Products (`product.auction-pro-template.json`)**
- **Usage:** Auction and special event products
- **Template:** `main-product-auction.liquid`
- **Special Features:**
  - Auction countdown timers
  - Bid functionality
  - Auction-specific pricing

**Athlete Brand Templates**
- `product.kolat.json` - Kolat brand products
- `product.rocky.json` - Rocky brand products
- `product.hildebrandt.json` - Hildebrandt products
- `product.jb-ultra-ps.json` - Jordan Burroughs Ultra products
- `product.jb-ultralite.json` - Jordan Burroughs Ultralite products

### Collection Pages

#### Standard Collection (`collection.json`)
- **Usage:** Default collection listing page
- **Template:** `main-collection-product-grid.liquid`
- **Features:**
  - Product grid display
  - Filtering and sorting
  - Pagination
  - Product count display

#### SearchSpring Collection (`collection.searchspring.json`)
- **Usage:** Collections using SearchSpring search/filter
- **Template Suffix:** `searchspring` (creates `collection.searchspring.json` template)
- **Template Section:** `main-collection-product-grid-ss.liquid`
- **Features:**
  - SearchSpring-powered search and filtering
  - Advanced filtering with SearchSpring widgets
  - SearchSpring recommendations
  - IntelliSuggest autocomplete integration
- **Configuration:**
  - Set collection template suffix to `searchspring` in Shopify Admin
  - SearchSpring app must be installed and configured
  - Collection uses `main-collection-product-grid-ss` section instead of standard grid
- **Code References:**
  - Template: `templates/collection.searchspring.json`
  - Section: `sections/main-collection-product-grid-ss.liquid`
  - JavaScript: `assets/searchspring.bundle.js`
  - Script Snippet: `snippets/searchspring-script.liquid`
  - Recommendations: `sections/searchspring-recommendations.liquid`
- **See Also:** [Integrations Guide - SearchSpring](integrations.md#searchspring) for detailed integration documentation

#### Team Store Collection (`collection.team-store-native.json`)
- **Usage:** Team store collection pages
- **Template:** `main-collection-team-store.liquid`
- **Features:**
  - Team store status messages
  - Team store approval workflow
  - Custom team store product display

### Page Templates

#### Standard Page (`page.json`)
- **Usage:** General content pages
- **Template:** `main-page.liquid`
- **Available Sections:** All content sections

#### Specialized Page Templates

**Yotpo Rewards Page (`page.yotpo-rewards.json`)**
- **Usage:** Yotpo loyalty rewards page
- **Template:** `main-page-yotpo-rewards.liquid`

**Digioh Results (`page.digioh-results.liquid`)**
- **Usage:** Digioh integration results page
- **Template:** Liquid template (not JSON)

**Style Guide (`page.styleguide.liquid`)**
- **Usage:** Design system and style guide
- **Template:** `main-page-styleguide.liquid`

**Technique Library Pages**
- `page.technique-library.json` - General technique library
- `page.technique-library-kennedy.json` - Kennedy Blades techniques
- `page.technique-library-kolat.json` - Cary Kolat techniques

**Athlete Pages**
- `page.spencer.json` - Spencer Lee athlete page
- `page.kolat.json` - Kolat athlete page

**Signup Forms**
- `page.signup-form.json`
- `page.signup-form-02.json`
- `page.signup-form-3.json`

---

## Customizer Sections

### Content Sections

#### Image Banner (`image-banner.liquid`)

**Purpose:** Full-width banner with background image and overlaid content

**Settings:**

**Images:**
- **Desktop Image:** 
  - Recommended: 1920px × 1080px (16:9 ratio)
  - Format: JPG, PNG, WebP
  - Max file size: 500KB recommended
- **Desktop Large Image (Wide Screens):**
  - Recommended: 2560px × 1440px (16:9 ratio)
  - For screens wider than 1650px
- **Mobile Image:**
  - Recommended: 750px × 1334px (9:16 portrait ratio)
  - Format: JPG, PNG, WebP

**Desktop Layout:**
- **Content Position:** Top Left, Top Center, Top Right, Middle Left, Middle Center, Middle Right, Bottom Left, Bottom Center, Bottom Right
- **Content Alignment:** Left, Center, Right
- **Desktop Max Height:** Number (px), default 640px
- **Content Area Max Width:** Number (px), default 400px

**Mobile Layout:**
- **Content Position:** Below image or overlaid
- **Content Alignment:** Left, Center, Right
- **Show Content Below Image:** Checkbox (default: true)
- **Hide Image on Mobile:** Checkbox

**Colors:**
- **Section Background Color:** Color picker
- **Content Container Color:** Color picker
- **Container Border Color:** Color picker (default: #333333)
- **Content Background Opacity:** Range 0-100% (default: 100%)

**Border Options:**
- **Show Container Border on Desktop:** Checkbox
- **Show Container Border on Mobile:** Checkbox
- **Offset Container Border on Desktop:** Checkbox
- **Offset Container Border on Mobile:** Checkbox

**Content Container:**
- **Show Container Background on Desktop:** Checkbox (default: false)
- **Show Container Background on Mobile:** Checkbox (default: false)

**Other Options:**
- **Section Link:** URL (makes entire section clickable)
- **Hide Section on Mobile:** Checkbox
- **Hide in Canada:** Checkbox (localization)

**Blocks:**

1. **Eyebrow Block** (Limit: 1)
   - Text: Text input
   - Style: Eyebrow - Small, Eyebrow - Large
   - Colors: Desktop color, Mobile color

2. **Headline Block** (Limit: 1)
   - Headline: Text input
   - Size: Small (h3), Medium (h2), Large (h1)
   - Colors: Desktop color, Mobile color
   - **XL Headline Override:**
     - Activate Desktop Override: Checkbox
     - Custom Size: 50-200px (default: 50px)
     - Activate Mobile Override: Checkbox
     - Custom Mobile Size: 16-100px (default: 16px)

3. **Description Block** (Limit: 1)
   - Description: Rich text editor
   - Text Style: Body (Default), Body - Small, Body - Medium, Body - Large, Caption, Subtitle
   - Colors: Desktop color, Mobile color

4. **Buttons Block** (Limit: 1)
   - **Button 1:**
     - Label: Text input
     - Link: URL
     - Style Desktop: Primary, Secondary, Secondary Transparent
     - Style Mobile: Primary, Secondary, Secondary Transparent
     - Colors: Foreground, Background, Border, Hover Border
   - **Button 2:** (Same options as Button 1)
   - **Display Options:**
     - Display side-by-side: Checkbox
     - Button widths: Inherit, Auto, 100%
     - Display vertical separator: Checkbox
     - Display horizontal separator: Checkbox
     - Separator color: Color picker
     - Override link/button default text color: Checkbox
     - Link color: Color picker

5. **Image Block** (Limit: 1)
   - Image: Image picker
   - Maximum Size: Number (px), default 75px

**Animations:**
- **Select Animation:** Fade In, Fade In Up, Fade In Left, Fade In Right, No Effect
- **Animation Time:** Text (e.g., "0.2s")

---

#### Rich Text (`rich-text.liquid`)

**Purpose:** Flexible text content section with multiple content blocks

**Settings:**

**Background:**
- **Background Color:** Color picker
- **Desktop Background Image:** Image picker
- **Mobile Background Image:** Image picker

**Section Padding:**
- **Desktop Top Padding:** Number (px), default 60px
- **Desktop Bottom Padding:** Number (px), default 60px
- **Mobile Top Padding:** Number (px), default 45px
- **Mobile Bottom Padding:** Number (px), default 45px
- **Disable Section Top Margin:** Checkbox

**Blocks:**

1. **Headline Block** (Limit: 1)
   - **Headline Animation:** Fade In, Fade In Up, Fade In Left, Fade In Right, No Effect
   - **Animation Time:** Text (default: "0.2s")
   - **Headline:** Text input
   - **Headline Color:** Color picker (default: #000000)
   - **Headline Size:** 
     - Headline Feature XL
     - Headline Feature Large
     - Headline Feature
     - Headline Small
     - Headline XS
     - Headline XS Regular
     - Custom Headline 1, 2, 3
     - X-Small (h4), Small (h3), Medium (h2), Large (h1), X-Large (h0)
   - **XL Headline Override:**
     - Activate Desktop: Checkbox
     - Custom Size: 50-200px (default: 50px)
     - Activate Mobile: Checkbox
     - Custom Mobile Size: 16-120px (default: 16px)

2. **Description Block** (Limit: 1)
   - **RichText Animation:** Fade In, Fade In Up, Fade In Left, Fade In Right, No Effect
   - **Animation Time:** Text (default: "0.2s")
   - **Description:** Rich text editor
   - **Text Color:** Color picker (default: #000000)
   - **Text Style:**
     - Paragraph Feature
     - Paragraph Interface
     - Paragraph Eyebrow
     - Paragraph Small
     - Caption
     - Subtitle
     - Body - Default
     - Body - Small
     - Body - Medium
     - Body - Large

3. **Button Block** (Limit: 2)
   - **Button Animation:** Fade In, Fade In Up, Fade In Left, Fade In Right, No Effect
   - **Animation Time:** Text (default: "0.2s")
   - **Button Label:** Text input
   - **Button Link:** URL
   - **Button Style:**
     - Primary
     - Secondary
     - Secondary Transparent
     - Secondary Alternate
     - Secondary Red
     - Secondary Gold
     - Link style 0, 1, 2

4. **Logo List Block** (Limit: 2)
   - **Logo Animation:** Fade In, Fade In Up, Fade In Left, Fade In Right, No Effect
   - **Animation Time:** Text (default: "0.2s")
   - **Logo Items:** Up to 5 logos per block
     - Logo Image: Image picker (max 300px width recommended)
     - Logo Link: URL

5. **Padding Block** (Unlimited)
   - **Mobile Padding:** Number (px)
   - **Desktop Padding:** Number (px)

---

#### Collapsible Content (`collapsible-content.liquid`)

**Purpose:** Accordion-style expandable content sections

**Settings:**

**Content:**
- **Caption:** Text input (optional)
- **Heading:** Inline rich text
- **Heading Size:** Small (h2), Medium (h1), X-Large (h0)
- **Heading Alignment:** Left, Center, Right (default: center)

**Layout:**
- **Layout:** None, Row, Section
- **Desktop Layout:** Image First, Image Second
- **Color Scheme:** accent-1, accent-2, background-1, background-2, inverse
- **Container Color Scheme:** accent-1, accent-2, background-1, background-2, inverse
- **Open First Collapsible Row:** Checkbox

**Image:**
- **Image:** Image picker
- **Image Ratio:** Adapt, Small, Large

**Section Padding:**
- **Padding Top:** 0-100px (default: 36px)
- **Padding Bottom:** 0-100px (default: 36px)

**Blocks:**

**Collapsible Row Block** (Unlimited)
- **Heading:** Text input
- **Icon:** 
  - None, Apple, Banana, Bottle, Box, Carrot, Chat Bubble, Check Mark, Clipboard, Dairy, Dairy Free, Dryer, Eye, Fire, Gluten Free, Heart, Iron, Leaf, Leather, Lightning Bolt, Lipstick, Lock, Map Pin, Nut Free, Pants, Paw Print, Pepper, Perfume, Plane, Plant, Price Tag, Question Mark, Recycle, Return, Ruler, Serving Dish, Shirt, Shoe, Silhouette, Snowflake, Star, Stopwatch, Truck, Washing
- **Row Content:** Rich text editor
- **Page:** Page picker (alternative to row content)

---

#### Multi-Column (`multicolumn.liquid`)

**Purpose:** Grid of content cards with images, text, and links

**Settings:**

**Content:**
- **Title:** Inline rich text
- **Heading Size:** Small (h2), Medium (h1), X-Large (h0)
- **Button Label:** Text input
- **Button Link:** URL

**Layout:**
- **Columns Desktop:** 1-5 (default: 4)
- **Columns Mobile:** 1-2 (default: 2)
- **Column Alignment:** Center checkbox
- **Swipe on Mobile:** Checkbox (enables slider on mobile)
- **Color Scheme:** accent-1, accent-2, background-1, background-2, inverse
- **Background Style:** None, Primary, Secondary

**Images:**
- **Image Ratio:** Adapt, Portrait, Square
- **Image Width:** Full, Half, Third

**Section Padding:**
- **Padding Top:** 0-100px (default: 36px)
- **Padding Bottom:** 0-100px (default: 36px)

**Blocks:**

**Column Block** (Unlimited)
- **Image:** Image picker
  - **Recommended:** 800px × 800px (square) or 800px × 1200px (portrait)
  - **Format:** JPG, PNG, WebP
- **Title:** Inline rich text
- **Text:** Rich text editor
- **Link Label:** Text input
- **Link:** URL

---

#### Video (`video.liquid`)

**Purpose:** Video player section with YouTube/Vimeo support

**Settings:**

**Images:**
- **Desktop Cover Image:** 
  - **Ratio:** 16:9
  - **Recommended:** 1920px × 1080px
  - **Format:** JPG, PNG, WebP
- **Mobile Cover Image:**
  - **Ratio:** 16:9
  - **Recommended:** 750px × 422px
  - **Format:** JPG, PNG, WebP
- **Image Hover:** Ease In, No Effect

**Video Options:**
- **Desktop Video URL:** YouTube or Vimeo URL
- **Mobile Video URL:** YouTube or Vimeo URL
- **Video Alt Text:** Text input (for accessibility)
- **Display as Background Video:** Checkbox
  - Background videos are automatically muted for autoplay
  - Supports only YouTube videos
- **Make Section Full Width:** Checkbox
- **Autoplay Video on Page Load:** Checkbox
- **Display Video Player in Modal:** Checkbox

**Colors:**
- **Background Color:** Color picker
- **Text Color:** Color picker
- **Button Fill Color:** Color picker (default: #ffffff)
- **Overlay Color:** Color picker (only for background video)
- **Overlay Opacity:** 0-100% (default: 100%)

**Content:**

**Eyebrow:**
- **Text:** Text input
- **Style:** Eyebrow - Small, Eyebrow - Large

**Headline:**
- **Text:** Text input
- **Text Size:** 
  - Headline Feature XL, Large, Feature, Small, XS, XS Regular
  - Custom Headline 1, 2, 3
  - X-Small (h4) through X-Large (h0)

**Description:**
- **Text:** Rich text editor
- **Text Style:**
  - Paragraph Feature, Interface, Eyebrow, Small
  - Body (Default, Small, Medium, Large)
  - Caption, Subtitle

**Button:**
- **Label:** Text input (leave blank to hide)
- **Link:** URL
- **Style Desktop:** Primary, Secondary, Secondary Transparent, Secondary Alternate, Secondary Red, Secondary Gold, Link 0-2
- **Style Mobile:** Same options as desktop
- **Override Link/Button Default Text Color:** Checkbox
- **Link Color:** Color picker

**Layout (Background Video Only):**

**Desktop:**
- **Content Position:** Top Left, Top Center, Top Right, Middle Left, Middle Center, Middle Right, Bottom Left, Bottom Center, Bottom Right
- **Content Alignment:** Left, Center, Right

**Mobile:**
- **Content Position:** Top, Middle, Bottom
- **Content Alignment:** Left, Center, Right

**Section Animation:**
- **Select Animation:** Fade In, Fade In Up, No Effect
- **Animation Time:** Text (e.g., "0.2s")

**Section Padding:**
- **Desktop:** Top, Right, Bottom, Left (px) - default: 60px top/bottom, 0px left/right
- **Mobile:** Top, Right, Bottom, Left (px) - default: 30px top/bottom, 0px left/right

---

### Product Sections

#### Featured Product (`featured-product.liquid`)

**Purpose:** Display a single featured product with media gallery

**Settings:**

**Product:**
- **Product:** Product picker

**Layout:**
- **Media Size:** Small (45% width), Medium (55% width), Large (65% width)
- **Media Position:** Left, Right
- **Media Fit:** Contain, Cover
- **Constrain to Viewport:** Checkbox
- **Color Scheme:** accent-1, accent-2, background-1, background-2, inverse
- **Secondary Background:** Checkbox

**Blocks:**

Available blocks include:
- Text
- Title
- Price
- Variant Picker
- Quantity Selector
- Buy Buttons
- Description
- Share Button
- Custom Liquid
- Product Recommendations
- And more...

---

#### Featured Collection (`featured-collection.liquid`)

**Purpose:** Display a grid of products from a selected collection

**Settings:**

**Collection:**
- **Collection:** Collection picker
- **Products to Show:** 2-25 (default: 4)
- **Show View All:** Checkbox (default: true)
- **View All Style:** Link, Outline, Solid

**Layout:**
- **Columns Desktop:** 1-5 (default: 4)
- **Columns Mobile:** 1-2 (default: 2)
- **Full Width:** Checkbox
- **Enable Desktop Slider:** Checkbox
- **Swipe on Mobile:** Checkbox

**Product Cards:**
- **Image Ratio:** Adapt, Portrait, Square
- **Show Secondary Image:** Checkbox (on hover)
- **Show Vendor:** Checkbox
- **Show Rating:** Checkbox
- **Enable Quick Add:** Checkbox (add to cart from card)

**Colors:**
- **Color Scheme:** accent-1, accent-2, background-1, background-2, inverse

**Section Padding:**
- **Padding Top:** 0-100px (default: 36px)
- **Padding Bottom:** 0-100px (default: 36px)

---

### Collection Sections

#### Collection Product Grid (`main-collection-product-grid.liquid`)

**Purpose:** Main product listing for collection pages

**Settings:**

**Filtering & Sorting:**
- **Enable Filtering:** Checkbox
- **Enable Sorting:** Checkbox
- **Collapse on Larger Devices:** Checkbox
- **Custom Swatch Name:** Text input

**Display:**
- **Products Per Page:** Number (default: 24)
- **Image Ratio:** Adapt, Portrait, Square
- **Show Secondary Image:** Checkbox
- **Add Image Padding:** Checkbox
- **Show Vendor:** Checkbox
- **Show Image Outline:** Checkbox
- **Show Rating:** Checkbox
- **Show Product Labels:** Checkbox
- **Image Hover:** Effect type

**Animations:**
- **Product Grid Animation:** Animation type
- **Product Grid Time:** Animation duration

---

### Media Sections

#### Animated Hero (`animated-hero.liquid`)

**Purpose:** Scroll-based animated hero section with image sequence animation

**Settings:**

**Image Configuration:**
- **Image Filename Prefix:** Text (e.g., "GoldReveal") - Prefix for image files in `/cdn/shop/files/`
  - Images must be named: `{prefix}__0.jpg`, `{prefix}__1.jpg`, etc. (up to 50 images)
  - Section auto-detects JPG or PNG format
- **Number of Images:** Number (0-50) - Total number of images in sequence
- **Frame Step Value:** Number (default: 30) - Pixels per scroll until next image (lower = faster animation)
- **Enable Loading Animation:** Checkbox - Shows loading animation until images are ready

**Colors:**
- **Background Color:** Color picker (default: #000000)
- **Text Color:** Color picker (default: #ffffff)
- **Accent Color:** Color picker (default: #c2956c)

**Background Image Position:**
- **Tablet BG Image Position:** Range 1-100% (default: 50%) - X-axis position for tablet view
- **Mobile BG Image Position:** Range 1-100% (default: 50%) - X-axis position for mobile view

**Blocks:**

1. **Story Block** (Limit: 2)
   - **Image:** Image picker
   - **Text:** Rich text editor
   - **Content Alignment:** Image First, Text First

2. **Punch Out Headline Block** (Limit: 1)
   - **Headline:** Text input

**Image Requirements:**
- **Format:** JPG or PNG (section auto-detects)
- **File Location:** `/cdn/shop/files/`
- **Naming:** `{prefix}__0.{ext}`, `{prefix}__1.{ext}`, etc.
- **Max Images:** 50 (numbered 0-49)
- **Recommended Size:** 1920px × 1080px (16:9) or larger

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

#### Team Store Banner (`team-store-banner.liquid`)

**Purpose:** Banner section for team store collection pages with date display, status messages, and disclaimer

**Settings:**

**Colors:**
- **Background Color:** Color picker (default: #F3F3F3)

**Section Padding:**
- **Desktop Padding Top:** Number (px) (default: 40)
- **Desktop Padding Bottom:** Number (px) (default: 40)
- **Mobile Padding Top:** Number (px) (default: 40)
- **Mobile Padding Bottom:** Number (px) (default: 40)

**Blocks:**

1. **Team Store Message Block** (Unlimited)
   - No settings - Displays team store open/close dates automatically
   - Shows date messages based on collection `custom.start_date` and `custom.end_date` metafields

2. **Description Block** (Unlimited)
   - **Shipping Description:** Rich text editor
     - Default: Customization disclaimer about shipping times and return policy
   - **Text Style:** Body - Default, Body - xSmall, Body - Small, Body - Medium, Body - Large, Subtitle
   - **Description Color - Desktop:** Color picker
   - **Description Color - Mobile:** Color picker

3. **Statuses Description Block** (Unlimited)
   - **Approved Description:** Rich text editor
     - Default: "The product is ready to buy, and the custom graphic is approved."
   - **Declined Description:** Rich text editor
     - Default: "The product is declined, and will not be available to buy."
   - **Revised Description:** Rich text editor
     - Default: "The revision request will be submitted after all statuses are updated on all products."
   - **Text Style:** Body - Default, Body - xSmall, Body - Small, Body - Medium, Body - Large, Subtitle
   - **Status Text Color:** Color picker

**Date Display Logic:**
- Automatically displays team store dates based on collection metafields:
  - If dates not set: "YOUR TEAM STORE DATES HAVE NOT BEEN SET YET"
  - Before start date: "YOUR TEAM STORE WILL BE OPEN ON [start date]"
  - Between start/end dates: "YOUR TEAM STORE WILL BE OPEN UNTIL [end date]"
  - After end date: "YOUR TEAM STORE CLOSED ON [end date]"

**Access Control:**
- Status messages only display for valid customers:
  - Sales representatives (`custom.sales_representative = true`)
  - Customers with matching opportunity number

**Collection Requirements:**
- Collection must have `custom.start_date` and `custom.end_date` metafields
- Collection should use `team-store-native` or `team-store-landing` template suffix

---

#### Slideshow (`slideshow.liquid`)

**Purpose:** Image carousel with multiple slides

**Settings:**

**Slideshow:**
- **Auto-Rotate:** Checkbox (enables automatic slide rotation)
- **Change Slides Every:** 3-9 seconds (default: 5) - Only applies when auto-rotate is enabled
- **Pagination Style:** Dots, Counter, Numbers - Controls how slide navigation is displayed

**Accessibility:**
- **Slideshow Description:** Text input (for screen readers) - Describes slideshow content for accessibility

**Section Padding:**
- **Desktop Top Padding:** Number (px) - Default: 0
- **Desktop Bottom Padding:** Number (px) - Default: 0
- **Mobile Top Padding:** Number (px) - Default: 0
- **Mobile Bottom Padding:** Number (px) - Default: 0

**Layout:**
- **Slide Height:** Adapt, Small, Medium, Large, Extra Large - Controls slide container height
- **Image Fit:** Contain, Cover - How images fit within slide containers

**Colors:**
- **Section Background Color:** Color picker - Background color for slideshow section

**Blocks:**

**Slide Block** (Unlimited)
- **Image:** Image picker
  - **Recommended:** 1920px × 1080px (16:9)
  - **Format:** JPG, PNG, WebP
  - **Max file size:** 500KB recommended
- **Mobile Image:** Image picker (optional)
  - **Recommended:** 750px × 422px (16:9)
  - **Format:** JPG, PNG, WebP
  - **Max file size:** 200KB recommended
- **Link:** URL (makes entire slide clickable)
- **Heading:** Text input - Main slide heading
- **Subheading:** Text input - Secondary slide text
- **Button Label:** Text input - CTA button text (leave blank to hide button)
- **Button Link:** URL - CTA button destination
- **Text Box Position:** Top Left, Top Center, Top Right, Middle Left, Middle Center, Middle Right, Bottom Left, Bottom Center, Bottom Right - Position of text overlay on slide
- **Text Alignment:** Left, Center, Right - Text alignment within text box
- **Text Color:** Color picker - Color for heading and subheading text
- **Overlay Opacity:** 0-100% - Dark overlay opacity for text readability (default: 0%)

---

## Image Specifications

### General Image Guidelines

**Recommended Formats:**
- JPG for photographs
- PNG for graphics with transparency
- WebP for optimized images (supported by theme)

**File Size:**
- Desktop images: 500KB or less recommended
- Mobile images: 200KB or less recommended
- Use image optimization tools before upload

**Aspect Ratios:**

**16:9 (Landscape)**
- Desktop: 1920px × 1080px
- Mobile: 750px × 422px
- Use for: Video covers, hero banners, slideshows

**1:1 (Square)**
- Desktop: 1200px × 1200px
- Mobile: 750px × 750px
- Use for: Product cards, featured collections, social media

**4:5 (Portrait)**
- Desktop: 1200px × 1500px
- Mobile: 600px × 750px
- Use for: Product images, featured collections

**9:16 (Vertical)**
- Desktop: 1080px × 1920px
- Mobile: 422px × 750px
- Use for: Mobile-specific banners

**Adapt (Natural Aspect Ratio)**
- Use original image dimensions
- Theme will maintain aspect ratio

---

## Navigation Sections

### Shopify Menus Implementation

RUDIS uses **29 navigation menus** throughout the theme. Menus are managed in Shopify Admin and rendered in theme sections using Liquid's `linklists` object.

### Menu Access in Liquid

**Accessing Menus:**
```liquid
{% for link in linklists['menu-handle'].links %}
  {{ link.title }}
  {{ link.url }}
{% endfor %}
```

**Menu Handle:**
- Menus are accessed by their **handle** (lowercase, hyphenated version of menu name)
- Example: Menu "Footer Support" has handle `footer-support`
- Menu handle is set in Shopify Admin when creating the menu

### Header Menu Implementation

**Header Section (`header.liquid`):**

The header section uses the menu assigned in theme settings:

```liquid
{%- if section.settings.menu != blank -%}
  {%- for link in linklists[section.settings.menu].links -%}
    <!-- Menu items rendered here -->
  {%- endfor -%}
{%- endif -%}
```

**Menu Assignment:**
- Menu is assigned in theme customizer: **Header** section → **Menu** dropdown
- Theme setting key: `section.settings.menu`
- Value is the menu handle (e.g., `main-menu`, `utility-menu`)

**Menu Components:**
- `menu-bar.liquid` - Main navigation menu bar
- `menu-drawer-list.liquid` - Mobile menu drawer
- `menu-list.liquid` - Standard menu list
- `menu-link-item.liquid` - Individual menu link item
- `menu-header-drawer.liquid` - Menu drawer component

### Footer Menu Implementation

**Footer Section (`footer.liquid`):**

Footer menus are assigned in theme customizer settings:

```liquid
{%- if section.settings.footer_menu != blank -%}
  {%- for link in linklists[section.settings.footer_menu].links -%}
    <!-- Footer menu items -->
  {%- endfor -%}
{%- endif -%}
```

**Multiple Footer Menus:**
- Footer can have multiple menu columns
- Each column can have its own menu assignment
- Settings: `footer_menu_1`, `footer_menu_2`, `footer_menu_3`, etc.

### Announcement Bar Menu

**Announcement Bar Section (`announcement-bar.liquid`):**

Utility menu displayed in announcement bar:

```liquid
{% for link in linklists[section.settings.utility_menu].links %}
  <div class="announcement-bar__menu-item" data-menu-link-handle="{{ link.handle }}">
    <a href="{{ link.url }}">{{ link.title }}</a>
  </div>
{% endfor %}
```

**Menu Assignment:**
- Theme setting: `section.settings.utility_menu`
- Assigned in theme customizer: **Announcement Bar** → **Utility Menu** dropdown

### Menu Item Properties

**Standard Menu Item Properties:**
- `link.title` - Display text
- `link.url` - Link URL (relative or absolute)
- `link.handle` - URL handle (lowercase, hyphenated)
- `link.type` - Link type (collection, page, product, http, etc.)
- `link.object` - Shopify object (collection, page, product)

**Nested Menu Items:**
- `link.links` - Child menu items (submenus)
- `link.levels` - Menu depth level
- `link.parent` - Parent menu item (if nested)

**Example - Nested Menu:**
```liquid
{% for link in linklists['main-menu'].links %}
  <a href="{{ link.url }}">{{ link.title }}</a>
  {% if link.links.size > 0 %}
    <ul>
      {% for child_link in link.links %}
        <li><a href="{{ child_link.url }}">{{ child_link.title }}</a></li>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
```

### Menu Link Types

**Collection Links:**
- `link.type` = `collection`
- `link.object` = Collection object
- `link.url` = `/collections/{handle}`

**Page Links:**
- `link.type` = `page`
- `link.object` = Page object
- `link.url` = `/pages/{handle}`

**Product Links:**
- `link.type` = `product`
- `link.object` = Product object
- `link.url` = `/products/{handle}`

**HTTP Links (External):**
- `link.type` = `http`
- `link.url` = Full URL (e.g., `https://www.rudis.com/...`)

**Frontpage Links:**
- `link.type` = `frontpage`
- `link.url` = `/`

**Search Links:**
- `link.type` = `search`
- `link.url` = `/search`

### Menu Component Files

**Menu Snippets:**
- `snippets/menu-list.liquid` - Standard menu list rendering
- `snippets/menu-list-image.liquid` - Menu list with images
- `snippets/menu-list-promos.liquid` - Menu list with promotional content
- `snippets/menu-list-activity.liquid` - Menu list with activity indicators
- `snippets/menu-link-item.liquid` - Individual menu link item component
- `snippets/menu-search.liquid` - Menu search component
- `snippets/menu-search-modal.liquid` - Menu search modal

**Menu CSS:**
- `assets/component-menu-drawer.css` - Menu drawer styles
- `assets/component-list-menu.css` - List menu styles
- `assets/component-mega-menu.css` - Mega menu styles (if used)

**Menu JavaScript:**
- Menu drawer functionality in `assets/global.js`
- Mobile menu toggle in header section

### Menu Data Structure

**RUDIS Menu Inventory:**
- **Total Menus:** 29 navigation menus
- **Menu Types:**
  - Header navigation (main menu, utility menu)
  - Footer menus (footer, support, policies)
  - Special purpose (customer account, partnership, collection menus)

**Menu Data Export:**
- Menu data available in: `/Users/pete/dev/shopify/rudis-documentation/data/AD-EVERYTHING-Export_2025-10-22_131917/Menus.csv`
- CSV includes: Menu ID, handle, title, menu items, parent-child relationships

### Menu Configuration

**Menu Assignment in Theme Settings:**

Menus are assigned in theme customizer sections:
1. **Header Section:**
   - Setting: `menu` (dropdown)
   - Selects main navigation menu

2. **Footer Section:**
   - Settings: `footer_menu_1`, `footer_menu_2`, `footer_menu_3` (dropdowns)
   - Multiple footer columns

3. **Announcement Bar Section:**
   - Setting: `utility_menu` (dropdown)
   - Utility navigation items

**Theme Settings Schema:**
Menus are defined in `config/settings_schema.json` with menu picker inputs:

```json
{
  "type": "link_list",
  "id": "menu",
  "label": "Menu",
  "default": "main-menu"
}
```

### Menu Best Practices

**Menu Handle Naming:**
- Use lowercase, hyphenated handles
- Keep handles descriptive (e.g., `footer-support`, `utility-menu`)
- Avoid special characters or spaces

**Menu Structure:**
- Limit main navigation to 5-7 items
- Use nested menus for subcategories
- Keep menu depth reasonable (2-3 levels max)

**Performance:**
- Menus are cached by Shopify
- Menu changes appear immediately
- No page rebuild required for menu updates

**Accessibility:**
- Ensure proper ARIA labels for menu items
- Support keyboard navigation
- Test menu accessibility with screen readers

### Code References

**Header Menu:**
```68:68:sections/header.liquid
  <header class="header page-width {% if section.settings.menu != blank %} header--has-menu{% endif %}">
```

```90:90:sections/header.liquid
    {%- if section.settings.menu != blank -%}
```

**Announcement Bar Menu:**
```44:51:sections/announcement-bar.liquid
    <div class="announcement_bar__menu">
      {% for link in linklists[section.settings.utility_menu].links %}
          {%- render "function.is_menu_item_hidden", link: link -%}
          {%- unless is_menu_item_hidden -%}
          <div class="announcement-bar__menu-item" data-menu-link-handle="{{ link.handle }}">
            <a href="{{ link.url }}">{{ link.title }}</a>
          </div>
```

**Menu List Component:**
See `snippets/menu-list.liquid` for menu rendering implementation.

---

## Custom Features

### Team Store Functionality

Team Stores are a B2B micro-site system built into the RUDIS theme that enables wrestling teams to customize products with team-specific colors, logos, and personalization. The system is powered by Shopify metaobjects, GraphQL API calls, custom JavaScript classes, and a complex approval workflow.

**📚 For complete Team Store/B2B system documentation, including Celigo, NetSuite, and custom cart logic, see: [Team Store/B2B Documentation](team-store-b2b.md)**

#### Architecture Overview

**Core Components:**
- **Templates:** `product.team-store-pdp.json`, `collection.team-store-native.json`, `collection.team-store-landing.json`
- **Sections:** `main-product-team-store.liquid`, `main-collection-team-store.liquid`, `team-store-banner.liquid`
- **Snippets:** `team-store-revision-form.liquid`, `product-card-team-store.liquid`, `product-card-team-store-quick-order.liquid`
- **JavaScript:** `team-product.js`, `team-store-redirect.js`
- **CSS:** `section-team-store-banner.css`, `component-product-grid-team-store.css`, `team-store-bar.css`

**Key Files:**
```12:49:sections/main-product-team-store.liquid
{%- liquid
    assign isCustomTeamBlank = product.metafields.custom.is_custom_team_blank
    assign teamParentSku = product.metafields.custom.parent_sku
    assign customerIsRep = customer.metafields.custom.sales_representative | default: false
    assign customerOppNum = customer.current_location.metafields.custom.opportunity_number | default: '' | json
    assign priceLevel = customer.current_location.metafields.custom.price_level.value[0] | default: 'Sales Rep Floor Price' | json
```

#### Data Structures & Metafields

**Product Metafields:**  
See [Data Guide - Product Metafields (Team Store)](data-guide.md#team-store-metafields) for complete documentation.
- `custom.is_custom_team_blank` (boolean) - Triggers team store product template
- `custom.team_gear_product` (boolean) - Marks product as team gear
- `custom.parent_sku` (text) - Parent SKU for team products (format: `{sku_prefix}{base_sku}`)
- `custom.team_store_close_date` (date) - Product-level close date override

**Collection Metafields:**  
See [Data Guide - Collection Metafields (Team Store)](data-guide.md#team-store-collection-metafields) for complete documentation.
- `custom.start_date` (date) - Store opening date (YYYY-MM-DD format)
- `custom.end_date` (date) - Store closing date (YYYY-MM-DD format)
- `custom.team_product_data` (JSON) - Team product configuration data
- `custom.opportunity_number` (text) - Team opportunity identifier

**Customer/Location Metafields:**  
See [Data Guide - Customer & Location Metafields](data-guide.md#customer--location-metafields) for complete documentation.
- `customer.metafields.custom.sales_representative` (boolean) - Grants sales rep access
- `customer.current_location.metafields.custom.opportunity_number` (text) - Team opportunity number
- `customer.current_location.metafields.custom.price_level.value[0]` (text) - Price tier (e.g., "Sales Rep Floor Price")

**Metaobject Type: `art_id`**  
See [Data Guide - Team Store Metaobjects](data-guide.md#team-store-metaobjects) for complete field documentation.
- **Handle Format:** `{parent_sku}_{opportunity_number}` (e.g., `RUDIS12345_67890`)
- **Key Fields:**
  - `opportunity_id` - Team opportunity number
  - `proof_status` - Approval status ("Approved", "Pending Revision", "Declined", "Pending Approval")
  - `include_default_images` (boolean/string) - Controls default image display
  - `personalization` (boolean/string) - Enables name/number personalization
  - `tier_pricing` (JSON) - Pricing tiers with quantity breaks
  - `upcharge_price` (number) - Additional embellishment cost
  - `price_override` (number) - Overrides all other pricing
  - `min_order_qty` (number) - Minimum order quantity
  - `entry_sku` - Entry SKU reference
  - `team_store_collection` - Reference to collection metaobject

#### GraphQL API Integration

Team Store products fetch metaobject data via Shopify Storefront GraphQL API:

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

**API Endpoint:** `{shop.secure_url}/api/graphql.json`  
**Access Token:** Hardcoded in theme (Storefront API token)  
**Event System:** Uses `CustomEvent('metaobjectDataRetrieved')` to notify components when data is available

```86:135:sections/main-product-team-store.liquid
            fetch(teamProductData.domain + '/api/graphql.json', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Shopify-Storefront-Access-Token': teamProductData.grapgqlToken,
                },
                body: JSON.stringify({ query: graphqlQuery }),
            })
            .then(response => {
                const elements = document.querySelectorAll('.product__media-list');
                elements.forEach(element => {
                  element.classList.remove('loading');
                  element.classList.add('loaded');
                });
                return response.json();
            })
            .then(response => {
                const responseObj = response.data.metaobject
                const fields = responseObj?.fields;
                const metaobject = fields?.reduce((acc, field) => {
                    acc[field.key] = field.value;
                    return acc;
                }, {});
                const teamStoreMetafields = responseObj?.team_store_collection?.reference?.metafields;
                const teamStoreCollection = teamStoreMetafields?.reduce((acc, field) => {
                    if (field && field.key && field.value) {
                        acc[field.key] = field.value;
                    }
                    return acc;
                }, {});

                teamStoreCollection.id = responseObj?.team_store_collection?.reference?.id;
                teamStoreCollection.url = responseObj?.team_store_collection?.reference?.onlineStoreUrl;
                metaobject.handle = metaobjectHandle;
                metaobject.isTeamStoreClosed = !teamStoreCollection?.end_date ||
                 !teamStoreCollection?.start_date ||
                 (teamStoreCollection.end_date && Date.now() > new Date(teamStoreCollection.end_date)) ||
                 (teamStoreCollection.start_date && Date.now() < new Date(teamStoreCollection.start_date)); 
                teamProductData.metaobject = metaobject;
                teamProductData.teamStoreCollection = teamStoreCollection;

                if (metaobject) {
                  const event = new CustomEvent('metaobjectDataRetrieved', { detail: {metaobject, teamStoreCollection} });
                  window.dispatchEvent(event);
                }
            })
```

#### JavaScript Architecture

**Global Data Object:** `window.teamProductData`
```34:49:sections/main-product-team-store.liquid
        window.teamProductData = {};
        const { teamProductData } = window;
        teamProductData.domain = {{ shop.secure_url | json }};
        teamProductData.priceLevel = {{ priceLevel }};
        teamProductData.teamParentSku = {{ teamParentSku | json }};
        teamProductData.grapgqlToken = '4276cb8ce158134eb5d9c2cb08c46cd0';
 
        // Save the opportunity number if it's passed in via URL, otherwise try to get it from localStorage
        let opportunityNumber = new URLSearchParams(window.location.search).get('opportunity_number');
        if (opportunityNumber) {
          localStorage.setItem('opportunity_number', opportunityNumber);
        } else {
          opportunityNumber = localStorage.getItem('opportunity_number');
        }
        teamProductData.opportunityNumber = opportunityNumber;

        teamProductData.isTeamAdmin = {{ customerIsRep }} || {{ customerOppNum }} === teamProductData.opportunityNumber;
```

**TeamStorePriceChart Class** (`assets/team-product.js`)
- Manages tier-based pricing calculations
- Handles price overrides and upcharges
- Updates DOM with calculated prices
- Stores pricing data in cart properties

```2:49:assets/team-product.js
  class TeamStorePriceChart {
      constructor() {
        this.teamProductData = window.teamProductData || {};
        this.metaobject = this.teamProductData?.metaobject;
        this.viewModel = this.getViewModel(document.querySelector('.product-container'));
        this.tierPricing = null;
        this.upchargePrice = null;
        this.priceOverride = null;
        this.priceTier = null;

        this.init();
      }

      init() {
          if (!this.metaobject) {
              window.addEventListener('metaobjectDataRetrieved', (event) => {
                  this.metaobject = event.detail.metaobject;
                  this.bindEvents();
              });
          } else {
              this.bindEvents();
          }
      }

      bindEvents() {
          this.tierPricing = JSON.parse(this.metaobject.tier_pricing);
          this.upchargePrice = this.metaobject.upcharge_price;
          this.priceOverride = this.metaobject.price_override;

          // That price if exists should override any other price.
          if (+this.priceOverride) { // If empty string +"" => 0
              const overridePrice = this.calculatePrice(this.priceOverride);
              this.updatePrice(overridePrice);
              return;
          }

          if (this.teamProductData.isTeamAdmin) {
              this.priceTier = this.tierPricing[this.teamProductData.priceLevel.toLowerCase().replace(/ /g,"_")];
              if (this.priceTier && this.viewModel.$cartPropertiesPriceTierInput) this.viewModel.$cartPropertiesPriceTierInput.value = JSON.stringify(this.priceTier);
              this.setPriceRange(this.priceTier);

              return;
          }

          // Fallback to base price for non-admin users or if no priceOverride exists.
          const basePrice = this.calculatePrice(this.tierPricing.base_price.prices["Price 1"]);
          this.updatePrice(basePrice);
      }
```

**TeamProductPageDetails Class** (`assets/team-product.js`)
- Sets embellishment pricing display
- Manages minimum order quantity (MOQ) messaging
- Populates cart item properties with metaobject data

```137:192:assets/team-product.js
    class TeamProductPageDetails {
        constructor() {
          this.teamProductData = window.teamProductData;
          this.metaobject = window.teamProductData.metaobject;
          this.viewModel = this.getViewModel(document.querySelector('.product-container'));
          this.variables = {
          }

          this.init();
        }

        init() {
            if (!this.metaobject) {
              window.addEventListener('metaobjectDataRetrieved', (event) => {
                  this.metaobject = event.detail.metaobject;
                  this.bindEvents();
              });
            } else {
                this.bindEvents();
            }
        }

        bindEvents() {
            this.setEmbelishmentPrice();
            this.setMoq();
            this.setCartItemProperties();
        }

        setCartItemProperties() {
            const isJSON = (str) => {
                try {
                    JSON.parse(str);
                    return true;
                } catch (e) {
                    return false;
                }
            };

            for (const [ key, value] of Object.entries(this.metaobject)) {
                const inputElement = this.viewModel.cartProperties[`$${key}`];
                if (inputElement) {
                    inputElement.value = value;
                }
            } 

            if (this.teamProductData?.priceLevel) {
                this.viewModel.cartProperties.$price_level.value = this.teamProductData.priceLevel;
            }

            const collectionProductsData = this.teamProductData.teamStoreCollection.team_product_data;
            if (isJSON(collectionProductsData)) {
                const imageUrl = JSON.parse(collectionProductsData)[this.metaobject.entry_sku]?.imageLink;
                if (imageUrl) this.viewModel.cartProperties.$image.value = imageUrl;
            }

        }
```

**CustomValidator Class** (`assets/team-product.js`)
- Validates personalization fields (last name requirement)
- Prevents add to cart if validation fails
- Manages "No Last Name" checkbox functionality

#### Image Gallery Management

**Image Indexing System:**
Team store products use a strict image indexing system via `data-image-index` attributes:

```172:189:sections/main-product-team-store.liquid
                    // Go through default image gallery and filter our only image with specific index that saved in the "data-image-index"
                    galleryImages.forEach(media => {
                        const dataImageIndex = parseInt(media.getAttribute('data-image-index'));

                        // Acceptance Criteria. Open team store PDPs only have custom images first. Then images named 0010-0019 for the model shots,
                        // then 0030-0039 for the detailed shots in that order. This should not include any images that are named outside of the mentioned range.
                        if (!Number.isNaN(dataImageIndex)) {
                            if ((dataImageIndex >= 10 && dataImageIndex <= 19) || (dataImageIndex >= 30 && dataImageIndex <= 39)) {
                                // Use index as flex order value (all custom image has -1 order to be first)
                                media.style.order = dataImageIndex;
                            } else {
                                media.classList.add('hidden');
                            }
                        } else { // Hide if there is no index was found
                            media.classList.add('hidden');
                        }
                    });
```

**Image Display Logic:**
1. **Custom Images:** No `data-image-index` (display first, order: -1)
2. **Model Shots:** `data-image-index` 10-19 (display second)
3. **Detail Shots:** `data-image-index` 30-39 (display third)
4. **All Other Images:** Hidden

**Dynamic Custom Image Loading:**
Custom images are fetched from `/cdn/shop/files/` using a naming convention:

```191:254:sections/main-product-team-store.liquid
                const opportunityNumber = event.detail.metaobject.opportunity_id;
                const skuTeamPrefix = teamProductData.teamParentSku.slice(0, 5);
                const productParentSku = teamProductData.teamParentSku.slice(5);

                let filesPath = document.getElementById('filesPath').value;
                let filesPathSlices = filesPath.indexOf("?");
                if (filesPathSlices !== -1) {
                  filesPath = filesPath.substring(0, filesPathSlices);
                }
                filesPath = '/cdn/shop/files/'
                let imgHandle = '';
                let imageUrl = '';

                for (let i = 1; i <= 3; i++) {
                  imgHandle = `${skuTeamPrefix}${opportunityNumber}_${productParentSku}__P${i}.webp`;
                  imageUrl = `${filesPath}${imgHandle}`;
                  
                  fetch(imageUrl)
                    .then(response => {
                      const elements = document.querySelectorAll('.product__media-list');
                      elements.forEach(element => {
                        element.classList.remove('loading');
                        element.classList.add('loaded');
                      });
                      if (!response.ok) {
                        throw new Error('Network response was not ok');
                      }
                      return response.blob();
                    })
                    .then(blob => {
                      var img = document.createElement('img');
                      img.src = URL.createObjectURL(blob);

                      let containersDesktop = document.querySelectorAll(`.Slide-P${i}`);
                      let containersMobile = document.querySelectorAll(`.Slide-P${i}--mobile`);

                      // Function to create a new img element
                      function createImgElement(blobUrl) {
                        let img = document.createElement('img');
                        img.src = blobUrl;
                        return img;
                      }

                      // Append the img element to each desktop container
                      containersDesktop.forEach(element => {
                        const customImageContainer = element.closest('.product__media-item');
                        customImageContainer.classList.remove('hidden');
                        let newImg = createImgElement(img.src);
                        element.appendChild(newImg);
                      });

                      // Append the img element to each mobile container
                      containersMobile.forEach(element => {
                        const customImageContainer = element.closest('.product__media-item--custom');
                        customImageContainer.classList.remove('hidden');
                        let newImg = createImgElement(img.src);
                        element.appendChild(newImg);
                      });

                    })
                    .catch(error => {
                      console.error('Error loading image:', error);
                    });
                }
```

**Image File Naming Convention:**
- Format: `{sku_prefix}{opportunity_number}_{base_sku}__P{1-3}.webp`
- Example: `RUDIS67890_RUDIS12345__P1.webp`
- Up to 3 custom images per product (P1, P2, P3)

#### Pricing System

**Tier Pricing Structure:**
Pricing is stored in metaobject `tier_pricing` field as JSON:
```json
{
  "sales_rep_floor_price": {
    "quantities": {"Quantity 1": 1, "Quantity 2": 12, "Quantity 3": 24},
    "prices": {"Price 1": 25.00, "Price 2": 22.00, "Price 3": 20.00}
  },
  "base_price": {
    "prices": {"Price 1": 30.00}
  }
}
```

**Price Calculation:**
```100:104:assets/team-product.js
      calculatePrice(initialPrice) {
          const upcharge = this.upchargePrice || 0;

          return parseFloat(initialPrice) + parseFloat(upcharge);
      }
```

**Price Priority:**
1. `price_override` (if set, overrides all)
2. Tier pricing based on `priceLevel` (for team admins)
3. Base price (fallback)

**Quantity-Based Pricing:**
```83:98:assets/team-product.js
      getPriceWithQuantityDiscount = (quantity) => {
          if (this.priceOverride) return +this.priceOverride;

          const { quantities, prices } = this.priceTier;
          const quantitiesArray = Object.values(quantities);
          const pricesArray = Object.values(prices);
          const maxQty = Math.max(...quantitiesArray);

          const thresholdIndex = quantity >= maxQty
            ? Math.max(quantitiesArray.findIndex(q => (q - 1) >= quantity) - 1, 0);

          const adjustedPrice = this.calculatePrice(pricesArray[thresholdIndex]);
          this.setPriceToCartProperties(adjustedPrice);
          return adjustedPrice;
      }
```

#### Approval Workflow

**Status Management:**
Statuses are stored in metaobject `proof_status` field:
- `"Pending Approval"` - Initial state, requires action
- `"Approved"` - Product ready for purchase
- `"Pending Revision"` - Revision requested
- `"Declined"` - Product declined, not available

**Status Update API:**
Status updates are sent to external AWS Lambda endpoint:

```163:201:snippets/team-store-revision-form.liquid
            const serverURL = 'https://x8x980f5a4.execute-api.us-east-2.amazonaws.com/metafield/update-status';
            const submitButton = teamStoreForm.querySelector('.submit-button')

            submitButton.addEventListener('click', () => {
                if(skuNumber && opportunityNumber && currentStatus) {
                    const data = {
                        "metafield_handle": metaobject.handle,
                        "status": currentStatus,
                        "collection_id": teamStoreCollection?.id,
                        "team_parent_sku": skuNumber
                    };
                    
                    if(notes.value.trim()) {
                        data.comments = notes.value
                    }
        
                    fetch(serverURL, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Success:', data);
                        updateFormState(currentStatus);

                        artStatusContainer.querySelector('.submission-error-message').classList.add('hidden');
                        teamStoreForm.classList.add('hidden')

                        setTimeout(() => {
                            window.location.href = window.teamProductData.teamStoreCollection.url;
                        }, 3000);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                        artStatusContainer.querySelector('.submission-error-message').classList.remove('hidden');
                    });
                }
```

**Status Display Logic:**
```74:117:snippets/team-store-revision-form.liquid
            function updateFormState(newStatus) {
                artStatusIcons.forEach((icon) => icon.classList.add('hidden'));
                artStatusLabel.classList.remove('pending', 'approved', 'declined', 'revised');
                if(newStatus == ArtProductStatuses.pending) {
                    artStatusLabelText.innerHTML = 'Action Required';
                    artStatusLabel.classList.add('pending');
                    artStatusPendingIcon.classList.remove('hidden');
                } else if(newStatus == ArtProductStatuses.revised) {
                    artStatusLabelText.innerHTML = "Revised";
                    artStatusLabel.classList.add('revised');
                    artStatusRevisedIcon.classList.remove('hidden');
                    artStatusSubmittedText.classList.remove('hidden');
                } else if(newStatus == ArtProductStatuses.declined) {
                    artStatusLabelText.innerHTML = 'Declined';
                    artStatusLabel.classList.add('declined');
                    artStatusDeclinedIcon.classList.remove('hidden');
                    artStatusSubmittedText.classList.remove('hidden');
                } else if(newStatus == ArtProductStatuses.approved) {
                    artStatusLabelText.innerHTML = 'Approved';
                    artStatusLabel.classList.add('approved');
                    artStatusApprovedIcon.classList.remove('hidden');
                    artStatusSubmittedText.classList.remove('hidden');
                } else {
                    artStatusLabelText.innerHTML = 'Status Unavailable';
                    artStatusLabel.classList.add('unknown');
                    artStatusPendingIcon.classList.remove('hidden');
                }
            }
```

#### Access Control

**Access Check Logic:**
```51:51:sections/main-product-team-store.liquid
        teamProductData.isTeamAdmin = {{ customerIsRep }} || {{ customerOppNum }} === teamProductData.opportunityNumber;
```

**Collection Access:**
```9:15:sections/team-store-banner.liquid
{% assign customer_opp_num = customer.current_location.metafields.custom.opportunity_number | default: '' %}
{% assign customer_is_rep = customer.metafields.custom.sales_representative | default: false %}
{% assign collection_opp_num = collection.metafields.custom.opportunity_number | default: '' %}
{% assign is_valid_customer = false %}

{% if customer_is_rep %}
  {% assign is_valid_customer = true %}
{% elsif customer_opp_num == collection_opp_num and customer_opp_num != '' %}
  {% assign is_valid_customer = true %}
{% endif %}
```

**Redirect Logic:**
Team store redirect script handles authentication flow:

```1:47:assets/team-store-redirect.js
// Story
// When user gets the Proof Store email, they get redirected back to Homepage after login instead of the proof store link they came from.
// Once the coach steps on the collection in the proof stage he should see modal pop up with some text that you have to login to see your collection.
// After login he will be redirected to that collection.

const COLLECTION_REDIRECT_KEY='teamProofStoreCollection';
const domain = window.location.origin;

document.addEventListener('DOMContentLoaded', () => {
    handleModal();
    handleRedirect();
});

function handleModal() {
  const modal = document.getElementById('team-modal');
  const modalBackdrop = document.getElementById('team-modal-backdrop');
  const modalButton = document.getElementById('team-modal-button');
  const collectionUrl = window.location.pathname;

  if (modal) {
      modal.classList.add('open');
      modalBackdrop.style.display = 'block';

      modalBackdrop.addEventListener('click', () => {
        modal.classList.remove('open');
        modalBackdrop.style.display = 'none';
      });

      modalButton.addEventListener('click', () => {
          localStorage.setItem(COLLECTION_REDIRECT_KEY, collectionUrl);

          window.location.href = domain + '/account/login';
      });
  }
}

function handleRedirect() {
    const redirectUrlCash = localStorage.getItem(COLLECTION_REDIRECT_KEY);

    if (redirectUrlCash) {
        localStorage.removeItem(COLLECTION_REDIRECT_KEY);
        const domain = window.location.origin;
        const collectionUrl = `${domain}${redirectUrlCash}`;

        window.location.href = collectionUrl;
    }
}
```

**Opportunity Number Management:**
```52:57:layout/theme.liquid
    {% if collection.metafields.custom.opportunity_number %}
      <script>
          localStorage.setItem('opportunity_number', "{{ collection.metafields.custom.opportunity_number }}");
          localStorage.setItem('team_collection_link', "{{ collection.url }}");
      </script>
    {% endif %}
```

#### Date-Based Store Control

**Store Open/Close Logic:**
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

**JavaScript Store Status:**
```120:123:sections/main-product-team-store.liquid
                metaobject.isTeamStoreClosed = !teamStoreCollection?.end_date ||
                 !teamStoreCollection?.start_date ||
                 (teamStoreCollection.end_date && Date.now() > new Date(teamStoreCollection.end_date)) ||
                 (teamStoreCollection.start_date && Date.now() < new Date(teamStoreCollection.start_date));
```

#### Cart Integration

**Cart Properties:**
Team store products add hidden input fields to cart for order processing:

```165:191:assets/team-product.js
        setCartItemProperties() {
            const isJSON = (str) => {
                try {
                    JSON.parse(str);
                    return true;
                } catch (e) {
                    return false;
                }
            };

            for (const [ key, value] of Object.entries(this.metaobject)) {
                const inputElement = this.viewModel.cartProperties[`$${key}`];
                if (inputElement) {
                    inputElement.value = value;
                }
            } 

            if (this.teamProductData?.priceLevel) {
                this.viewModel.cartProperties.$price_level.value = this.teamProductData.priceLevel;
            }

            const collectionProductsData = this.teamProductData.teamStoreCollection.team_product_data;
            if (isJSON(collectionProductsData)) {
                const imageUrl = JSON.parse(collectionProductsData)[this.metaobject.entry_sku]?.imageLink;
                if (imageUrl) this.viewModel.cartProperties.$image.value = imageUrl;
            }

        }
```

**Cart Property Fields:**
- `#ts_price` - Calculated price
- `#ts_price_tier` - Tier pricing JSON
- `#ts_image` - Product image URL
- `#ts_min_order_qty` - Minimum order quantity
- `#ts_price_level` - Price level/tier
- `#ts_opportunity_id` - Opportunity number
- `#ts_version_number` - Design version
- `#ts_customization_embellishment_type` - Embellishment type
- `#ts_display_name` - Display name
- `#ts_entry_sku` - Entry SKU
- `#ts_upcharge` - Upcharge price
- `#ts_back_print` - Back print option
- `#_ts_sleeve_print` - Sleeve print option
- `#ts_personalization` - Personalization enabled

#### Personalization System

**Last Name Field:**
```150:154:sections/main-product-team-store.liquid
                const isPersonalization = event.detail.metaobject.personalization;
                const isApproved = event.detail.metaobject.proof_status;
                if (isPersonalization === "true" && isApproved === 'Approved' && !event.detail.metaobject.isTeamStoreClosed) {
                  document.getElementById('lastNameField').style.display = "block";
                }
```

**Validation:**
```276:286:assets/team-product.js
      isCustomValidationPassed = () => {
          const { $noLastNameCheckbox, $nameInput } = this.viewModel.lastNameOption;

          // Validate Last name input only if personalization true and checkbox "No name" is not checked
          if (!$nameInput.value && !$noLastNameCheckbox.checked && this.metaobject.personalization === "true") {
              $nameInput.classList.add('invalid')
              return false;
          }

          return true;
      }
```

#### Status Messages (Collection Level)

**Status Key Messages Block:**
```64:90:sections/main-collection-team-store.liquid
  "blocks": [
    {
      "type": "status_key_messages",
      "name": "Status Key Messages",
      "settings" : [
          {
            "type": "richtext",
            "label": "Approved Description",
            "id": "approved",
            "default": "<p>YOUR GEAR LOOKS GREAT: Your sale's rep will contact you soon to order.</p>"
          },
          {
            "type": "richtext",
            "label": "Action Required Description",
            "id": "action_required",
            "default": "<p>ACTION REQUIRED: Update the status on ALL products to proceed with your order.</p>"
          },
          {
            "type": "richtext",
            "label": "In Revision Description",
            "id": "in_revision",
            "default": "<p>REVISIONS IN PROGRESS: You will be notified when action is required.</p>"
          }
      ]
    }
  ]
```

#### File Reference Summary

**Templates:**
- `templates/product.team-store-pdp.json` - Team store product template
- `templates/collection.team-store-native.json` - Native team store collection
- `templates/collection.team-store-landing.json` - Team store landing page

**Sections:**
- `sections/main-product-team-store.liquid` - Main team store product section
- `sections/main-collection-team-store.liquid` - Team store collection section
- `sections/team-store-banner.liquid` - Team store banner with dates/status
- `sections/main-collection-product-grid-team-store.liquid` - Product grid for team stores

**Snippets:**
- `snippets/team-store-revision-form.liquid` - Approval workflow form
- `snippets/product-card-team-store.liquid` - Team store product card
- `snippets/product-card-team-store-quick-order.liquid` - Quick order card variant

**JavaScript:**
- `assets/team-product.js` - Team store product classes (TeamStorePriceChart, TeamProductPageDetails, CustomValidator)
- `assets/team-store-redirect.js` - Authentication redirect handler

**CSS:**
- `assets/section-team-store-banner.css` - Banner styling
- `assets/component-product-grid-team-store.css` - Product grid styling
- `assets/team-store-bar.css` - Announcement bar styling

**Layout Integration:**
```17:17:layout/theme.liquid
    {% if collection.template_suffix == 'team-store-landing' or product.metafields.custom.is_custom_team_blank %}
```

```134:134:layout/theme.liquid
    {% unless collection.template_suffix == 'team-store-landing' or product.metafields.custom.is_custom_team_blank %}
```

### Athlete Features

**Athlete Product Highlights:**
- Featured products by athlete
- Athlete-specific product templates
- Athlete branding elements

### Auction Functionality

**Auction Product Pages:**
- Countdown timers
- Bid functionality
- Auction-specific pricing display
- Special event product templates

---

## Template Variants

### Product Template Variants

**Standard Templates:**
- `product.json` - Default
- `product.alternate.json` - Alternate layout
- `product.with-free-returns-text.json` - Free returns messaging
- `product.no-reviews.json` - No reviews display
- `product.default-product-reviews.json` - Default reviews

**Shoe Templates:**
- `product.shoe-product.json` - Standard shoe
- `product.ecom-store-shoe-pdp.json` - Ecom store shoe
- `product.ds-shoe-pdp.json` - DS shoe
- `product.jb-shoe-pdp.json` - JB shoe
- `product.ks-shoe-pdp.json` - KS shoe
- `product.sh-wrestling-shoe.json` - Wrestling shoe
- `product.one-of-one-wrestling-shoe.json` - One-of-one shoe

**Brand/Athlete Templates:**
- `product.kolat.json` - Kolat brand
- `product.rocky.json` - Rocky brand
- `product.hildebrandt.json` - Hildebrandt
- `product.jb-ultra-ps.json` - JB Ultra PS
- `product.jb-ultralite.json` - JB Ultralite
- `product.chronicle-elite.json` - Chronicle Elite
- `product.alpha-2-0-happy.json` - Alpha 2.0
- `product.tmnt.json` - TMNT

**Specialized Templates:**
- `product.bundles.json` - Bundle products
- `product.bags.json` - Bag products
- `product.gift-card.json` - Gift cards
- `product.auction-pro-template.json` - Auction products
- `product.team-store-pdp.json` - Team store products
- `product.coming-soon.json` - Coming soon products

---

## Usage Guidelines

### Adding Sections to Pages

1. Navigate to the page in Shopify admin
2. Click "Customize" or use the theme customizer
3. Click "Add section"
4. Select the desired section type
5. Configure settings and add blocks as needed
6. Save changes

### Best Practices

**Image Optimization:**
- Always optimize images before upload
- Use appropriate aspect ratios for each section
- Test images on both desktop and mobile
- Use descriptive alt text for accessibility

**Content Management:**
- Use consistent heading sizes across sections
- Maintain brand color consistency
- Test animations on actual devices
- Ensure mobile responsiveness

**Performance:**
- Limit number of sections per page
- Use lazy loading for images
- Optimize video embeds
- Test page load times

---

## Reference

**Theme Code Location:** `code/theme_export__www-rudis-com-production-10-29-25__31OCT2025-0252pm/`

**Settings Schema:** `config/settings_schema.json`

**Settings Data:** `config/settings_data.json`

**Main Layout:** `layout/theme.liquid`

---

## Data Reference

For complete documentation of all metafields, metaobjects, and data structures used in the RUDIS platform, see the **[Data Guide](data-guide.md)**. The Data Guide provides comprehensive reference documentation with code examples, field-level details, and usage guidelines for all custom data structures.

