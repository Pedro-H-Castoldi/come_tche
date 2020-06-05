from django.contrib import admin
from .models import Produto, Pizza
from django.db import models

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display =('produto', 'estoque', 'ativo')