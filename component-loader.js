// Component Loader: Dynamically loads header.html and footer.html
// Works for both root-level and docs/ subdirectory pages

(function() {
    // Determine the correct path based on current location
    const isDocsPage = window.location.pathname.includes('/docs/');
    const pathPrefix = isDocsPage ? '../' : '';
    
    // Load header
    fetch(pathPrefix + 'header.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('header-container').innerHTML = html;
            initializeHeader();
        })
        .catch(error => console.error('Error loading header:', error));
    
    // Load footer
    fetch(pathPrefix + 'footer.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('footer-container').innerHTML = html;
        })
        .catch(error => console.error('Error loading footer:', error));
    
    // Initialize header functionality (menu toggle, etc.)
    function initializeHeader() {
        const menuToggle = document.getElementById('menu-toggle');
        const headerMenu = document.getElementById('header-menu');
        
        if (menuToggle && headerMenu) {
            menuToggle.addEventListener('click', function() {
                const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
                menuToggle.setAttribute('aria-expanded', !isExpanded);
                headerMenu.classList.toggle('open');
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', function(event) {
                if (!menuToggle.contains(event.target) && !headerMenu.contains(event.target)) {
                    menuToggle.setAttribute('aria-expanded', 'false');
                    headerMenu.classList.remove('open');
                }
            });
        }
    }
})();

