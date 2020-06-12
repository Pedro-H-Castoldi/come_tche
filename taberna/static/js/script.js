let c = document.getElementsByClassName('box')
let butao = document.getElementById('encomendar')
let mais = document.getElementById('mais')

var encontrado = false
var ident = []
let quant = ''
var n = 1
var ns = 3
let pizzas_container = document.getElementById('pizzas')

quant = function(id){
    alert('qq')
    var quant = document.createElement('input')
    var catupiry = document.createElement('input')
    var label = document.createElement('label')
    var texto = document.createElement('p')
    var data = document.createElement('input')
        
    texto = "(+ R$2)"
    
    var p = id.value.split(',')
    var preco = `${p[1]},${p[2]}`
    
    quant.type = "number"
    quant.min = "1"
    quant.value = "1"
    quant.name = `${id.id}${p[1]}.${p[2]}`
        
    catupiry.type = "checkbox"
    catupiry.name = `c${id.id}${p[1]}.${p[2]}`
        
    data.type = "datetime-local"
    data.name = "datetime"
    data.required = true

        
    var pizzas = document.getElementById(`${id.id}${preco}`)
    var pedir = document.getElementById('ir')

    if(ident.length == 0){
        ident.push([`${id.id}${p[1]}.${p[2]}`, 1])
        //alert('iniciar')
        pizzas.append(quant)
        label.append(texto)
        label.append(catupiry)
        pizzas.append(label)
        pedir.prepend(data)
    }
    else{
        for(let i=0; i< ident.length; i++){             
            if(ident[i][0] == quant.name){
                encontrado = true
                if(ident[i][1] == 0){
                    alert('Não remover')
                    ident[i][1] = 1
                    pizzas.append(quant)
                    label.append(texto)
                    label.append(catupiry)
                    pizzas.append(label)
                }
                else if(ident[i][1] == 1){
                    alert('remover')
                    ident[i][1] = 0
                    pizzas.remove()
                    pizzas = document.createElement('strong')
                    pizzas.id = `${id.id}${preco}`

                    if(parseFloat(preco) == 30.00){
                        let pizz = document.getElementById(`fam${id.id}`)
                        //alert(`fam${id.id}`)
                        //alert(pizz)
                        pizz.append(pizzas)
                    }
                    else if(parseFloat(preco) == 25.00){
                        let pizz = document.getElementById(`gra${id.id}`)
                        pizz.append(pizzas)
                    }
                    else if(parseFloat(preco) == 20.00){
                        let pizz = document.getElementById(`med${id.id}`)
                        pizz.append(pizzas)
                    }
                    else{
                        let pizz = document.getElementById(`peq${id.id}`)
                        pizz.append(pizzas)
                    }
                }
            }
        }
        if(encontrado == false){
            ident.push([`${id.id}${p[1]}.${p[2]}`, 1])
            alert('Criado carimbo')
            pizzas.append(quant)
            label.append(texto)
            label.append(catupiry)
            pizzas.append(label)
        }
    }
    encontrado = false
}

let encomendar = function() {
    let pedido = document.getElementById('pedido').getAttribute('mensagem')
    pedido = window.encodeURIComponent(pedido)

    open(`https://api.whatsapp.com/send?phone=5588981194819&text=${pedido}`)
}

function foto(id) {
    let nf = id.slice(5, id.length)
    let valor = document.getElementById(`${id}`).value

    if(nf%2 != 0){
        if(valor == 'Calabresa'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/calabresa_e.jpg"
        }
        else if(valor == 'Frango'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/frango_e.jpg"
        }
        else if(valor == 'Portuguesa'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/portuguesa_e.png"
        }
    }
    else{
        if(valor == 'Calabresa'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/calabresa_d.jpg"
        }
        else if(valor == 'Frango'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/frango_d.jpg"
        }
        else if(valor == 'Portuguesa'){
            let img = document.getElementById(`f${nf}`)
            img.src = "../static/images/portuguesa_d.png"
        }
    }

}

let mais_uma = function() {
    let div = document.createElement('div')
    div.id = `${n}`
    div.class = "pizza"

    div.innerHTML = document.getElementById('0').innerHTML

    div.children[0].children[0].id = `sabor${ns}`
    div.children[0].children[1].id = `sabor${ns+1}`

    div.children[1].children[0].id = `f${ns}`
    div.children[1].children[1].id = `f${ns+1}`
    div.children[1].children[0].src = "../static/images/pizza.jpg"
    div.children[1].children[1].src = "../static/images/pizza2.jpg"

    div.children[2].children[0].id = `fam${n}`
    div.children[2].children[1].id = `gra${n}`
    div.children[2].children[2].id = `med${n}`
    div.children[2].children[3].id = `peq${n}`

    div.children[2].children[0].children[1].id = `${n}`
    div.children[2].children[0].children[1].name = `f${n}`
    div.children[2].children[0].children[2].id = `${n} 30,00`
    div.children[2].children[1].children[1].id = `${n}`
    div.children[2].children[1].children[1].name = `g${n}`
    div.children[2].children[1].children[2].id = `${n} 25,00`
    div.children[2].children[2].children[1].id = `${n}`
    div.children[2].children[2].children[1].name = `m${n}`
    div.children[2].children[2].children[2].id = `${n} 20,00`
    div.children[2].children[3].children[1].id = `${n}`
    div.children[2].children[3].children[1].name = `p${n}`
    div.children[2].children[3].children[2].id = `${n} 15,00`

    //alert(div.children[2].children[0].children[1].id)
    //alert(div.children[1].children[1].id)

    pizzas_container.append(div)

    n++
    ns += 2


    for(let i=0; i < c.length; i++){
        c[i].addEventListener('click', function(){quant(c[i])})
    }
}


for(let i=0; i < c.length; i++){
    c[i].addEventListener('click', function(){quant(c[i])})
}
mais.addEventListener('click', mais_uma)
butao.addEventListener('click', encomendar)

// Está clicando 2x na funcão q add quant e catupiry.