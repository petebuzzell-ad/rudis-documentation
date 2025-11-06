// Component Loader: Dynamically loads header.html and footer.html
// Works for root-level pages (GitHub Pages serves from root)
// Also handles basic password protection

(function() {
    // ============================================
    // Basic Password Protection
    // ============================================
    const PASSWORD = 'arcadia';
    const AUTH_KEY = 'rudis_docs_authenticated';
    
    // Hide content immediately to prevent flash
    document.body.style.visibility = 'hidden';
    document.body.style.overflow = 'hidden';
    
    // Check if already authenticated
    function isAuthenticated() {
        return sessionStorage.getItem(AUTH_KEY) === 'true';
    }
    
    // Set authenticated state
    function setAuthenticated() {
        sessionStorage.setItem(AUTH_KEY, 'true');
    }
    
    // Show password prompt
    function showPasswordPrompt() {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.id = 'auth-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #1a1a1a;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        `;
        
        // Create prompt container
        const container = document.createElement('div');
        container.style.cssText = `
            background: #2a2a2a;
            padding: 2rem 3rem;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 400px;
            width: 90%;
        `;
        
        // Title
        const title = document.createElement('h2');
        title.textContent = 'Protected Documentation';
        title.style.cssText = `
            color: #fff;
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
            font-weight: 600;
        `;
        
        // Description
        const desc = document.createElement('p');
        desc.textContent = 'Please enter the password to access this documentation.';
        desc.style.cssText = `
            color: #aaa;
            margin: 0 0 1.5rem 0;
            font-size: 0.9rem;
        `;
        
        // Form to contain password input (fixes browser warning)
        const form = document.createElement('form');
        form.style.cssText = 'width: 100%;';
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            checkPassword();
        });
        
        // Hidden username field for accessibility (browser requirement)
        const usernameInput = document.createElement('input');
        usernameInput.type = 'text';
        usernameInput.name = 'username';
        usernameInput.autocomplete = 'username';
        usernameInput.style.cssText = 'position: absolute; left: -9999px; width: 1px; height: 1px;';
        usernameInput.tabIndex = -1;
        usernameInput.setAttribute('aria-hidden', 'true');
        
        // Password input
        const input = document.createElement('input');
        input.type = 'password';
        input.placeholder = 'Password';
        input.id = 'auth-password-input';
        input.name = 'password';
        input.autocomplete = 'current-password';
        input.style.cssText = `
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border: 1px solid #444;
            border-radius: 4px;
            background: #1a1a1a;
            color: #fff;
            font-size: 1rem;
            box-sizing: border-box;
        `;
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                checkPassword();
            }
        });
        
        // Error message
        const error = document.createElement('div');
        error.id = 'auth-error';
        error.style.cssText = `
            color: #ff6b6b;
            margin-bottom: 1rem;
            min-height: 1.2rem;
            font-size: 0.85rem;
            display: none;
        `;
        
        // Submit button
        const button = document.createElement('button');
        button.type = 'submit';
        button.textContent = 'Access Documentation';
        button.style.cssText = `
            width: 100%;
            padding: 0.75rem;
            background: #2d5016;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        `;
        button.addEventListener('mouseenter', function() {
            button.style.background = '#3a6a1e';
        });
        button.addEventListener('mouseleave', function() {
            button.style.background = '#2d5016';
        });
        
        // Assemble form
        form.appendChild(usernameInput);
        form.appendChild(input);
        form.appendChild(error);
        form.appendChild(button);
        
        // Assemble container
        container.appendChild(title);
        container.appendChild(desc);
        container.appendChild(form);
        overlay.appendChild(container);
        document.body.appendChild(overlay);
        
        // Focus input
        setTimeout(() => input.focus(), 100);
        
        // Check password function
        function checkPassword() {
            const password = input.value.trim();
            if (password === PASSWORD) {
                setAuthenticated();
                overlay.remove();
                document.body.style.visibility = 'visible';
                document.body.style.overflow = '';
                // Continue with component loading
                loadComponents();
            } else {
                error.textContent = 'Incorrect password. Please try again.';
                error.style.display = 'block';
                input.value = '';
                input.focus();
            }
        }
    }
    
    // ============================================
    // Component Loading
    // ============================================
    function loadComponents() {
        // Load header
        fetch('header.html')
            .then(response => response.text())
            .then(html => {
                document.getElementById('header-container').innerHTML = html;
                initializeHeader();
            })
            .catch(error => console.error('Error loading header:', error));
        
        // Load footer
        fetch('footer.html')
            .then(response => response.text())
            .then(html => {
                document.getElementById('footer-container').innerHTML = html;
            })
            .catch(error => console.error('Error loading footer:', error));
    }
    
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
    
    // Initialize: Check auth first, then load components
    if (!isAuthenticated()) {
        showPasswordPrompt();
    } else {
        document.body.style.visibility = 'visible';
        document.body.style.overflow = '';
        loadComponents();
    }
})();

