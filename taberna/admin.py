from django.contrib import admin
from .models import Pizza, PrecoPizza, Drink, Pasta, Cart

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display =('product', 'stock')

@admin.register(PrecoPizza)
class PrecoPizzaAdmin(admin.ModelAdmin):

    list_display = ('price_f', 'price_b', 'price_a', 'price_s', 'price_m')

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):

    list_display = ('product', 'stock', 'category', 'liters')

@admin.register(Pasta)
class PastaAdmin(admin.ModelAdmin):
    list_display = ('product', 'flavor', 'stock')