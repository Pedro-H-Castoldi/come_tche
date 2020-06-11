let c = document.getElementsByClassName('box')
let butao = document.getElementById('encomendar')

var encontrado = false
var ident = []
let quant = ''

quant = function(id){

    var quant = document.createElement('input')
    var catupiry = document.createElement('input')
    var label = document.createElement('label')
    var texto = document.createElement('p')
    var data = document.createElement('input')
        
    texto = "(+ R$2)"
    
    var preco
    var p = id.value.split(',')
    preco = `${p[1]},${p[2]}`
    
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
                    //alert('Não remover')
                    ident[i][1] = 1
                    pizzas.append(quant)
                    label.append(texto)
                    label.append(catupiry)
                    pizzas.append(label)
                }
                else if(ident[i][1] == 1){
                    //alert('remover')
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
            //alert('Criado carimbo')
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

for(let i=0; i < c.length; i++){
    c[i].addEventListener('click', function(){quant(c[i])})
}

butao.addEventListener('click', encomendar)