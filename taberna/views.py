from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from .models import Pizza, PrecoPizza, Drink, Pasta
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
import re

class AddCart:
    list_orders = []
    def __init__(self, request):
        self.add(request)

    def add(self, request):
        if str(request.method) == 'POST':
            messages.success(request,
                             "Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")
            form = request.POST
            AddCart.list_orders.append(form)

"""def add_cart(request):
    if str(request.method) == 'POST':
        messages.success(request,"Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")
        form = request.POST
        order.append(form)"""

def make_message(order):
    message = '*Olá. Eu gostaria de:*\n\n'
    for pe in order:
        if pe == 'pz':
            for each_order in order[pe][0]:
                if len(each_order) == 5:
                    message += f'Pizza: {each_order[0]} {each_order[4]} (R$2.0) - {each_order[1]} x {each_order[3]} ({each_order[2]})\n\n'
                else:
                    message += f'Pizza: {each_order[0]} - {each_order[1]} x {each_order[3]} ({each_order[2]})\n\n'

        elif pe == 'dk':
            for each_order in order[pe]:
                message += f'{each_order[0]}: {each_order[1]} x {each_order[4]} ({each_order[2]})\n\n'

        elif pe == 'pa':
            for pasta in order[pe].values():
                for each_order in pasta:
                    message += f'{each_order[0]}: {each_order[1]} x {each_order[4]} ({each_order[2]})\n\n'

    message += f'Total: {order["tt"]}\n\n'
    message += f'Data: {order["dt"]}'

    print(message)

    return message

def index_view(request):
    return render(request, 'index.html')

def drinks_view(request):
    context = {
        'drinks': Drink.objects.all()
    }
    drink_order = AddCart(request)

    return render(request, 'drinks.html', context)

def pastas_view(request):
    pastas = Pasta.objects.all()
    pastas_types = {}
    pastel = []
    sfiha = []
    enroladinho = []
    coxinha = []
    sundry = []

    for pasta in pastas:
        if pasta.product.lower() == 'pastel':
            pastel.append(pasta)
            pastas_types['pastel'] = pastel
        elif pasta.product.lower() == 'esfirra':
            sfiha.append(pasta)
            pastas_types['esfirra'] = sfiha
        elif pasta.product.lower() == 'coxinha':
            coxinha.append(pasta)
            pastas_types['coxinha'] = coxinha
        elif pasta.product.lower() == 'enroladinho':
            enroladinho.append(pasta)
            pastas_types['enroladinho'] = enroladinho
        else:
            sundry.append(pasta)
            pastas_types['sundry'] = sundry

    context = {
        'pastas': pastas_types,
        'soda': Drink.objects.filter(category='soda'),
    }

    pasta_order = AddCart(request)

    return render(request, 'pastas.html', context)

def pizza_view(request):
    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda': Drink.objects.filter(category='soda'),
    }

    pizza_order = AddCart(request)

    return render(request, 'pizzas.html', context)

def kart_view(request):

    context = {}

    if AddCart.list_orders:
        pizzas = []
        specifications = []
        drinks = []
        type = price = amount = cont = f1 = f2 = date = total = 0
        catupiry = False
        pastas = {}
        pastel_cart = []
        coxinha_cart = []
        sfiha_cart = []
        enroladinho_cart = []
        sundry_cart = []

        for p in AddCart.list_orders:
            for pp, hh in p.items():
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
                    amount = int(hh)

                if pp[0:7] == 'camount':
                    catupiry = True

                if amount != 0:
                    if not catupiry:
                        price *= amount
                        total += price
                        specifications.append(f'{f1}/{f2}, {type}, {price}, {amount}'.split(', '))
                    else:
                        price = (price + 2) * amount
                        total += price
                        specifications.append(f'{f1}/{f2}, {type}, {price}, {amount}, + catupiry'.split(', '))
                        catupiry = False

                amount = 0
                if pp[:5] == 'drink' and hh != '' and hh != '0':
                    category_d, size_d, price_d, photo_d = pp[6:].split(', ')
                    price_d = float(price_d.replace(',', '.'))
                    price_d *= int(hh)
                    total += price_d
                    drinks.append(f'{category_d}, {size_d}, R${price_d}, {photo_d}, {hh}'.split(', '))

                if pp == 'request_date':
                    date = f'{hh[8:10]}/{hh[5:7]}/{hh[0:4]} às {hh[11:]}'



                if pp[:5] == 'pasta' and hh != '' and int(hh) > 0:
                    pasta_pp = pp.split(', ')[1:]

                    price_pasta = float(pasta_pp[2].replace(',', '.'))
                    price_pasta *= int(hh)

                    total += price_pasta

                    if 'pastel' in pp:
                        pastel_cart.append([pasta_pp[0], pasta_pp[1], f'R${pasta_pp[2]}', pasta_pp[3], hh])
                        pastas['pastel'] = pastel_cart
                    elif 'esfirra' in pp:
                        sfiha_cart.append([pasta_pp[0], pasta_pp[1], f'R${pasta_pp[2]}', pasta_pp[3], hh])
                        pastas['sfiha'] = sfiha_cart
                    elif 'enroladinho' in pp:
                        enroladinho_cart.append([pasta_pp[0], pasta_pp[1], f'R${pasta_pp[2]}', pasta_pp[3], hh])
                        pastas['enroladinho'] = enroladinho_cart
                    elif 'coxinha' in pp:
                        coxinha_cart.append([pasta_pp[0], pasta_pp[1], f'R${pasta_pp[2]}', pasta_pp[3], hh])
                        pastas['coxinha'] = coxinha_cart
                    elif 'sundry' in pp:
                        sundry_cart.append([pasta_pp[0], pasta_pp[1], f'R${pasta_pp[2]}', pasta_pp[3], hh])
                        pastas['sundry'] = sundry_cart

        pizzas.append(specifications)
        print(drinks)

        order = {'pz': pizzas, 'dk': drinks, 'pa': pastas, 'dt': date, 'tt': total}

        message = make_message(order)

        context = {
            'order': order,
            'message': message,
        }

    return render(request, 'cart.html', context)