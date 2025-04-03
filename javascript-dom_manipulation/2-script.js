const element = document.getElementById('red_header');
element.addEventListener('click', (event) => {
    const header = document.querySelector('header');
    header.classList.add('red');
});
