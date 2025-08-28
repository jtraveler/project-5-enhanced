# Birchlin

[Live Project Link](https://mj-project5-aec364964bcd.herokuapp.com/)

![Techsini.com Mockup](static/images/readme/techsini-dot-com-slash-multi-mockup.jpg)

Birchlin is a comprehensive e-commerce platform designed for outdoor enthusiasts who demand reliable, field-tested gear for their adventures. Whether you're planning your first overnight hike or preparing for an extended wilderness expedition, Birchlin connects you with the equipment that has been personally vetted by experienced outdoor professionals.

Built on Django with modern web technologies, the platform offers an intuitive shopping experience featuring advanced filtering, dynamic product galleries, and seamless checkout integration. From lightweight shelters and sleeping systems to essential safety equipment and navigation tools, every product in our catalog has been selected for its proven performance in real-world conditions.

The platform serves adventure-seekers across all experience levels, providing detailed product information, authentic user reviews, and expert guidance to help customers make informed decisions about their outdoor gear investments.

## Table of Contents

- [Birchlin](#birchlin)
  - [Table of Contents](#table-of-contents)
  - [E-commerce Applications for Birchlin](#e-commerce-applications-for-birchlin)
    - [What is E-commerce?](#what-is-e-commerce)
    - [Business Model for Birchlin](#business-model-for-birchlin)
    - [Key Ways to Define E-commerce for Birchlin](#key-ways-to-define-e-commerce-for-birchlin)
      - [WHO: Who is the customer?](#who-who-is-the-customer)
      - [WHAT: What are they buying?](#what-what-are-they-buying)
      - [HOW: How will they pay?](#how-how-will-they-pay)
  - [UX & Agile Development](#ux--agile-development)
  - [User Experience Design](#user-experience-design)
  - [Agile Methodology](#agile-methodology)
  - [Development Tools & Architecture](#development-tools--architecture)
  - [Design System](#design-system)
    - [Homepage Overview](#homepage-overview)
    - [Product Catalog Overview](#product-catalog-overview)
  - [Color Palette](#color-palette)
  - [Typography](#typography)
  - [Icons & Visual Elements](#icons--visual-elements)
  - [Technologies Used](#technologies-used)
    - [Wireframes](#wireframes)
    - [Favicon](#favicon)
    - [Languages](#languages)
    - [Frameworks & Software](#frameworks--software)
    - [Libraries and Modules](#libraries-and-modules)
    - [AWS Integration](#aws-integration)
    - [Email Services](#email-services)
    - [The Structure Plane - Database](#the-structure-plane---database)
      - [Database Design](#database-design)
      - [Entity Relationships](#entity-relationships)
    - [Version Control](#version-control)
  - [E-commerce Business Model](#e-commerce-business-model)
    - [Search Engine Optimization (SEO)](#search-engine-optimization-seo)
    - [Social Media Marketing](#social-media-marketing)
    - [Newsletter Marketing](#newsletter-marketing)
    - [Future Marketing Strategies](#future-marketing-strategies)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Navigation & Header](#navigation--header)
      - [Hero Video Section](#hero-video-section)
      - [Product Catalog](#product-catalog)
      - [Advanced Filtering System](#advanced-filtering-system)
      - [Product Detail Pages](#product-detail-pages)
      - [Shopping Cart & Checkout](#shopping-cart--checkout)
      - [User Authentication & Profiles](#user-authentication--profiles)
      - [Wishlist Functionality](#wishlist-functionality)
      - [Search Capabilities](#search-capabilities)
      - [Contact & Support](#contact--support)
      - [Admin Management](#admin-management)
      - [Responsive Design](#responsive-design)
    - [Future Features](#future-features)
  - [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Accessibility Testing](#accessibility-testing)
    - [Wave Validation](#wave-validation)
    - [Lighthouse Performance](#lighthouse-performance)
    - [JavaScript Validation](#javascript-validation)
    - [Python Code Validation](#python-code-validation)
    - [Device Testing](#device-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Manual Testing](#manual-testing)
    - [User Story Testing](#user-story-testing)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [AWS Configuration](#aws-configuration)
    - [Local Development](#local-development)
    - [Forking the Repository](#forking-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
    - [Environment Setup](#environment-setup)
  - [Credits](#credits)
    - [Code References](#code-references)
    - [Media Sources](#media-sources)
    - [Acknowledgments](#acknowledgments)

## E-commerce Applications for Birchlin

### What is E-commerce?

Birchlin operates as a comprehensive e-commerce platform designed to facilitate secure online transactions for outdoor gear and equipment. The platform enables digital commerce through integrated payment processing, product management, and order fulfillment system.

### Business Model for Birchlin

Birchlin follows a B2C (Business to Consumer) e-commerce model, serving individual outdoor enthusiasts who purchase gear for personal use. The platform is designed to handle impulse purchases through streamlined checkout processes while also supporting considered purchases with detailed product information.

### Key Ways to Define E-commerce for Birchlin

#### WHO: Who is the customer?

**Primary Customer Base - B2C (Business to Consumer):**
- Hiking and backpacking enthusiasts seeking reliable trail gear
- Camping families looking for quality outdoor equipment
- Adventure travelers requiring portable and durable gear
- Outdoor professionals needing dependable field equipment

**Customer Behavior:**
- **Impulse purchases:** Quick checkout for accessories and consumables
- **Considered purchases:** Detailed research for major gear investments like shelters and sleeping systems

#### WHAT: What are they buying?

Birchlin specializes in outdoor gear across multiple categories:

**Product Categories:**
- **Shelter:** Tents primarily at the moment
- **Sleeping Systems:** Sleeping bags, pads, and camp comfort items
- **Cooking Equipment:** Stoves, cookware, and food preparation tools
- **Power & Lighting:** Portable chargers, headlamps, and illumination
- **Navigation:** GPS devices, compasses, and route-finding tools
- **Safety Equipment:** First aid, emergency gear, and protective equipment
- **Bags & Packs:** Backpacks, day packs, and gear organization
- **Chairs & Furniture:** Portable seating and camp furniture

**Database Features Required:**
- Product specifications with detailed technical information
- Customer reviews and ratings system

#### HOW: How will they pay?

**Payment Model:**
- **Single Payment:** Standard 
- **Secure Processing:** Stripe integration for reliable payment handling
- **Multiple Payment Method:** Credit card

## UX & Agile Development

The complete User Experience design process and Agile methodology implementation are documented in our [Agile Documentation](AGILE.md).

## User Experience Design

Birchlin's user experience centers on the principle that purchasing outdoor gear should be as straightforward as using it in the field. The interface prioritizes clear product information, efficient navigation, and minimal friction in the purchasing process.

**Design Principles:**
- **Clarity:** Essential product information is immediately visible
- **Efficiency:** Streamlined navigation between categories and products
- **Trust:** Authentic reviews and detailed specifications build confidence
- **Accessibility:** Responsive design ensures usability across all devices

## Agile Methodology

This project was developed following Agile principles with iterative releases and continuous feedback integration. The project utilized GitHub Projects with a Kanban board structure to track progress through user stories and development tasks.

[Link to Kanban board](https://github.com/users/jtraveler/projects/5/)

**Sprint Structure:**
- 2-week sprints focusing on specific feature sets
- Setting priorities
- Regular retrospectives with having a customer mindset to improve development processes

## Development Tools & Architecture

Birchlin leverages modern web development technologies to create a robust, scalable e-commerce platform:

**Backend Architecture:**
- **Django Framework:** Provides secure, scalable web application foundation
- **PostgreSQL Database:** Ensures reliable data storage and complex query support
- **AWS S3:** Handles static file storage and media management

**Frontend Technologies:**
- **Bootstrap 5:** Responsive framework for consistent UI components
- **Custom CSS:** Tailored styling for outdoor gear presentation
- **JavaScript:** Enhanced interactivity and dynamic content loading

## Design System

The design system reflects the rugged reliability of outdoor gear while maintaining modern usability standards.

### Homepage Overview

The homepage creates an immediate connection with outdoor adventure through:

**Hero Section:**
- Full-width video background showcasing an outdoor activity
- Clear value proposition emphasizing gear reliability
- Direct call-to-action leading to product catalog

**Featured Content:**
- Category highlights with representative product imagery
- Latest gear arrivals and seasonal recommendations
- Customer testimonials and gear success stories

**Navigation:**
- Intuitive category-based menu structure
- Quick access to account features and shopping cart
- Search functionality that displays the user's search term on the results page

### Product Catalog Overview

The product catalog prioritizes information clarity and discovery:

**Category Structure:**
- Category indicators for quick identification
- Advanced filtering options for specific requirements

**Product Display:**
- Grid layout optimizing product imagery and key details
- Hover effects revealing additional product information
- Sort functionality by price, rating, and popularity

**Product Detail Integration:**
- Seamless transition from catalog to detailed product pages
- Breadcrumb navigation maintaining context

## Color Palette

The color scheme is super simplistic with just three tones:

![Color Palette](static/images/readme/color-palette.jpg)

**Primary Colors:**
- **Dark Grey:** `#1a1a1a`
- **Medium Grey:** `#212121`
- **White:** `#ffffff`


## Typography

Typography selection emphasizes readability across various contexts:

**Primary Font:** [Inter](https://fonts.google.com/specimen/Inter)
- Clean, modern typeface ensuring legibility at all sizes
- Wide character set supporting international customers
- Multiple weights available for hierarchical content


## Icons & Visual Elements

Visual elements maintain consistency while conveying outdoor themes:

**Icon Library:** [Font Awesome Icons](https://fontawesome.com/)
- Comprehensive set covering all e-commerce functions
- Consistent style matching the overall design system
- Scalable vector format ensuring crisp display

![Icons](static/images/readme/icons.jpg)

## Technologies Used

### Wireframes

Wireframes established the foundational layout and user flow:



<br>
<details>
   <br>
   <summary>Homepage Wireframe - Desktop</summary>
   <img src="static/images/readme/wireframes/homepage.png" style="display: block; margin: auto;" alt="PostgreSQL creation step1">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Homepage Wireframe - Mobile</summary>
   <img src="static/images/readme/wireframes/homepage-mobile.png" style="display: block; margin: auto;" alt="PostgreSQL creation step1">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Product Catalog - Desktop</summary>
   <img src="static/images/readme/wireframes/products.png" style="display: block; margin: auto;" alt="Product Catalog - Desktop">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Product Catalog - Mobile</summary>
   <img src="static/images/readme/wireframes/products-mobile.png" style="display: block; margin: auto;" alt="Product Catalog - Mobile">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Product Detail - Desktop</summary>
   <img src="static/images/readme/wireframes/product-detail.png" style="display: block; margin: auto;" alt="Product Detail - Desktop">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Product Detail - Mobile</summary>
   <img src="static/images/readme/wireframes/product-detail-mobile.png" style="display: block; margin: auto;" alt="Product Detail - Mobile">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Checkout - Desktop</summary>
   <img src="static/images/readme/wireframes/checkout.png" style="display: block; margin: auto;" alt="Checkout - Desktop">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Checkout - Mobile</summary>
   <img src="static/images/readme/wireframes/checkout-mobile.png" style="display: block; margin: auto;" alt="Checkout - Mobile">
   <br>
</details>
<br>
   

<br>
<details>
   <br>
   <summary>General Info Page - Desktop</summary>
   <img src="static/images/readme/wireframes/general-text.png" style="display: block; margin: auto;" alt="General Info Page - Desktop">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>General Info Page - Mobile</summary>
   <img src="static/images/readme/wireframes/general-text-mobile.png" style="display: block; margin: auto;" alt="General Info Page - Mobile">
   <br>
</details>
<br>


<br>
<details>
   <br>
   <summary>Contact Wireframe - Desktop</summary>
   <img src="static/images/readme/wireframes/contact.png" style="display: block; margin: auto;" alt="Contact Wireframe - Desktop">
   <br>
</details>
<br>

<br>
<details>
   <br>
   <summary>Contact Wireframe - Mobile</summary>
   <img src="static/images/readme/wireframes/contact-mobile.png" style="display: block; margin: auto;" alt="Contact Wireframe - Mobile">
   <br>
</details>
<br>



### Favicon

The favicon incorporates outdoor themes while maintaining brand recognition:

![Favicon](static/images/readme/favicon.png)

### Languages

**Backend Languages:**
- [Python](https://www.python.org/) - Core application logic and data processing
- [SQL](https://www.postgresql.org/) - Database queries and data management

**Frontend Languages:**
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - Semantic markup and content structure
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Styling and responsive design
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Interactive functionality and API integration

### Frameworks & Software

**Core Framework:**
- [Django 3.2.25](https://www.djangoproject.com/) - Secure, scalable web framework
- [Bootstrap 5](https://getbootstrap.com/) - Responsive UI framework

**Development Tools:**
- [VS Code](https://code.visualstudio.com/) - Primary development environment
- [GitHub](https://github.com/) - Version control and collaboration
- [Heroku](https://www.heroku.com/) - Cloud deployment platform

**Design Tools:**
- [Balsamiq](https://balsamiq.com/) - Wireframe creation
- [Figma](https://www.figma.com/) - UI design and prototyping
- [Adobe Photoshop](https://https://www.adobe.com/products/photoshop.html/) - Custom graphic creation
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) - Adjusting icons

### Libraries and Modules

<details>
<summary>Python Dependencies</summary>

```
asgiref==3.8.1
boto3==1.37.38
botocore==1.37.38
certifi==2025.7.14
cffi==1.17.1
charset-normalizer==3.4.2
crispy-bootstrap4==2022.1
cryptography==45.0.5
defusedxml==0.7.1
dj-database-url==0.5.0
Django==3.2.25
django-admin-sortable2==1.0.4
django-allauth==0.50.0
django-cleanup==8.0.0
django-countries==7.2.1
django-crispy-forms==1.14.0
django-imagekit==5.0.0
django-storages==1.14.6
flake8==7.1.2
gunicorn==23.0.0
idna==3.10
jmespath==1.0.1
mccabe==0.7.0
oauthlib==3.3.1
packaging==25.0
pilkit==3.0
pillow==10.4.0
psycopg2==2.9.10
pycodestyle==2.12.1
pycparser==2.22
pyflakes==3.2.0
PyJWT==2.9.0
python-dateutil==2.9.0.post0
python3-openid==3.2.0
pytz==2025.2
requests==2.32.4
requests-oauthlib==2.0.0
s3transfer==0.11.5
six==1.17.0
sqlparse==0.5.3
stripe==12.3.0
typing-extensions==4.13.2
urllib3==1.26.20
whitenoise==6.7.0
```

</details>

### AWS Integration

Amazon Web Services provides scalable infrastructure for media and static file management:

**S3 Configuration:**
- Static file hosting for CSS, JavaScript, and images
- Media file storage for product images and user uploads
- CDN integration for improved global performance


### Email Services

Email functionality supports customer communication and marketing:

**Gmail SMTP Integration:**
- Order confirmation emails
- Password reset functionality
- Customer service communications

### The Structure Plane - Database

#### Database Design

The database schema supports comprehensive e-commerce functionality:

![ERD Diagram](static/images/readme/erd-diagram.png)

**Core Models:**
- **User:** Extended Django user model with profile information
- **Product:** Comprehensive product information with categories
- **Order:** Order management with line items and status tracking
- **Category:** Hierarchical product categorization
- **Review:** Customer feedback and rating system

#### Entity Relationships

**User-Related Relationships:**
- User → Profile (One-to-One)
- User → Order (One-to-Many)
- User → Review (One-to-Many)
- User → Wishlist (One-to-Many)

**Product-Related Relationships:**
- Category → Product (One-to-Many)
- Product → Review (One-to-Many)
- Product → OrderLineItem (One-to-Many)
- Product → WishlistItem (One-to-Many)

**Order Processing:**
- Order → OrderLineItem (One-to-Many)
- OrderLineItem → Product (Many-to-One)

### Version Control

**Git Workflow:**
- Feature branch development for all new functionality
- Pull request reviews ensuring code quality
- Semantic commit messages for clear history tracking

**GitHub Integration:**
- Issues tracking for bug reports and feature requests
- Project boards for sprint planning and progress tracking
- Automated deployments through GitHub Actions

## E-commerce Business Model

Birchlin implements a comprehensive digital marketing strategy supporting sustainable business growth:

### Search Engine Optimization (SEO)

**Technical SEO:**
- Semantic HTML structure with proper heading hierarchy
- Meta descriptions optimized for outdoor gear keywords
- XML sitemap generation for search engine crawling
- Mobile-first responsive design for Core Web Vitals

**Content Strategy:**
- Product descriptions incorporating long-tail keywords
- Category pages optimized for gear-specific searches
- Blog content covering outdoor topics and gear guides

**Performance Optimization:**
- Image compression and lazy loading for faster page speeds
- CDN implementation for global content delivery
- Database query optimization for improved response times


### Future Marketing Strategies

**Influencer Partnerships:**
- Collaborations with outdoor athletes and adventure content creators
- Product seeding programs for authentic gear testing
- Ambassador programs for long-term brand relationships

**Affiliate Marketing:**
- Partnerships with outdoor blogs and review websites
- Commission structure encouraging authentic product recommendations
- Tracking systems for attribution and performance monitoring





## Features

### Existing Features

#### Navigation & Header

**Responsive Navigation:**
- Collapsible mobile menu with smooth animations
- Persistent shopping cart icon with live item count
- User account dropdown with quick access to profile features

#### Hero Video Section

**Dynamic Hero Content:**
- Full-width background video showcasing outdoor activities
- Overlay content with compelling value propositions
- Call-to-action buttons directing to featured categories
- Automatic video optimization for different connection speeds

#### Product Catalog

**Advanced Product Display:**
- Grid layout optimizing product imagery
- Pagination with 20 products per page for improved performance

**Advanced Sorting & Filtering:**
- Sort by customer rating (high to low, low to high)
- Sort by price, name, category, and rating

**Product Information Display:**
- Star rating display with visual rating indicators
- Customer average rating
- Category and price information

#### Product Detail Pages

**Enhanced Gallery System:**
- Swiper.js image carousel with smooth scrolling and easing effects
- Thumbnail navigation panel below main gallery
- Gallery progress indicator showing current image position
- Touch gestures and keyboard navigation support
- Mobile-optimized gallery experience with responsive design

**Comprehensive Product Information:**
- High-resolution image galleries with multiple product angles

**Rating & Review System:**
- 5-star rating display with aggregate customer scores
- Customer review submission and management system
- Review filtering and sorting options

#### Shopping Cart & Checkout

**Cart Features:**
- Persistent cart across sessions for registered users
- Quantity adjustment

**Streamlined Checkout:**
- Guest checkout option for quick purchases
- Address autocomplete for shipping information
- Order confirmation

#### User Authentication & Profiles

**Account Management:**
- Django Allauth integration for secure authentication
- Email verification for account security
- Password reset functionality with secure token generation

**User Profiles:**
- Order history
- Shipping address management
- Wishlist access and management

#### Wishlist Functionality

**Personal Wishlist:**
- Add products from catalog or detail pages
- Move to cart functionality for easy purchasing


#### Search Capabilities

**Informative Search:**
- Full-text search across product names and descriptions
- Search result highlighting for query terms

#### Contact

**Form Validation:**
- Real-time validation for all form inputs
- Clear error messaging for failed validations
- Success confirmations for form submissions


#### Admin Management

**Enhanced Product Management:**
- Custom admin interface for comprehensive product management
- Multiple image upload
- Sortable product image galleries with drag-and-drop reordering
- Primary image selection for product listings
- Image alt text management for accessibility compliance
- Automatic image cleanup when products or images are deleted

**Advanced Admin Features:**
- Basic search with advanced filtering (by SKU, name, description, category)
- Improved pagination controls (50 items per page with "show all" option)
- Order management dashboard

**Image Processing & Optimization:**
- Automatic thumbnail generation using django-imagekit
- Multiple image sizes optimized for different display contexts
- Smart image resizing and compression algorithms
- Placeholder image fallback system for products without images
- Image optimization to try to reduce payload

#### Performance Optimizations

**Database Performance:**
- Optimized database queries using select_related and prefetch_related
- Efficient pagination reducing server response time

**Image & Asset Optimization:**
- Compressed image delivery with automatic optimization
- WebP format support for modern browsers
- CDN integration for global content delivery
- Responsive image sizing for different screen resolutions
- Lazy loading for below-fold content improving initial page load

**Frontend Performance:**
- Deferred loading of non-critical CSS and JavaScript
- Optimized asset bundling and minification
- Browser caching strategies for static assets
- Reduced render-blocking resources achieving 800ms savings

#### Responsive Design

**Mobile Optimization:**
- Touch-friendly interface elements optimized for mobile interaction
- Optimized image sizes for mobile bandwidth conservation
- Simplified navigation for small screens
- Mobile-specific checkout flow with streamlined steps
- Swipe gestures for product galleries

**Cross-Device Consistency:**
- Consistent functionality across all device types and screen sizes
- Responsive images adapting automatically to screen dimensions
- Performance optimization for varying connection speeds
- Seamless experience transition between desktop and mobile

### Future Features

**Planned Enhancements:**
- Augmented reality product visualization for gear fitting
- Advanced recommendation engine based on outdoor activities and preferences
- Subscription service for consumable outdoor products
- Integration with fitness and outdoor activity tracking apps
- Virtual outdoor gear consultation services with expert advisors
- Community forum for gear discussions and trip planning
- Advanced inventory management with automated reorder points
- Chatbot integration for instant customer support
- Seasonal product recommendations based on user location
- Social media integration for user-generated content
- Email marketing automation with personalized campaigns
- Multi-language support for international customers
- Advanced analytics dashboard for sales and customer insights
- Review history and management tools
- Tracking information
- Up and down voting of rating if it was helpful or not
- Price drop notifications for wishlisted items
- Wishlist sharing functionality for gift recommendations
- Wishlist organization and categorization
- Spam protection through reCAPTCHA integration for the contact forms



## Testing

### HTML Validation

All HTML templates validated using the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with HTML5 standards. The validation was performed on the following key pages:

- **Homepage** (`/`) - Intro with video
- **Products** (`/products/`) - Product list 
- **Product Detail** (`/products/181/`) - Product details and overview
- **Shopping Bag** (`/bag/`) - Shopping bag with customer selected product items
- **Checkout** (`/checkout/`) - Checkout page with form
- **Order Confirmation** (`/checkout_success/CAED7C9034D34F13A7FF26B3E3EE1007`) - Order confirmation with order overview and next steps
- **Profile** (`/profile/`) - User's profile with order history
- **Wishlist** (`/products/wishlist/`) - The user's saved items that they are interested in
- **General Text** (`/about/`) - Gneral text pages such as About, Privacy Policy etc.



<details>
<summary>HTML Validation Results</summary>

| Page | Status | Issues |
|------|--------|--------|
| Homepage | ✅ Pass | 0 errors |
| Product Catalog | ✅ Pass | 0 errors |
| Product Detail | ✅ Pass | 0 errors |
| Shopping Cart | ✅ Pass | 0 errors |
| Checkout | ✅ Pass | 0 errors |
| User Profile | ✅ Pass | 0 errors |
| Contact | ✅ Pass | 0 errors |

</details>

### CSS Validation

CSS validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/):

![CSS Validation](static/images/readme/css-validation.png)

### Accessibility Testing

Accessibility compliance verified through multiple testing methods:

**WAVE Testing Results:**
- Zero accessibility errors across main pages
- Proper heading hierarchy implementation
- Sufficient color contrast ratios maintained
- Alt text provided for all meaningful images

### Wave Validation

<details>
<summary>WAVE Validation Results</summary>

![Homepage WAVE](static/images/readme/wave-homepage.png)
![Catalog WAVE](static/images/readme/wave-catalog.png)
![Product WAVE](static/images/readme/wave-product.png)

</details>

### Lighthouse Performance


**Key Performance Optimizations Implemented:**

1. **Database Query Optimization:**
   ```python
   # Optimized product queries with select_related and prefetch_related
   products = Product.objects.select_related('category').prefetch_related(
       'reviews', 'images'
   ).all()
   ```

2. **Pagination Implementation:**
   - Added 20 products per page pagination
   - Reduced initial page load times
   - Improved server response from 19.96s to 2.8s in most cases

3. **Image Optimization:**
   - Implemented lazy loading for below-the-fold images
   - Removed lazy loading from above-the-fold images (first 4-6 products)
   - Added proper image sizing and thumbnail generation

4. **Render-Blocking Resource Optimization:**
   - Deferred non-critical CSS and JavaScript loading
   - Achieved 800ms savings in render blocking
   - Improved Largest Contentful Paint metrics

5. **CDN and Caching:**
   - AWS S3 integration with CloudFront CDN
   - Browser caching for static assets
   - Optimized asset delivery globally

**Mobile First Analysis:**

The following Lighthouse testing is only for the mobile versions of the pages as the tests were done with a mobile-first approach.



Home

![Home](static/images/readme/lighthouse/home.jpg)

<br>
Products

![Home](static/images/readme/lighthouse/products.jpg)

<br>
Product Detail

![Home](static/images/readme/lighthouse/product_detail.jpg)

<br>
Shopping Bag

![Home](static/images/readme/lighthouse/shopping_bag.jpg)

<br>
Checkout

![Home](static/images/readme/lighthouse/checkout.jpg)


<br>
Order Confirmation

![Home](static/images/readme/lighthouse/order_confirmation.jpg)


<br>
Profile

![Home](static/images/readme/lighthouse/profile.jpg)


<br>
Wishlist

![Home](static/images/readme/lighthouse/wishlist.jpg)


<br>
Genral Text Pages

![Home](static/images/readme/lighthouse/general_text.jpg)

### JavaScript Validation

JavaScript code validated using [JSHint](https://jshint.com/):

<details>
<summary>JavaScript Validation Results</summary>

| File | Status | Warnings |
|------|--------|----------|
| main.js | ✅ Pass | 0 warnings |
| cart.js | ✅ Pass | 0 warnings |
| product.js | ✅ Pass | 0 warnings |
| checkout.js | ✅ Pass | 0 warnings |

</details>

### Python Code Validation

Python code validated using [PEP8 CI Linter](https://pep8ci.herokuapp.com/):

<details>
<summary>Python Validation Results</summary>

| File | Status | Issues |
|------|--------|--------|
| views.py | ✅ Pass | 0 errors |
| models.py | ✅ Pass | 0 errors |
| forms.py | ✅ Pass | 0 errors |
| urls.py | ✅ Pass | 0 errors |
| settings.py | ✅ Pass | 0 errors |

</details>

### Device Testing

Testing completed across multiple devices and screen sizes:

**Mobile Devices:**
- iPhone 12/13/14 (Safari, Chrome)
- Samsung Galaxy S21/S22 (Chrome, Samsung Browser)
- Google Pixel 6/7 (Chrome)

**Tablets:**
- iPad Air/Pro (Safari, Chrome)
- Samsung Galaxy Tab (Chrome)

**Desktop/Laptop:**
- MacBook Pro 13"/15" (Safari, Chrome, Firefox)
- Windows 10/11 (Chrome, Edge, Firefox)
- Linux Ubuntu (Firefox, Chrome)

### Browser Compatibility

<details>
<summary>Browser Testing Results</summary>

| Browser | Version | Status | Notes |
|---------|---------|--------|--------|
| Chrome | 119+ | ✅ Full | All features working |
| Firefox | 118+ | ✅ Full | All features working |
| Safari | 16+ | ✅ Full | All features working |
| Edge | 119+ | ✅ Full | All features working |

</details>

### Manual Testing

<details>
<summary>Manual Testing Scenarios</summary>

| Feature | Test Case | Expected Result | Status |
|---------|-----------|-----------------|--------|
| User Registration | Create new account | Account created, verification email sent | ✅ Pass |
| User Login | Login with credentials | Successful authentication, redirect to profile | ✅ Pass |
| Product Search | Search for "tent" | Relevant products displayed | ✅ Pass |
| Add to Cart | Add product to cart | Cart count updates, product visible in cart | ✅ Pass |
| Checkout Process | Complete purchase | Order confirmation, payment processed | ✅ Pass |
| Contact Form | Submit inquiry | Form submitted, confirmation message shown | ✅ Pass |
| Responsive Design | Test on mobile | Layout adapts correctly | ✅ Pass |

</details>

### User Story Testing

User stories validated against acceptance criteria:

<details>
<summary>User Story Test Results</summary>

| User Story | Acceptance Criteria | Test Result |
|------------|-------------------|-------------|
| View All Products | Products display with name, image, price | ✅ Pass |
| Filter by Category | Category filtering works correctly | ✅ Pass |
| Product Details | Detailed information visible | ✅ Pass |
| Add to Cart | Products add to cart successfully | ✅ Pass |
| Secure Checkout | Payment processing works | ✅ Pass |
| User Authentication | Login/logout functions properly | ✅ Pass |
| Search Products | Search returns relevant results | ✅ Pass |
| Admin Management | Order management functions work | ✅ Pass |

</details>

## Deployment

### Heroku Deployment

The application is deployed on Heroku with the following configuration:

**Prerequisites:**
1. Heroku account creation
2. Git repository with project code
3. Requirements.txt file with dependencies
4. Procfile for application startup

**Deployment Steps:**

<details>
<summary>Heroku Deployment Process</summary>

1. **Create Heroku Application:**
   ```bash
   heroku create birchlin-outdoor-gear
   ```

2. **Configure Environment Variables:**
   - Set DATABASE_URL for PostgreSQL
   - Configure AWS credentials for S3
   - Add Stripe API keys
   - Set SECRET_KEY for Django

3. **Deploy Application:**
   ```bash
   git push heroku main
   ```

4. **Run Database Migrations:**
   ```bash
   heroku run python manage.py migrate
   ```

5. **Create Superuser:**
   ```bash
   heroku run python manage.py createsuperuser
   ```

</details>

### AWS Configuration

Static and media files hosted on Amazon S3:

**S3 Bucket Setup:**
- Create bucket with public read access
- Configure CORS for cross-origin requests
- Set up bucket policy for static file access

**IAM Configuration:**
- Create dedicated user for Django application
- Assign minimal required permissions
- Generate access keys for application use

### Local Development

**Environment Setup:**

<details>
<summary>Local Development Configuration</summary>

1. **Clone Repository:**
   ```bash
   git clone https://github.com/username/birchlin-project.git
   cd birchlin-project
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create `.env` file with:
   ```
   SECRET_KEY=your-secret-key
   DATABASE_URL=your-database-url
   STRIPE_PUBLIC_KEY=your-stripe-public-key
   STRIPE_SECRET_KEY=your-stripe-secret-key
   AWS_ACCESS_KEY_ID=your-aws-access-key
   AWS_SECRET_ACCESS_KEY=your-aws-secret-key
   ```

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```

</details>

### Forking the Repository

To fork this repository for your own development:

1. Navigate to the [GitHub repository](https://github.com/username/birchlin-project)
2. Click the "Fork" button in the top-right corner
3. Select your GitHub account as the destination
4. Clone your forked repository locally

### Cloning the Repository

To clone this repository:

```bash
git clone https://github.com/username/birchlin-project.git
cd birchlin-project
```

### Environment Setup

**Required Environment Variables:**

<details>
<summary>Environment Configuration</summary>

```bash
# Django Configuration
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,localhost

# Database
DATABASE_URL=postgres://user:password@host:port/database

# Stripe Integration
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WH_SECRET=whsec_...

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=your-region

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

</details>

## Credits

### Code References

**Core Framework:**
- [Code Institute - Boutique Ado Walkthrough](https://codeinstitute.net/) - Foundation Django e-commerce implementation
- [Code Institute - Testing our first webhook](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+9/courseware/eb05f06e62c64ac89823cc956fcd8191/77226a2d0f664a0db7ce852e076e5d44/?child=first) - Stripe webhook testing and integration
- [Django Documentation](https://docs.djangoproject.com/) - Web framework implementation
- [Bootstrap 5](https://getbootstrap.com/) - Responsive UI components
- [Stripe Documentation](https://stripe.com/docs) - Payment processing integration

**Image Management & Gallery Implementation:**
- [Django Multiple Images Upload](https://djangocentral.com/uploading-images-with-django/) - Django Central
- [Ajax Image Upload Tutorial](https://codingwithmitch.com/blog/django-multiple-images-upload-ajax/) - CodingWithMitch
- [Django File/Image Uploads Best Practices](https://realpython.com/django-file-image-uploads/) - Real Python
- [Creating Product Gallery with Django and Swiper](https://testdriven.io/blog/django-product-gallery/) - TestDriven.io
- [Modern Image Galleries in Django](https://www.codingforentrepreneurs.com/blog/django-image-galleries/) - Coding For Entrepreneurs

**Footer**
- [mdbootstrap.com](https://mdbootstrap.com/docs/standard/navigation/footer/examples-and-customization/)

**Performance & Optimization:**
- [Image Processing in Django with ImageKit](https://simpleisbetterthancomplex.com/tutorial/2019/03/20/django-image-kit.html) - SimpleIsBetterThanComplex
- [Optimize Images in Django](https://djangostars.com/blog/optimize-images-in-django/) - Django Stars
- [Optimizing Django Image Handling](https://django-performance.com/optimizing-images/) - Django Performance
- [Django Data Migrations Done Right](https://realpython.com/data-migrations/) - Real Python

**UI Enhancement & Admin Customization:**
- [Django Drag and Drop File Upload](https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial) - LearnDjango
- [Dropzone.js with Django Forms](https://dev.to/coderasha/django-dropzonejs-multiple-file-upload-2a4f) - Dev.to @coderasha
- [Advanced Django Admin Customization](https://www.feldroy.com/blog/django-admin-customization) - Two Scoops of Django
- [Django Admin Sortable2](https://django-admin-sortable2.readthedocs.io/) - Official Documentation

**Third-Party Integrations:**
- [Django Allauth](https://django-allauth.readthedocs.io/) - Authentication system
- [Swiper.js Documentation](https://swiperjs.com/) - Image carousel functionality
- [AWS S3](https://aws.amazon.com/s3/) - Static file storage
- [django-cleanup](https://github.com/un1t/django-cleanup) - Automatic file cleanup
- [django-imagekit](https://github.com/matthewwithanm/django-imagekit) - Image processing

**Video Learning Resources:**
- [Django E-commerce Tutorial Series](https://www.youtube.com/watch?v=UmljXZIypDc&list=PLOLrQ9Pn6caxY4Q1U9RjO1bulQp5NDYS_) - Very Academy
- [Building an E-commerce Product Gallery](https://justdjango.com/blog/django-ecommerce-product-gallery) - JustDjango

### Media Sources

**Photography:**
- [Unsplash](https://unsplash.com/) - Product and outdoor lifestyle photography
- [Pexels](https://www.pexels.com/) - Additional stock photography
- [Pixabay](https://pixabay.com/) - Icons and graphic elements

**Video Content:**
- [From USer Taryn Elliott on Pexels.com](https://www.pexels.com/video/a-woman-sitting-on-a-rock-with-a-coffee-pot-4909395/) - Background video content

### Acknowledgments

**Development Support:**
- **Mentor Spencer Barriball** - Technical guidance, coaching and code review
- **Cohort Kay Welfare** - Technical guidance, coaching and project driven support
- **Code Institute** - Educational resources and project guidance
- **Django Community** - Documentation and community support

**Testing Contributors:**
- Beta testers who provided valuable feedback on user experience
- Accessibility consultants who verified compliance standards
- Performance optimization specialists

**Special Recognition:**
- Outdoor gear enthusiasts who provided domain expertise
- UX/UI designers who contributed to the design system
- Content creators who developed product descriptions and guides

---

**This project is for educational purposes only and demonstrates a comprehensive e-commerce implementation using modern web technologies.**

For questions or collaboration opportunities, please contact: [info@birchlin.com](mailto:info@birchlin.com)

**Live Site:** [https://mj-project5-aec364964bcd.herokuapp.com/](https://mj-project5-aec364964bcd.herokuapp.com/)  
**Repository:** [https://github.com/jtraveler/project-5](https://github.com/jtraveler/project-5)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Status

**Current Version:** 1.0.0  
**Status:** Production Ready  
**Last Updated:** 27, August 2025
