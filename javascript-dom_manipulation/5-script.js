const updateHeader = document.getElementById('update_header');
updateHeader.addEventListener('click', () => {
    document.querySelector('header').textContent = 'New Header!!!';
});
