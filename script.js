document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scrolling for Navigation
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetSection = document.querySelector(this.getAttribute('href'));
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Initialize Leaflet Map
    var map = L.map('mapid').setView([20.5937, 78.9629], 5); // Centered to India
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
    }).addTo(map);
    L.marker([20.5937, 78.9629]).addTo(map)
        .bindPopup('Our Service Coverage')
        .openPopup();

    // Initialize AOS
    AOS.init();

    // Contact Form Validation
    document.getElementById('contactForm').addEventListener('submit', function(e) {
        const email = document.querySelector('input[name="email"]');
        if (!validateEmail(email.value)) {
            e.preventDefault();
            alert('Please enter a valid email address!');
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Testimonials Carousel
    const carousel = document.querySelector('.testimonial-carousel');
    const prevBtn = document.querySelector('.carousel-control-prev');
    const nextBtn = document.querySelector('.carousel-control-next');
    const testimonials = Array.from(carousel.children);
    const numVisible = 2; // Number of testimonials to show at a time
    let currentIndex = 0;

    function updateCarousel() {
        const offset = -currentIndex * (100 / numVisible) + '%';
        carousel.style.transform = `translateX(${offset})`;
    }

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % Math.ceil(testimonials.length / numVisible);
        updateCarousel();
    });

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + Math.ceil(testimonials.length / numVisible)) % Math.ceil(testimonials.length / numVisible);
        updateCarousel();
    });

    // Initialize carousel
    updateCarousel();
});
