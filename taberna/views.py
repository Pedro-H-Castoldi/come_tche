from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from .models import Pizza, PrecoPizza, Refrigerante
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

pedido = []

def index_view(request):

    return render(request, 'index.html')

def bebidas_view(request):

    return render(request, 'bebidas.html')

def comidas_view(request):

    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda':  Refrigerante.objects.all(),
    }

    def add_kart():
        messages.success(request,"Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")
        form = request.POST
        pedido.append(form)

    if str(request.method) == 'POST':
        if pedido:
            if request.POST != pedido[-1]:
                add_kart()
        else:
            add_kart()

    return render(request, 'comidas.html', context)

def pizza_view(request):

    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda': Refrigerante.objects.all(),
    }

    if PrecoPizza.objects.all():
        context['preco'] = PrecoPizza.objects.all()[0]

    return render(request, 'pizzas.html', context)

def pizza_view(request):

    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda': Refrigerante.objects.all(),
    }

    if PrecoPizza.objects.all():
        context['preco'] = PrecoPizza.objects.all()[0]

    return render(request, 'pizzas.html', context)

def kart_view(request):

    context = {}

    if pedido:
        pizzas = []
        specifications = []
        sodas = []
        type = price = amount = cont = f1 = f2 = date = 0
        catupiry = False


        for p in pedido:
            for pp, hh in p.items():
                print(f'{pp}: {hh}')
                if pp[0:6] == 'flavor':
                    if cont == 0:
                        f1 = hh
                        cont = 1
                    else:
                        f2 = hh
                        cont = 0

                if hh != '':
                    if len(hh.split(' ')) == 2:
                        type, price = hh.split(', ')
                        price = float(price.replace(',', '.'))

                if pp[0:7] == 'qamount' and pp != 0:
                    amount = hh

                if pp[0:7] == 'camount':
                    catupiry = True

                if amount != 0:
                    if not catupiry:
                        specifications.append(f'{f1}/{f2}, {type}, {price}, {amount}'.split(', '))
                    else:
                        price += 2
                        specifications.append(f'{f1}/{f2}, {type}, {price}, {amount}, + catupiry'.split(', '))
                        catupiry = False

                amount = 0

                if pp[0:4] == 'soda' and hh != '' and hh != '0':
                    flavor_s, size_s, price_s = pp[7:].split(', ')
                    sodas.append(f'{flavor_s}, {size_s}, R${float(price_s.replace(",", "."))}, {hh}'.split(', '))

                if pp == 'request_date':
                    date = f'{hh[8:10]}/{hh[5:7]}/{hh[0:4]} às {hh[11:]}'

        pizzas.append(specifications)

        order = {'pz':pizzas, 'sd':sodas, 'dt':date}

        context = {
            'order': order,
        }

    return render(request, 'carrinho.html', context)


"""def carrinho_view(request):
    order = {}
    pizzas = []
    specifications = []
    pizza = []
    sodas = []
    dates = []
    type_price = 0
    amount = 0
    catupiry = False

    for p in pedido:
        for pp, hh in p.items():
            if pp[0:6] == 'flavor':
                pizzas.append(hh)

            if hh != '':
                if len(hh.split(' ')) == 2:
                    type_price = hh.split(', ')
                    type_price[1] = float(type_price[1].replace(',', '.'))

            if pp[0:7] == 'qamount' and pp != 0:
                amount = hh

            if pp[0:7] == 'camount':
                catupiry = True

            if amount != 0:
                if catupiry:
                    specifications.append([type_price, amount, catupiry])
                else:
                    specifications.append([type_price, amount])

            catupiry = False
            amount = 0

            if pp[0:4] == 'soda' and hh != '' and hh != '0':
                sodas.append(f'{pp[7:]}, {hh}')

            if pp == 'request_date':
                dates.append(hh)

    if pizzas:
        for i in range(1, len(pizzas), 2):
            pizza.append(f'{pizzas[i-1]}/{pizzas[i]}')

    order = {'pz':pizza, 'sp':specifications, 'sd':sodas, 'dt':dates}

    for k in order:
        print()

    context = {
        'order': order,
    }

    return render(request, 'carrinho.html', context)"""






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
        
        
        
        
        
        sabor = []
    refrigerantes = []
    encontrado = False
    catupiry = False
    total = 0
    s = 1
    verifica = ''

    pizzas = Pizza.objects.order_by('pk').all()
    preco_p = PrecoPizza.objects.all()[0]

    while request.GET.get(f'sabor1-{s}') != None:
        s1 = request.GET.get(f'sabor1-{s}')
        s2 = request.GET.get(f'sabor2-{s}')
        sabor.append(f'Pizza {s1} / {s2}')
        s += 1

    j = 0
    for pi in pizzas:
        if request.GET.get(f'f{pi.id}'):
            pp = request.GET.get(f'f{pi.id}').split(',')
            quant = int(request.GET.get(f'{pi.id} {preco_p.preco_f}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {preco_p.preco_f}') == 'on':
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
            quant = int(request.GET.get(f'{pi.id} {preco_p.preco_g}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {preco_p.preco_g}') == 'on':
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
            quant = int(request.GET.get(f'{pi.id} {preco_p.preco_m}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {preco_p.preco_m}') == 'on':
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
            quant = int(request.GET.get(f'{pi.id} {preco_p.preco_p}'))
            pp[1] = float(pp[1])

            if request.GET.get(f'c{pi.id} {preco_p.preco_p}') == 'on':
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

    if request.GET.get('coca-cola'):
        refri = request.GET.get('coca-cola')
        if request.GET.get('cocadlq1'):
            q1 = int(request.GET.get('cocadlq1'))
            refrigerantes.append(f'{refri} 1l x {q1} (R$ {5.0 * q1})')
            total += (5.0 * q1)
        if request.GET.get('cocadlq2'):
            q2 = int(request.GET.get('cocadlq2'))
            refrigerantes.append(f'{refri} 2l x {q2} (R$ {10.0 * q2})')
            total += (10.0 * q2)

    if request.GET.get('pepsi'):
        refri = request.GET.get('pepsi')
        if request.GET.get('pepsidlq1'):
            q1 = int(request.GET.get('pepsidlq1'))
            refrigerantes.append(f'{refri} 1l x {q1} (R$ {5.0 * q1})')
            total += (5.0 * q1)
        if request.GET.get('pepsidlq2'):
            q2 = int(request.GET.get('pepsidlq2'))
            refrigerantes.append(f'{refri} 2l x {q2} (R$ {10.0 * q2})')
            total += (10.0 * q2)

    if request.GET.get('guarana'):
        refri = request.GET.get('guarana')
        if request.GET.get('guaranadlq1'):
            q1 = int(request.GET.get('guaranadlq1'))
            refrigerantes.append(f'{refri} 1l x {q1} (R$ {5.0 * q1})')
            total += (5.0 * q1)
        if request.GET.get('guaranadlq2'):
            q2 = int(request.GET.get('guaranadlq2'))
            refrigerantes.append(f'{refri} 2l x {q2} (R$ {10.0 * q2})')
            total += (10.0 * q2)

    if request.GET.get('fanta-laranja'):
        refri = request.GET.get('fanta-laranja')
        if request.GET.get('fanta-laranja'):
            q1 = int(request.GET.get('fantadlq1'))
            refrigerantes.append(f'{refri} 1l x {q1} (R$ {5.0 * q1})')
            total += (5.0 * q1)
        if request.GET.get('fantadlq2'):
            q2 = int(request.GET.get('fantadlq2'))
            refrigerantes.append(f'{refri} 2l x {q2} (R$ {10.0 * q2})')
            total += (10.0 * q2)

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
        'refrigerantes': refrigerantes,
    }

    
    """