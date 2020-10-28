from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pizza, PrecoPizza, Drink, Pasta, Cart

"""class AddCart:
    dic_orders = {}
    list_order = []

    def add(self, request):
        if str(request.method) == 'POST':
            messages.success(request,
                             "Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")

            if len(self.list_order) == 0:
                self.add_cart_now(request)
            elif self.list_order[-1] != request.POST:
                self.add_cart_now(request)

    def add_cart_now(self, request):
        form = request.POST
        self.list_order.append(form)
        AddCart.dic_orders[str(request.user)] = self.list_order

add_cart = AddCart()"""

"""def add_cart(request):
    if str(request.method) == 'POST':
        messages.success(request,"Seu pedido foi enviado ao carrinho. Continue pedindo ou acesse o carrinho para finalizar a encomenda.")
        form = request.POST
        order.append(form)"""

dic_order = {}

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

    return message

def index_view(request):
    return render(request, 'index.html')

def drinks_view(request):
    context = {
        'drinks': Drink.objects.all()
    }

    if str(request.method) == 'POST':
        form = request.POST
        for i in form:
            if form[i] != '' and len(i) < 5:
                drink = Drink.objects.get(pk=i)
                a = Cart(
                    user=request.user,
                    product=drink.product,
                    product_id=drink.id,
                    price=drink.price,
                    amount=form[i],
                    image=drink.image,
                )

                Cart.save(a)


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

    #add_cart.add(request)

    return render(request, 'pastas.html', context)

def pizza_view(request):
    context = {
        'pizzas': Pizza.objects.order_by('?').all(),
        'price': PrecoPizza.objects.all()[0],
        'soda': Drink.objects.filter(category='soda'),
    }

    #add_cart.add(request)

    return render(request, 'pizzas.html', context)

@login_required()
def kart_view(request):
    context = {
        'order': Cart.objects.filter(user=request.user)
    }

    return render(request, 'cart.html', context)