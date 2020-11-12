from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
import uuid

def get_filename(_intance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}.{ext}'
    return filename

class Base(models.Model):

    created = models.DateField('Data de criação', auto_now_add=True)
    modified = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True

class Produto(Base):

    product = models.CharField('Produto', max_length=50)
    stock = models.BooleanField('Estoque', default=True)
    image = StdImageField('Imagem', upload_to=get_filename, variations={'thumb': (124, 124)})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.product

class Pizza(Produto):

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return 'pizza'

class PrecoPizza(Base):

    price_f = models.DecimalField('Preço Família', max_digits=8, decimal_places=2, default=30.00)
    price_b = models.DecimalField('Preço Grande', max_digits=8, decimal_places=2, default=25.00)
    price_a = models.DecimalField('Preço Média', max_digits=8, decimal_places=2, default=20.00)
    price_s = models.DecimalField('Preço Pequena', max_digits=8, decimal_places=2, default=15.00)
    price_m = models.DecimalField('Preço Mini', max_digits=8, decimal_places=2, default=6.00)

    class Meta:
        verbose_name = 'Preço Pizza'
        verbose_name_plural = 'Preços Pizzas'

    def __str__(self):
        return 'Preços'


class Drink(Produto):

    CHOICES = [
        ('beer', 'Cerveja'),
        ('whisky', 'Whisky'),
        ('vodka', 'Vodka'),
        ('energetic', 'Energético'),
        ('cognac', 'Conhaque'),
        ('cachaça', 'Cachaça'),
        ('rum', 'Rum'),
        ('soda', 'Refrigerante'),
        ('wine', 'Vinho'),
        ('varied', 'Variados'),
    ]
    category = models.CharField('Categoria', choices=CHOICES, max_length=10)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    liters = models.DecimalField('Litros/Ml', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

    def __str__(self):
        return 'Bebida'

class Pasta(Produto):

    flavor = models.CharField('Sabor', max_length=100)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Salgado'
        verbose_name_plural = 'Salgados'

    def __str__(self):
        return 'Salgado'


class Cart(Base):
    user = models.CharField('User', max_length=255)
    product = models.CharField('Produto', max_length=255)
    product_id = models.PositiveIntegerField('Produto ID')
    product_type = models.CharField('Tipo', max_length=25)
    details = models.CharField('Detalhes', max_length=25)
    measure = models.CharField('Medida', max_length=25)
    price = models.FloatField('Preço')
    amount = models.PositiveIntegerField('Quantidade')
    image = models.CharField('Imagem', max_length=2000)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


    def __str__(self):
        return self.user

class Date(models.Model):
    user = models.CharField('User', max_length=255)
    date = models.CharField('Date', max_length=20)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Datas'

    def __str__(self):
        return f'{self.user} | {self.date}'

