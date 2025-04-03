const addItem = document.getElementById('add_item');
const myList = document.querySelector('.my_list');
addItem.addEventListener('click', function () {
    const newList = document.createElement('li');
    newList.textContent = 'Item';
});