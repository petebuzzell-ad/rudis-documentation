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
5. [Global Navigation & Header](#global-navigation--header)
   - [Header Section](#header-section)
   - [Mega Menu Configuration](#mega-menu-configuration)
   - [Announcement Bar](#announcement-bar)
   - [Global Footer](#global-footer)
   - [Managing Menus in Shopify Admin](#managing-menus-in-shopify-admin)
6. [Page Template Assignments](#page-template-assignments)
7. [Custom Sections & RUDIS-Specific Components](#custom-sections--rudis-specific-components)
8. [Metafields & Custom Data](#metafields--custom-data)
9. [Media Asset Specifications](#media-asset-specifications)
10. [Making Site Updates](#making-site-updates)
11. [Troubleshooting](#troubleshooting)
12. [Data Reference](#data-reference)

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

## Global Navigation & Header

### Overview

The RUDIS storefront uses a global header section that appears on every page. The header includes navigation menus, logo, search functionality, and cart icons. The header is managed in the theme customizer and uses Shopify menus for navigation links.

---

## Header Section

### Location in Theme Customizer

**Path:** Online Store → Themes → Customize → **Header** section

The Header section is a global section that appears on all pages. All header settings are configured in this single section.

### Header Menu Assignments

**Main Shopping Menu** (`menu` setting)
- **Location:** Primary navigation bar in header (desktop and mobile)
- **Where to Edit:** Header section → **Main Shopping Menu** dropdown
- **Display:** Horizontal menu bar on desktop, mobile drawer menu on mobile
- **Purpose:** Main product/category navigation (e.g., Shop, Collections, Athletes)
- **Menu Type:** Use nested menus for subcategories (up to 3 levels supported)
- **Mega Menu Support:** Can be configured with mega menu flyouts (see [Mega Menu Configuration](#mega-menu-configuration) below)

**Main Content Menu** (`main_content_menu` setting)
- **Location:** Secondary navigation bar in header (desktop and mobile)
- **Where to Edit:** Header section → **Main Content Menu** dropdown
- **Display:** Appears next to Main Shopping Menu on desktop, below main menu in mobile drawer
- **Purpose:** Content/informational links (e.g., Blog, Stories, Media)
- **Menu Type:** Standard menu (no mega menu support)

**Utility Menu** (`utility_menu` setting)
- **Location:** Mobile menu drawer only (below main menu links)
- **Where to Edit:** Header section → **Utility menu mobile** dropdown
- **Display:** Mobile-only menu below main menu in drawer
- **Purpose:** Utility/quick links (e.g., Custom Team Gear, Outlet, Contact)
- **Icons:** Can be configured with icons via "Utility menu - icons" block (see below)

### Header Logo

**Desktop Logo** (`logo` setting)
- **Location:** Header section → **Logo** image picker
- **Display:** Desktop header (hides on mobile)
- **Width:** Configurable (Header section → **Desktop width** slider, 50-250px, default: 100px)
- **Format:** PNG recommended (transparency supported)
- **Where to Edit:** Header section → Logo section

**Mobile Logo** (`logo_mobile` setting)
- **Location:** Header section → **Sticky logo** image picker (optional)
- **Display:** Mobile header when sticky header is active
- **Width:** Configurable (Header section → **Width for sticky logo** slider, 30-250px, default: 100px)
- **Format:** PNG recommended
- **Where to Edit:** Header section → Mobile Sticky Logo section
- **Note:** If not provided, desktop logo is used on mobile

**Mobile Primary Logo** (`logo_width_mobile` setting)
- **Location:** Uses same logo as desktop but different width
- **Width:** Configurable (Header section → **Mobile width** slider, 30-250px, default: 100px)
- **Where to Edit:** Header section → Logo section

### Header Options

**Sticky Header** (`enable_sticky_header` setting)
- **Location:** Header section → **Options** → **Enable sticky header** checkbox
- **Effect:** Header stays visible when scrolling up
- **Default:** Enabled
- **Where to Edit:** Header section → Options section

**Border Line** (`show_line_separator` setting)
- **Location:** Header section → **Options** → **Show border line** checkbox
- **Effect:** Displays border between header and page content
- **Default:** Enabled
- **Where to Edit:** Header section → Options section

**Header Animations** (`enable_header_animation` setting)
- **Location:** Header section → **Animations** → **Enable header animation** checkbox
- **Effect:** Enables fade-in animations for header elements and mega menus
- **Default:** Enabled
- **Where to Edit:** Header section → Animations section
- **Note:** Must be enabled for all animation options to work

**Header Items Animation** (`enable_header_items_animation` setting)
- **Location:** Header section → **Animations** → **Show header items fade in** checkbox
- **Effect:** Fade-in animation for header menu items
- **Default:** Enabled
- **Where to Edit:** Header section → Animations section

**Mobile Icon Animation** (`enable_mobile_icon_animation` setting)
- **Location:** Header section → **Animations** → **Show mobile menu icon animation** checkbox
- **Effect:** Animated hamburger menu icon on mobile
- **Default:** Enabled
- **Where to Edit:** Header section → Animations section

### Header Blocks

**Utility Menu - Icons** (`menu_icons` block)
- **Location:** Header section → **Add block** → **Utility menu - icons**
- **Purpose:** Add icons to utility menu links in mobile drawer
- **Configuration:**
  - Icon labels must match menu link names exactly
  - Configure up to 3 icons (Icon 1, Icon 2, Icon 3)
  - For each icon:
    - **Link label:** Exact text of menu item (e.g., "Custom Team Gear")
    - **Select icon:** Choose from available icons (Account, Box, Chat Bubble, Check Mark, Clipboard, Eye, Heart, Leaf, Map Pin, Question Mark, Return, Ruler, Silhouette, Star, Store Locator)
- **Where to Edit:** Header section → Click block → Configure icon settings
- **Important:** Icon labels must match menu item names exactly and in order

**Promo Message** (`promo` block)
- **Location:** Header section → **Add block** → **Promo Message**
- **Purpose:** Display promotional messages in header (currently not visible in header, may be used elsewhere)
- **Configuration:**
  - **Message:** Text (keep under 40 characters for mobile)
  - **Link url:** Optional link for promo
  - **Text color:** Color picker
  - **Background color:** Color picker
- **Where to Edit:** Header section → Click block → Configure promo settings

### Mega Menu Configuration

Mega menus are large dropdown flyouts that appear when hovering over main menu items. They support images, promotional content, and activity links.

**Where to Configure:** Header section → **Add block** → Choose **Megamenu - link lists** or **Megamenu - image blocks**

#### Mega Menu - Link Lists

**Purpose:** Create mega menu flyouts with nested link lists and promotional content

**Configuration:**
1. **Parent Menu Item:**
   - **Menu item name:** Exact name of top-level menu item (e.g., "Boys", "Collections")
   - **Select menu style:** 
     - **Default:** Standard mega menu layout
     - **Left rail:** Left-aligned menu with rail layout

2. **Link Lists:**
   - Menu structure automatically uses nested menu items from Shopify menu
   - **Display 'All X' links?:** Checkbox to show "Shop All" links for each subcategory

3. **Promo Content** (Right side of mega menu):
   - **Promo markup (liquid):** Optional custom HTML/Liquid code
   - **Promo 1-4:** Up to 4 promotional images/links:
     - **Promo X image:** Image picker
     - **Promo X label:** Text label
     - **Promo X label subtext:** Secondary text
     - **Promo X link:** URL for promo

4. **Activity Links:**
   - **Activity Menu:** Select a menu to display as "By Activity" section
   - Appears at bottom of mega menu

**Where to Edit:** Header section → Click **Megamenu - link lists** block → Configure settings

#### Mega Menu - Image Blocks

**Purpose:** Create image-based mega menus with video thumbnails

**Configuration:**
1. **Parent Menu Item:**
   - **Menu item name:** Exact name of top-level menu item

2. **Image Blocks** (Up to 4 images):
   - **Block X label:** Menu item name that image corresponds to (must match child menu item exactly)
   - **Video X Image:** Thumbnail image
   - **Video X Thumbnail:** Text label below image
   - **Video X Link:** URL for video/content

**Where to Edit:** Header section → Click **Megamenu - image blocks** block → Configure settings

**Important:** Block labels must match child menu item names exactly for images to appear correctly.

---

## Announcement Bar

### Location in Theme Customizer

**Path:** Online Store → Themes → Customize → **Announcement bar** section

The Announcement Bar appears at the very top of every page, above the header.

### Announcement Bar Menu

**Utility Menu** (`utility_menu` setting)
- **Location:** Right side of announcement bar (desktop and mobile)
- **Where to Edit:** Announcement bar section → **Utility Menu** dropdown
- **Display:** Horizontal menu in announcement bar
- **Purpose:** Quick utility links (e.g., Custom Team Gear, Outlet, Contact)
- **Text Color:** Configurable (Announcement bar section → **Utility menu text color** color picker, default: white)
- **Note:** This is different from the header utility menu (mobile-only)

### Announcement Blocks

**Announcement** (`announcement` block)
- **Location:** Announcement bar section → **Add block** → **Announcement**
- **Purpose:** Display promotional messages or announcements
- **Configuration:**
  - **Message:** Announcement text
  - **Link url:** Optional link for announcement
  - **Link label:** Link text (if link provided)
  - **Text color:** Color picker (default: white)
  - **Link color:** Color picker (default: blue)
  - **Background color:** Color picker (default: black)
- **Carousel:** If multiple announcement blocks are added, they rotate automatically
- **Carousel Speed:** Configurable (Announcement bar section → **Slide scroll speed**, 5-15 seconds, default: 5)
- **Where to Edit:** Announcement bar section → Click announcement block → Configure settings

**Special Features:**
- Team Store links automatically appear for team store customers
- US-only display (hidden for non-US customers)

---

## Global Footer

### Location in Theme Customizer

**Path:** Online Store → Themes → Customize → **Footer** section

The Footer appears at the bottom of every page and includes multiple content blocks.

### Footer Menu Blocks

**Footer menus are added as blocks**, not as direct menu assignments.

**Link List Block** (`link_list` block)
- **Location:** Footer section → **Add block** → **Link List**
- **Purpose:** Display a menu column in footer
- **Configuration:**
  - **Heading:** Column heading text (e.g., "Support", "About")
  - **Menu:** Select menu to display
- **Display:** Desktop: Column layout, Mobile: Accordion (collapsible)
- **Where to Edit:** Footer section → Click link list block → Configure heading and menu

**Multiple Footer Menus:**
- Add multiple **Link List** blocks to create multiple footer columns
- Each block can have its own heading and menu
- Blocks automatically arrange in grid layout (1-5 columns based on number of blocks)

### Footer Logo & Text

**Logo Image** (`logo_image` setting)
- **Location:** Footer section → **Logo** section → **Image** picker
- **Display:** Top-left of footer content area
- **Where to Edit:** Footer section → Logo section

**Logo Text** (`logo_text` setting)
- **Location:** Footer section → **Logo** section → **Text** rich text editor
- **Display:** Below logo image (if provided) or standalone
- **Where to Edit:** Footer section → Logo section

### Footer Text Blocks

**Text Block** (`text` block)
- **Location:** Footer section → **Add block** → **Text**
- **Purpose:** Display custom text content in footer
- **Configuration:**
  - **Heading:** Optional heading text
  - **Subtext:** Rich text content
- **Where to Edit:** Footer section → Click text block → Configure heading and content

### Footer Image Blocks

**Image Block** (`image` block)
- **Location:** Footer section → **Add block** → **Image**
- **Purpose:** Display images in footer (logos, badges, etc.)
- **Configuration:**
  - **Image:** Image picker
  - **Image width:** Slider (50-200px, default: 100px)
  - **Image alignment:** Left, Center, Right (default: center)
- **Where to Edit:** Footer section → Click image block → Configure image settings

### Footer Newsletter

**Newsletter Enable** (`newsletter_enable` setting)
- **Location:** Footer section → **Newsletter** section → **Enable newsletter** checkbox
- **Default:** Enabled
- **Where to Edit:** Footer section → Newsletter section

**Newsletter Heading** (`newsletter_heading` setting)
- **Location:** Footer section → **Newsletter** section → **Heading** text input
- **Default:** "Subscribe to our emails"
- **Where to Edit:** Footer section → Newsletter section

**Newsletter Text** (`newsletter_text` setting)
- **Location:** Footer section → **Newsletter** section → **Text** rich text editor
- **Purpose:** Additional text below newsletter heading
- **Where to Edit:** Footer section → Newsletter section

### Footer SMS Signup

**SMS Signup Show** (`sms_signup_show` setting)
- **Location:** Footer section → **SMS Signup** section → **Show SMS Signup** checkbox
- **Default:** Enabled
- **Where to Edit:** Footer section → SMS Signup section

**SMS Signup Icon** (`sms_signup_icon` setting)
- **Location:** Footer section → **SMS Signup** section → **SMS Icon** image picker
- **Display:** Icon next to SMS signup text
- **Where to Edit:** Footer section → SMS Signup section

**SMS Signup Heading** (`sms_signup_heading` setting)
- **Location:** Footer section → **SMS Signup** section → **Heading** text input
- **Where to Edit:** Footer section → SMS Signup section

**SMS Signup Text** (`sms_signup_text` setting)
- **Location:** Footer section → **SMS Signup** section → **Text** rich text editor
- **Where to Edit:** Footer section → SMS Signup section

**SMS Signup Trigger** (`sms_signup_trigger` setting)
- **Location:** Footer section → **SMS Signup** section → **Text** (trigger button text)
- **Purpose:** Text for button that opens SMS signup form
- **Where to Edit:** Footer section → SMS Signup section

**Klaviyo Active** (`klaviyo` setting)
- **Location:** Footer section → **SMS Signup** section → **Active Klaviyo button** checkbox
- **Default:** Enabled
- **Purpose:** Enables Klaviyo SMS form integration
- **Where to Edit:** Footer section → SMS Signup section

### Footer Social Media

**Show Social** (`show_social` setting)
- **Location:** Footer section → **Social** section → **Show social** checkbox
- **Default:** Disabled
- **Effect:** Displays social media icons in footer
- **Display:** Desktop: Next to logo, Mobile: Below newsletter section
- **Where to Edit:** Footer section → Social section
- **Note:** Social media links are configured in theme settings (not in footer section)

**Social Media Links Configuration:**
- **Location:** Theme Settings → **Social media** section (not in footer section)
- **Supported Platforms:** Instagram, LinkedIn, Pinterest, Facebook, Twitter, TikTok, Tumblr, Snapchat, YouTube, Vimeo
- **Where to Edit:** Online Store → Themes → Customize → **Theme Settings** → **Social media** section
- **Note:** Icons only appear if links are provided AND "Show social" is enabled in footer section

### Footer Copyright

**Copyright Menu** (`copyright_menu` setting)
- **Location:** Footer section → **Copyright** section → **Menu** dropdown
- **Purpose:** Menu displayed in footer bottom bar (policies, privacy links)
- **Display:** Horizontal links in footer bottom bar
- **Mobile Display:** Configurable (Column or Row, Copyright section → **Copyright Menu display (mobile)**)
- **Where to Edit:** Footer section → Copyright section

**Copyright Text** (`copyright_text` setting)
- **Location:** Footer section → **Copyright** section → **Copyright Text** text input
- **Display:** Next to copyright year (e.g., "© 2025 RUDIS")
- **Where to Edit:** Footer section → Copyright section

### Footer Payment Icons

**Payment Enable** (`payment_enable` setting)
- **Location:** Footer section → **Payment** section → **Enable payment icons** checkbox
- **Default:** Disabled
- **Effect:** Displays accepted payment method icons
- **Icons:** Automatically displays all enabled payment types from Shopify settings
- **Where to Edit:** Footer section → Payment section

### Footer Country/Language Selectors

**Country Selector** (`enable_country_selector` setting)
- **Location:** Footer section → **Country selector** section → **Enable country selector** checkbox
- **Default:** Disabled
- **Effect:** Displays country/currency selector dropdown
- **Where to Edit:** Footer section → Country selector section

**Language Selector** (`enable_language_selector` setting)
- **Location:** Footer section → **Language selector** section → **Enable language selector** checkbox
- **Default:** Disabled
- **Effect:** Displays language selector dropdown
- **Where to Edit:** Footer section → Language selector section

### Footer App Settings

**App Description** (`app_description` setting)
- **Location:** Footer section → **App Settings** section → **Description** rich text editor
- **Purpose:** Display app download information
- **Where to Edit:** Footer section → App Settings section

**App Label & Link** (`app_label_one`, `app_link_one`, `app_label_two`, `app_link_two` settings)
- **Location:** Footer section → **App Settings** section
- **Purpose:** App download buttons (up to 2)
- **Configuration:**
  - **App Label One/Two:** Button text
  - **App Link One/Two:** Download URL
- **Where to Edit:** Footer section → App Settings section

### Footer Color Scheme

**Color Scheme** (`color_scheme` setting)
- **Location:** Footer section → **Colors** section → **Color scheme** dropdown
- **Options:** Accent 1, Accent 2, Background 1, Background 2, Inverse
- **Default:** Background 1
- **Effect:** Controls footer background and text colors
- **Where to Edit:** Footer section → Colors section

---

## Managing Menus in Shopify Admin

### Access Menus

**Path:** Online Store → **Navigation**

All menus are managed in Shopify Admin, then assigned to theme sections in the theme customizer.

### Creating a New Menu

1. Navigate to **Online Store** → **Navigation**
2. Click **Add menu**
3. Enter menu name (e.g., "Footer Support")
4. Click **Add menu item** to add links
5. Configure each menu item (see below)
6. Save

### Editing Menu Items

1. Select the menu to edit
2. Click **Add menu item** or edit existing items
3. Configure menu item:
   - **Name:** Display text (e.g., "Contact", "Shipping")
   - **Link:** Choose link type:
     - **Collections** - Link to a product collection
     - **Pages** - Link to a content page
     - **Products** - Link to a product page
     - **Blogs** - Link to blog or blog post
     - **HTTP** - External URL (e.g., `https://www.rudis.com/pages/custom-team-gear`)
     - **Frontpage** - Link to homepage (`/`)
     - **Search** - Link to search page (`/search`)
     - **Customer Account Page** - Link to customer account pages
4. **Parent menu item:** For nested menus, select parent item to create submenus
5. Drag to reorder items
6. Save

### Menu Item Types

**Collection Links:**
- Links to product collections (e.g., `/collections/sale`, `/collections/usa-wrestling`)
- Automatically updates when collection URL changes
- Use for category navigation

**Page Links:**
- Links to content pages (e.g., `/pages/contact`, `/pages/shipping`)
- Use for informational pages, policies, support pages

**External URLs (HTTP):**
- Links to external websites or absolute URLs
- Examples:
  - `https://www.rudis.com/blogs/stories/...` (blog posts)
  - `https://rudissupport.zendesk.com/...` (help center)
  - `https://rudis.loopreturns.com/...` (returns portal)

**Frontpage:**
- Links to homepage (`/`)
- Use for "Home" links

**Search:**
- Links to search page (`/search`)
- Use for search functionality

**Customer Account Pages:**
- Links to customer account sections (orders, addresses, etc.)
- Use for account navigation

### Creating Nested Menus (Submenus)

**Hierarchical Menu Structure:**
1. Create parent menu item (e.g., "Support")
2. Create child menu items (e.g., "Contact", "Shipping", "Returns")
3. For each child item, select the parent menu item in the **Parent menu item** dropdown
4. Child items will appear as submenus under the parent

**Mega Menu Support:**
- Nested menus up to 3 levels deep are supported
- First level (parent) triggers mega menu flyout
- Second level (child) appears as subcategories
- Third level (grandchild) appears as sub-subcategories

**Example - Footer Support Menu:**
- **Parent:** Support
  - **Child:** Contact
  - **Child:** Help Center
  - **Child:** Shipping
  - **Child:** Track my Order
  - **Child:** Returns & Exchanges

### Menu-to-Section Mapping Reference

**Quick Reference - Which Menu Goes Where:**

| Menu Setting           | Location         | Section                         | Desktop Display      | Mobile Display            |
| ---------------------- | ---------------- | ------------------------------- | -------------------- | ------------------------- |
| **Main Shopping Menu** | Header           | Header → Main Shopping Menu     | Primary nav bar      | Mobile drawer menu        |
| **Main Content Menu**  | Header           | Header → Main Content Menu      | Secondary nav bar    | Below main menu in drawer |
| **Utility Menu**       | Header           | Header → Utility menu mobile    | Hidden               | Mobile drawer only        |
| **Utility Menu**       | Announcement Bar | Announcement bar → Utility Menu | Top bar (right side) | Top bar (right side)      |
| **Footer Menus**       | Footer           | Footer → Link List blocks       | Footer columns       | Accordion sections        |
| **Copyright Menu**     | Footer           | Footer → Copyright → Menu       | Footer bottom bar    | Footer bottom bar         |

### Menu Best Practices

**Menu Organization:**
- Keep main navigation focused (5-7 items)
- Use nested menus for subcategories
- Group related items together
- Place most important links first

**Naming Conventions:**
- Use clear, descriptive names
- Keep names concise (avoid long text)
- Use consistent naming across menus
- For mega menu blocks, menu item names must match exactly (case-sensitive)

**Link Management:**
- Use collection/page links instead of HTTP when possible (easier to maintain)
- Test all links after updates
- Update external URLs when pages move
- Remove or update broken links regularly

**Menu Updates:**
- Changes appear immediately on storefront
- Test menu changes on mobile and desktop
- Verify nested menu structure displays correctly
- Check that menu items are accessible on all page types

### Troubleshooting Menus

**Menu Not Appearing:**
- Verify menu is assigned in theme customizer
- Check menu has menu items
- Ensure menu is enabled/active
- Check theme section settings
- Verify correct section is being edited

**Menu Item Links Broken:**
- Verify collection/page/product exists
- Check URL is correct
- Test external URLs
- Update HTTP links if pages moved

**Nested Menu Not Displaying:**
- Verify parent menu item is selected for child items
- Check theme supports nested menus (up to 3 levels)
- Test on mobile (may display differently)
- Verify mega menu block is configured (if using mega menus)

**Mega Menu Not Showing:**
- Verify mega menu block exists for parent menu item
- Check "Menu item name" in block matches parent menu item name exactly (case-sensitive)
- Ensure menu has nested items (child links)
- Check header animation is enabled (required for mega menu animations)

**Menu Changes Not Visible:**
- Clear browser cache
- Check theme customizer saved
- Verify correct menu is assigned
- Test in incognito/private browsing mode

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
