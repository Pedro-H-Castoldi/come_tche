const button = document.querySelector('#order-now button');

let drinkOrder = document.querySelectorAll('.drink-amount input');
drinkOrder.forEach(task => {
    task.addEventListener('change', drink_exist);
})

function drink_exist() {

    let found = false;
    drinkOrder.forEach(task => {
        if(task.value > 0) {
            found = true;
        }
    })

    if(found) {
        button.disabled = false;
    }
    else {
        button.disabled = true;
    }
}