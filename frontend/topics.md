A. HTML
Semantic HTML5:
        What are semantic elements (e.g., <header>, <nav>, <main>, <article>, <section>, <footer>, <aside>) and why are they important? (Accessibility, SEO, readability).
        Examples of using them correctly.
        HTML Structure:
        DOCTYPE, meta tags (charset, viewport, SEO).
        Difference between block, inline, and inline-block elements.        ------
        Forms: input types, attributes (name, id, for), form submission.
        tables in html          ------

Accessibility (a11y):
    Basic ARIA attributes (aria-label, role).       ------
    Keyboard navigation (tabindex).
    Image alt text.
    How to ensure your HTML is accessible.

Web Storage: localStorage, sessionStorage, cookies (differences, use cases, limitations, security).     ------


B. CSS
The Box Model: Deep understanding of content-box vs. border-box and box-sizing.
Selectors & Specificity:
        All types of selectors (element, class, ID, attribute, pseudo-classes, pseudo-elements, combinators).
        How specificity is calculated and why it matters for debugging.
        The role of !important (and why to avoid it).

Layout:
        Flexbox: Comprehensive understanding of all properties (container and item properties). Be ready to build common layouts (nav bars, evenly spaced items, centering).
        CSS Grid: Comprehensive understanding of explicit and implicit grids, grid-template-areas, fr units, minmax(). Be ready to build complex page layouts.
        Positioning: static, relative, absolute, fixed, sticky – understand their behaviors, how they interact with the document flow, and the concept of "stacking contexts."
        float and clear: Understand their historical use and limitations, and how to clear floats (though Flexbox/Grid are preferred now).

Responsive Web Design:
        Media Queries (min-width, max-width, orientation, prefers-color-scheme).
        Viewport units (vw, vh, vmin, vmax).        ----    
        Relative units (em, rem, %).
        Fluid images (max-width: 100%; height: auto;).
        Transitions & Animations: transition vs. @keyframes animations. How to trigger and control them.

CSS Preprocessors (Sass/Less): What they are, benefits (variables, mixins, nesting, functions), and common features.
CSS Custom Properties (Variables): Advantages over preprocessor variables (dynamic, cascading, runtime access).
BEM (Block, Element, Modifier) or other CSS methodologies (OOCSS, SMACSS): Why they are useful for large projects, naming conventions, and maintainability.


C. JavaScript (The Most Crucial Part)
Fundamentals:
        Data types (primitives vs. objects), type coercion (== vs ===).
        var, let, const (scoping, hoisting, temporal dead zone).
        Functions: declarations vs. expressions, arrow functions (this binding).
        this keyword (how it works in different contexts).
        Closures: What they are, how they are formed, and common use cases (data privacy, currying, module pattern).
        Prototypes and Prototypal Inheritance vs. ES6 Classes.
        bind, call, apply.

Asynchronous JavaScript:
        Event Loop: In-depth understanding (Call Stack, Web APIs, Callback Queue, Microtask Queue). How setTimeout(0) works.    ------
        Callbacks: Callback hell, common issues.        ------
        Promises: States (pending, fulfilled, rejected), then, catch, finally, Promise.all, Promise.race, Promise.allSettled.       ------
        Async/Await: How it simplifies asynchronous code, error handling (try...catch).
        Fetch API vs. XMLHttpRequest.

DOM Manipulation:
        Selecting elements (querySelector, getElementById, etc.).
        Creating, appending, removing elements.
        Event Handling: addEventListener, event bubbling, event capturing, event delegation.

        ES6+ Features:
        Destructuring (arrays, objects).
        Spread and Rest operators.
        Template literals.
        Modules (import/export).
        Generators, Iterators (good to know, but less critical than others).
        Optional Chaining (?.) and Nullish Coalescing (??).
        Array Methods: map, filter, reduce, forEach, some, every, find, findIndex, slice, splice. Be ready to explain their differences and provide examples.
        Error Handling: try...catch...finally.


Web Performance: Critical Rendering Path, browser caching, minification, lazy loading.
                Images ,CDNs
    Web performance optimization points and its implementation


Security: XSS attacks 

Bundlers 

Web Accessibility Interview questions (Google it once)Webpack, babel, parcel
Tree shaking during build process

------------------------------------------------------------------------------------------------------------------------------


* basics 
    - HTML
    - CSS
    - JS 
    - React
    - DOM (virtual DOM)
-> Tricky and handson coding excercise 

* frontend design principles
    - atomic
    - container ??? 

* Live / machine coding 
    - Application building
    - DSA 

* Design 
    - Frontend design round ??? 
    - HLD 

* Optimizations 
    - web performance optimizations
    - bundling optimizations  (frontend build)
    - assets managments (images, videos) (bundle size)
    - core web vitals
    - critical rendering path
    - service worker/ web worker
    - CDNs

* Security
    - CORS
    - XSS attacks 