document.addEventListener("DOMContentLoaded", function () {
    const navbarContainer = document.getElementById('navbar-container');
    fetch('navbar.html')
        .then(data => Response.text())
        .then(data => {
            document.getElementById('navbar-placeholder').innerHTML = data;
        });
});


document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll('.nav-link');
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath.includes(linkPath)) {
            navLinks.forEach(item => item.classList.remove('active'));
            link.classList.add('active');
        }
    });
});
