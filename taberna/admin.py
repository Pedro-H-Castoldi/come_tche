from django.contrib import admin
from .models import Pizza, PrecoPizza, Refrigerante

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display =('produto', 'estoque', 'ativo')

@admin.register(PrecoPizza)
class PrecoPizzaAdmin(admin.ModelAdmin):

    list_display = ('preco_f', 'preco_g', 'preco_a', 'preco_p', 'preco_m')

@admin.register(Refrigerante)
class RefrigeranteAdmin(admin.ModelAdmin):

    list_display = ('produto', 'estoque', 'ativo')