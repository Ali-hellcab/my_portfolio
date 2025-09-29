document.addEventListener('DOMContentLoaded', () => {
    // --- Mobile Navigation Toggle ---
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // --- Theme Toggler (Light/Dark Mode) ---
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Function to apply the currently saved theme
    const applyTheme = () => {
        const savedTheme = localStorage.getItem('theme');
        // If a theme is saved and it's 'light', add the light-mode class
        if (savedTheme === 'light') {
            body.classList.add('light-mode');
        } else {
            // Otherwise, ensure light-mode is removed (for dark mode)
            body.classList.remove('light-mode');
        }
    };

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            // Toggle the .light-mode class on the body
            body.classList.toggle('light-mode');

            // Check if light-mode is now active and save the preference
            if (body.classList.contains('light-mode')) {
                localStorage.setItem('theme', 'light');
            } else {
                localStorage.setItem('theme', 'dark');
            }
        });
    }

    // Apply the saved theme when the page loads
    applyTheme();
});