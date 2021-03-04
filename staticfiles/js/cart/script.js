document.querySelector('#order-now').addEventListener('click', () => {

    let have_order = document.querySelector('#order-cart').getAttribute('data-order');
    if(have_order) {
        let order = document.querySelector('#order-cart').getAttribute('data-message');
        order = window.encodeURIComponent(order);
    
        open(`https://api.whatsapp.com/send?phone=5588981361195&text=${order}`);
    }
    else {
        alert("Seu carrinho está vázio. Peça algum produto antes de encomendar.");
    }

});