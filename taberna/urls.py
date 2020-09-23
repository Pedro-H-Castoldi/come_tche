from django.urls import path
from .views import index_view, pizza_view, drinks_view, pastas_view, kart_view

urlpatterns = [
    path('', index_view,  name='index'),
    path('pizzas/', pizza_view, name='pizzas'),
    path('bebidas/', drinks_view, name='drinks'),
    path('salgados/', pastas_view, name='pastas'),
    path('carrinho/', kart_view, name='cart'),
]