var n = 1;
var nn = 3;
let number_pizza = 0;
const button = document.querySelector('#authenticated');

function order_released() {
    button.removeAttribute('disabled');
}

function date_today() {
    let today = new Date;
    let date = document.querySelector('#datetime');
    let day = today.getDate();
    let max_day = day;
    let month = today.getMonth() + 1;
    let max_month = month;
    let max_year = today.getFullYear();
    let hours = today.getHours();
    let minutes = today.getMinutes();

    if(month < 10) {
        month = `0${month}`;
        if(parseInt(month) < 9) {
            max_month = `0${parseInt(month)+1}`;
        }
        else {
            max_month = parseInt(month) + 1;
        }
    }
    else if (month < 12) {
        max_month = parseInt(month) + 1;
    }

    if(month == 12) {
        max_month = '01';
        max_year = today.getFullYear() + 1;
    }

    if(day < 10) {
        day = `0${day}`;
    }
    else if(max_month == '02' && day >= 28) {
        let year = today.getFullYear();
        if(year%4 == 0 && year%100 != 0 || year%400 == 0) {
            max_day = 29;
        }
        else {
            max_day = 28;
        }
    }
    else if( (day == 31 && max_month == '04') || (day == 31 && max_month == '06') || (day == 31 && max_month == '09') || (day == 31 && max_month == '11') ) {
        max_day = 30;
    }

    else {
        max_day = 31
    }

    if(hours < 23) {
        hours = hours + 1;
    }
    else {
        hours = '00';
    }
    if(minutes < 10) {
        minutes = `0${minutes}`;
    }
    
    date.min = `${today.getFullYear()}-${month}-${day}T${hours}:${minutes}`;
    date.value = `${today.getFullYear()}-${month}-${day}T${hours}:${minutes}`;
    date.max = `${max_year}-${max_month}-${max_day}T23:59`;
}

let amount_soda = document.querySelectorAll('.soda-flavor input');
amount_soda.forEach(task => {
    task.addEventListener('change', soda_exist);
})

function soda_exist() {

    let found = false;
    amount_soda.forEach(task => {
        if(task.value > 0) {
            found = true;
        }
    })

    if(found) {
        order_released();
    }
    else {
        button.disabled = true;
    }
}

function pizza_exist(c_size_exist, number_pizza_exist) {
    let checked = 0;
    let cont = 0
    
    for(let i=0; i<number_pizza_exist; i++) {
        for(j=cont; j<cont+5; j++){
            if(c_size_exist[j].children[2].checked) {
                checked++;
                break;
            }
        }
        cont += 5;
    }

    if(checked == number_pizza_exist) {
        order_released();
    }
    else {
        soda_exist();
    }
}

function go(more=false) {

    button.disabled = true;
    soda_exist();

    /*let select = document.querySelectorAll('.select');
    select.forEach(task => {
        task.addEventListener('change', e => {
            let flavor = e.target.value;
            let num = e.target.id.split('-')[1];
    
            if(num%2 != 0) {
                let photo_l = document.querySelector(`#img-p${num}`);
                photo_l.src = `../static/images/${flavor}_e.jpg`;
            }
            else {
                let photo_l = document.querySelector(`#img-p${num}`);
                photo_l.src = `../static/images/${flavor}_d.jpg`;
            }
        })
    })*/

    let c_size = document.querySelectorAll('.content-sizes');
    number_pizza = c_size.length / 5;

    if(!more) {
        pizza_exist(c_size, number_pizza);
    }
    
    c_size.forEach(task => {
        task.children[2].addEventListener('click', e => {
            if(e.target.checked) {
                let quant_catu = task.children[3];
                quant_catu.innerHTML = `<p> + Catu</p><input type="checkbox" class="catu" name="c${quant_catu.id}"><input type="number" min="1" placeholder="quant" class="quant" name="q${quant_catu.id}" required>`;
            }
            else {
                task.children[3].innerHTML = '';
            }
            pizza_exist(c_size, number_pizza);
        })
    })
}

let one_more = document.querySelector('#one-more').addEventListener('click', function() {
    let pizzas_content = document.querySelector('#pizzas-content');
    let pizza_template = document.querySelector('#p1');

    let new_pizza = document.createElement('div');
    let close_pizza = document.createElement('div');

    close_pizza.className = "close-element";
    close_pizza.innerHTML = "X";

    new_pizza.className = "product-content";
    new_pizza.id = "p2";

    new_pizza.innerHTML = pizza_template.innerHTML;
    new_pizza.append(close_pizza);
    n++;

    new_pizza.children[0].children[0].name = `flavor1_${n}`;
    new_pizza.children[0].children[0].id = `flavor-${nn}`;

    new_pizza.children[0].children[1].name = `flavor2_${n}`;
    new_pizza.children[0].children[1].id = `flavor-${nn+1}`;

    new_pizza.children[1].children[0].children[0].id = `img-p${nn}`;
    new_pizza.children[1].children[0].children[0].src = "../static/images/pizza.jpg"
    new_pizza.children[1].children[1].children[0].id = `img-p${nn+1}`;
    new_pizza.children[1].children[1].children[0].src = "../static/images/pizza2.jpg"

    new_pizza.children[2].children[0].id = `fam${n}`;
    new_pizza.children[2].children[0].children[0].htmlFor = `check-f${n}`;
    new_pizza.children[2].children[0].children[0].children[0].children[2].id = `check-f${n}`;
    new_pizza.children[2].children[0].children[0].children[0].children[2].name = `F${n}`;
    new_pizza.children[2].children[0].children[0].children[0].children[3].id = `amount_f${n}`;
    new_pizza.children[2].children[0].children[0].children[0].children[3].innerHTML = "";

    new_pizza.children[2].children[1].id = `big${n}`;
    new_pizza.children[2].children[1].children[0].htmlFor = `check-b${n}`;
    new_pizza.children[2].children[1].children[0].children[0].children[2].id = `check-b${n}`;
    new_pizza.children[2].children[1].children[0].children[0].children[2].name = `B${n}`;
    new_pizza.children[2].children[1].children[0].children[0].children[3].id = `amount_b${n}`;
    new_pizza.children[2].children[1].children[0].children[0].children[3].innerHTML = "";

    new_pizza.children[2].children[2].id = `ave${n}`;
    new_pizza.children[2].children[2].children[0].htmlFor = `check-a${n}`;
    new_pizza.children[2].children[2].children[0].children[0].children[2].id = `check-a${n}`;
    new_pizza.children[2].children[2].children[0].children[0].children[2].name = `A${n}`;
    new_pizza.children[2].children[2].children[0].children[0].children[3].id = `amount_a${n}`;
    new_pizza.children[2].children[2].children[0].children[0].children[3].innerHTML = "";

    new_pizza.children[2].children[3].id = `sam${n}`;
    new_pizza.children[2].children[3].children[0].htmlFor = `check-s${n}`;
    new_pizza.children[2].children[3].children[0].children[0].children[2].id = `check-s${n}`;
    new_pizza.children[2].children[3].children[0].children[0].children[2].name = `S${n}`;
    new_pizza.children[2].children[3].children[0].children[0].children[3].id = `amount_s${n}`;
    new_pizza.children[2].children[3].children[0].children[0].children[3].innerHTML = "";

    new_pizza.children[2].children[4].id = `min${n}`;
    new_pizza.children[2].children[4].children[0].htmlFor = `check-m${n}`;
    new_pizza.children[2].children[4].children[0].children[0].children[2].id = `check-m${n}`;
    new_pizza.children[2].children[4].children[0].children[0].children[2].name = `M${n}`;
    new_pizza.children[2].children[4].children[0].children[0].children[3].id = `amount_m${n}`;
    new_pizza.children[2].children[4].children[0].children[0].children[3].innerHTML = "";

    pizzas_content.append(new_pizza);
    nn += 2;

    let closePizzaNow = document.querySelectorAll('.close-element');

    closePizzaNow.forEach(task => {
        task.addEventListener('click', e => {
            e.target.parentNode.remove();
            --number_pizza;
            go();
        })
    } )

    go(true);
})

go();
date_today();