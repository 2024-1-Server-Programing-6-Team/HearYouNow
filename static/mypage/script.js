document.querySelectorAll('.side-nav-bar a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('href').replace('#', '');
        document.querySelector(`.${sectionId}-container`).scrollIntoView({ behavior: 'smooth' });
    });
});
