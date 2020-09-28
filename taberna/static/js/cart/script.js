document.querySelector('#order-now').addEventListener('click', () => {

    let order = document.querySelector('#order-cart').getAttribute('message');
    order = window.encodeURIComponent(order);

    open(`https://api.whatsapp.com/send?phone=5588981194819&text=${order}`);
});