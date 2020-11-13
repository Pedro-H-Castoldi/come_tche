from django.views.generic import FormView, TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pizza, PrecoPizza, Drink, Pasta, Cart, Date

def add_date(dates):
    definitive_date = ''
    for date in dates:
        if definitive_date == '':
            definitive_date = date.date
        else:
            if date.date != definitive_date:
                if int(date.date.split('/')[1]) > int(definitive_date.split('/')[1]):
                    if int(date.date.split('/')[1]) == 12 and int(definitive_date.split('/')[1]) == 1:
                        pass
                    else:
                        definitive_date = date.date
                elif int(date.date.split('/')[1]) == int(definitive_date.split('/')[1]):
                    if int(date.date.split('/')[2][8:10]) > int(definitive_date.split('/')[2][8:10]):
                        definitive_date = date.date
                    elif int(date.date.split('/')[2][8:10]) == int(definitive_date.split('/')[2][8:10]):
                        if int(date.date.split('/')[2][11:]) > int(definitive_date.split('/')[2][11:]):
                            definitive_date = date.date
    return definitive_date

def add_cart(request, soda_pizza=False):
    if not soda_pizza:
        messages.success(request,
                         "Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")

    form = request.POST
    measure = details = data = date = ''

    for i in form:
        identify = i.split(', ')

        if i == 'request_date':
            date = f'{form[i][8:10]}/{form[i][5:7]}/{form[i][0:4]} às {form[i][11:]}'

        if form[i] != '' and len(identify) == 2:
            if identify[0] == 'd':
                data = Drink.objects.get(pk=int(identify[1]))
                details = data.category
                if data.liters > 5:
                    measure = f'{data.liters:.0f}ml'
                else:
                    measure = f'{data.liters:.0f}l'

            elif identify[0] == 'p':
                data = Pasta.objects.get(pk=int(identify[1]))
                details = data.flavor

            cart = Cart(
                user=request.user,
                product=data.product,
                product_id=data.id,
                product_type=data,
                details=details,
                measure=measure,
                price=data.price * int(form[i]),
                amount=form[i],
                image=data.image.thumb.url,
            )
            Cart.save(cart)
    order_date = Date(
        user=request.user,
        date=date,
    )
    Date.save(order_date)

def add_pizzar_cart(request):
    messages.success(request,"Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")
    form = request.POST
    date = product = details = measure = flavor1 = flavor2 = price = amount = ''
    for i in form:
        identify = i.split(', ')

        if i == 'request_date':
            date = f'{form[i][8:10]}/{form[i][5:7]}/{form[i][0:4]} às {form[i][11:]}'


        if identify[0] == 'd' and form[i] != '':
            add_cart(request, True)
        elif 'flavor1' in i:
            flavor1 = form[i]
        elif 'flavor2' in i:
            flavor2 = form[i]

        elif i[0] == 'F' and int(i[1:]) > 0:
            product = f'{flavor1}/{flavor2}'
            measure = 'Família'
            price = form[i].split(', ')[1]
            price = float(price.replace(',', '.'))

        elif i[0] == 'B' and int(i[1:]) > 0:
            product = f'{flavor1}/{flavor2}'
            measure = 'Grande'
            price = form[i].split(', ')[1]
            price = float(price.replace(',', '.'))

        elif i[0] == 'A' and int(i[1:]) > 0:
            product = f'{flavor1}/{flavor2}'
            measure = 'Média'
            price = form[i].split(', ')[1]
            price = float(price.replace(',', '.'))

        elif i[0] == 'S' and int(i[1:]) > 0:
            product = f'{flavor1}/{flavor2}'
            measure = 'Pequena'
            price = form[i].split(', ')[1]
            price = float(price.replace(',', '.'))

        elif i[0] == 'M' and int(i[1:]) > 0:
            product = f'{flavor1}/{flavor2}'
            measure = 'Mini'
            price = form[i].split(', ')[1]
            price = float(price.replace(',', '.'))

        elif 'camount' in i:
            details = ' + catupiry'
            price += 2

        elif 'qamount' in i:
            amount = int(form[i])
            price *= amount

        if amount != '':
            cart = Cart(
                user=request.user,
                product=product,
                product_id=0,
                product_type='Pizza',
                details=details,
                measure=measure,
                price=float(price),
                amount=amount,
                image='',
            )
            Cart.save(cart)
            amount = ''

    order_date = Date(
        user=request.user,
        date=date,
    )
    Date.save(order_date)

def make_message(orders, total, date, user):
    message = f'*Olá sou {user}. Eu gostaria de:*\n\n'
    for order in orders:
        if order.product_type == 'Pizza':
            if 'catupiry' in order.details:
                message += f'Pizza: {order.product} + catupiry (R$2,0) - {order.measure} x {order.amount} (R${order.price})\n\n'
            else:
                message += f'Pizza: {order.product} {order.measure} x {order.amount} (R${order.price})\n\n'

        elif order.product_type == 'Bebida':
            message += f'{order.details} {order.product} {order.measure} x {order.amount} (R${order.price})\n\n'

        elif order.product_type == 'Salgado':
            message += f'{order.product} de {order.details} x {order.amount} (R${order.price})\n\n'

    message += f'*Total: {total}*\n\n'
    message += f'*Data: {date}*'

    return message

def index_view(request):
    return render(request, 'index.html')

def drinks_view(request):
    context = {
        'drinks': Drink.objects.all()
    }

    if str(request.method) == 'POST':
        add_cart(request)
        return redirect(to='drinks')


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

    if str(request.method) == 'POST':
        add_cart(request)
        return redirect(to='pastas')

    return render(request, 'pastas.html', context)

def pizza_view(request):
    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda': Drink.objects.filter(category='soda'),
    }

    if str(request.method) == 'POST':
        add_pizzar_cart(request)
        return redirect(to='pizzas')

    return render(request, 'pizzas.html', context)

@login_required()
def kart_view(request):
    context = {}
    orders = Cart.objects.filter(user=request.user)
    dates = Date.objects.filter(user=request.user)

    if orders:
        total = 0
        order_date = ''
        for order in orders:
            total += order.price

        order_date = add_date(dates)
        message = make_message(orders, total, order_date, request.user)

        context = {
            'orders': orders,
            'total': total,
            'date': order_date,
            'message': message,
            'user': request.user,
        }

        if str(request.method) == 'POST':
            orders.delete()
            dates.delete()
            return redirect(to='index')

    return render(request, 'cart.html', context)