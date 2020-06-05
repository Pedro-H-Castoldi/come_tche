var f = true
var i = 0
let c = document.getElementsByClassName('box')
var ident = ''
let quant = ''

quant = function(id){

    if(f){

        var quant = document.createElement('input')
        var catupiry = document.createElement('input')
        var label = document.createElement('label')
        var texto = document.createElement('p')
        var data = document.createElement('input')
        
        texto = "(+ R$2)"
    
        var preco
        var p = id.value.split(',')
        preco = `${p[2]},${p[3]}`
    
        quant.type = "number"
        quant.min = "1"
        quant.value = "1"
        quant.name = `${id.id}${p[2]}.${p[3]}`
        
        catupiry.type = "checkbox"
        catupiry.name = `c${id.id}${p[2]}.${p[3]}`
        
        data.type = "datetime-local"
        
        var pizzas = document.getElementById(`${id.id}${preco}`)
        var pedir = document.getElementById('ir')
        
        pizzas.append(quant)
        label.append(texto)
        label.append(catupiry)
        pizzas.append(label)
        pedir.prepend(data)
        //pizzas.append(br)

        alert(i)

        if(ident == quant.name && i > 0){
            i = 0
            pizzas.remove() // O remove comum n está funcionando.. ele só remove se for a div toda.
        }

        ident = `${id.id}${p[2]}.${p[3]}`
        i = 1
    }
}

for(let i=0; i < c.length; i++){
    c[i].addEventListener('click', function(){quant(c[i])})
}