// Component Loader: Dynamically loads header.html and footer.html
// Works for root-level pages and subdirectories (GitHub Pages serves from root)

(function() {
    // Determine the correct path based on current location
    const pathSegments = window.location.pathname.split('/').filter(Boolean);
    // Remove the HTML filename to get directory depth
    const directoryDepth = pathSegments.length - 1;
    // Build path prefix based on depth (0 = root, 1 = ../, 2 = ../../, etc.)
    const pathPrefix = directoryDepth > 0 ? '../'.repeat(directoryDepth) : '';
    
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
            menuToggle.addEventListener('click', function(e) {
                e.stopPropagation();
                const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
                const newExpanded = !isExpanded;
                menuToggle.setAttribute('aria-expanded', newExpanded);
                
                if (newExpanded) {
                    headerMenu.classList.add('show');
                    menuToggle.classList.add('active');
                } else {
                    headerMenu.classList.remove('show');
                    menuToggle.classList.remove('active');
                }
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', function(event) {
                if (menuToggle && headerMenu && 
                    !menuToggle.contains(event.target) && 
                    !headerMenu.contains(event.target)) {
                    menuToggle.setAttribute('aria-expanded', 'false');
                    headerMenu.classList.remove('show');
                    menuToggle.classList.remove('active');
                }
            });
            
            // Close menu on Escape key
            document.addEventListener('keydown', function(event) {
                if (event.key === 'Escape' && headerMenu.classList.contains('show')) {
                    menuToggle.setAttribute('aria-expanded', 'false');
                    headerMenu.classList.remove('show');
                    menuToggle.classList.remove('active');
                }
            });
        }
    }
})();

