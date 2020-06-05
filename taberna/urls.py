from django.urls import path
from .views import index_view, pizza_view, bebidas_view, comidas_view, carrinho_view

urlpatterns = [
    path('', index_view,  name='index'),
    path('pizzas/', pizza_view, name='pizzas'),
    path('bebidas/', bebidas_view, name='bebidas'),
    path('comidas/', comidas_view, name='comidas'),
    path('carrinho/', carrinho_view, name='carrinho'),
]