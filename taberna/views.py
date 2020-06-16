from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from .models import Pizza
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

def index_view(request):

    return render(request, 'index.html')

def bebidas_view(request):

    return render(request, 'bebidas.html')

def comidas_view(request):

    context = {
        'pizza': Pizza.objects.order_by('?').all(),
    }

    return render(request, 'comidas.html', context)

def pizza_view(request):

    context = {
        'pizza': Pizza.objects.order_by('?').all(),
    }

    return render(request, 'pizzas.html', context)



def carrinho_view(request):
    pedido = []
    sabor = []
    encontrado = False
    catupiry = False
    total = 0
    s = 1
    verifica = ''

    pizzas = Pizza.objects.order_by('pk').all()

    while request.GET.get(f'sabor1-{s}') != None:
        s1 = request.GET.get(f'sabor1-{s}')
        s2 = request.GET.get(f'sabor2-{s}')
        sabor.append(f'Pizza {s1} / {s2}')
        s += 1

    j = 0
    for pi in pizzas:
        if request.GET.get(f'f{pi.id}'):
            pp = request.GET.get(f'f{pi.id}').split(',')
            quant = int(request.GET.get(f'{pi.id} {pi.preco_f}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {pi.preco_f}') == 'on':
                catupiry = True
                pp[1] += 2

            pp[1] *= quant
            if verifica != pi.id:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j], pp, quant])
                j += 1
            else:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j - 1]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j - 1], pp, quant])

            encontrado = True
            total += pp[1]
            verifica = pi.id

        if request.GET.get(f'g{pi.id}'):
            pp = request.GET.get(f'g{pi.id}').split(',')
            quant = int(request.GET.get(f'{pi.id} {pi.preco_g}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {pi.preco_g}') == 'on':
                catupiry = True
                pp[1] += 2

            pp[1] *= quant
            if verifica != pi.id:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j], pp, quant])
                j += 1
            else:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j - 1]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j - 1], pp, quant])

            encontrado = True
            total += pp[1]
            verifica = pi.id

        if request.GET.get(f'm{pi.id}'):
            pp = request.GET.get(f'm{pi.id}').split(',')
            quant = int(request.GET.get(f'{pi.id} {pi.preco_m}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {pi.preco_m}') == 'on':
                catupiry = True
                pp[1] += 2

            pp[1] *= quant
            if verifica != pi.id:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j], pp, quant])
                j += 1
            else:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j - 1]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j - 1], pp, quant])

            encontrado = True
            total += pp[1]
            verifica = pi.id

        if request.GET.get(f'p{pi.id}'):
            pp = request.GET.get(f'p{pi.id}').split(',')
            quant = int(request.GET.get(f'{pi.id} {pi.preco_p}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {pi.preco_p}') == 'on':
                catupiry = True
                pp[1] += 2

            pp[1] *= quant
            if verifica != pi.id:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j], pp, quant])
                j += 1
            else:
                if catupiry:
                    catupiry = False
                    pedido.append([f'{sabor[j - 1]} + Catupiry', pp, quant])
                else:
                    pedido.append([sabor[j - 1], pp, quant])

            encontrado = True
            total += pp[1]
            verifica = pi.id

    if not encontrado:
        return redirect(to='pizzas')

    data = request.GET.get('datetime')

    data = f'{data[8:10]}/{data[5:7]}/{data[0:4]} às {data[11:]}'
    mensagem = '*Olá. Eu gostaria de:*\n\n'
    for pe in pedido:
        mensagem = mensagem + f'{pe[0]} ({pe[1][0]}) x {pe[2]}\n'

    mensagem = mensagem + f'\n*Data: {data}*'

    print(mensagem)

    context = {
        'pedido': pedido,
        'total': total,
        'data': data,
        'mensagem': mensagem,
    }

    return render(request, 'carrinho.html', context)






    """
    def form_valid(self, form):
        form.pedido()

        pizza = form.cleaned_data['pizza']
        email = form.cleaned_data['email']

        print(f'Boa refeição {email} {pizza}')

        messages.success(self.request, 'Deu certo')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Deu errado')
        return super(IndexView, self).form_invalid(form)
    """