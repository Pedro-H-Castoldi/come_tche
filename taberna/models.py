from django.db import models
from stdimage.models import StdImageField
import uuid

def get_filename(_intance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}.{ext}'
    return filename

class Base(models.Model):

    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):

    produto = models.CharField('Produto', max_length=50)
    estoque = models.BooleanField('Estoque')
    imagem = StdImageField('Imagem', upload_to=get_filename, variations={'thumb': (124, 124)})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.produto

class Pizza(Produto):

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return self.produto

class PrecoPizza(Base):

    preco_f = models.DecimalField('Preço Família', max_digits=8, decimal_places=2, default=30.00)
    preco_g = models.DecimalField('Preço Grande', max_digits=8, decimal_places=2, default=25.00)
    preco_a = models.DecimalField('Preço Média', max_digits=8, decimal_places=2, default=20.00)
    preco_p = models.DecimalField('Preço Pequena', max_digits=8, decimal_places=2, default=15.00)
    preco_m = models.DecimalField('Preço Mini', max_digits=8, decimal_places=2, default=6.00)

    class Meta:
        verbose_name = 'Preço Pizza'
        verbose_name_plural = 'Preços Pizzas'

    def __str__(self):
        return 'Preços'

class Refrigerante(Produto):

    CHOICES = [
        ('1 l', '1 Litro'),
        ('2 l', '2 Litro'),
        ('KS', 'KS'),
        ('Lata', 'Lata'),
        ('Pequena', 'Pequena'),
    ]

    tipo = models.CharField('Tipo', choices=CHOICES, max_length=7)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Refrigerante'
        verbose_name_plural = 'Refrigerantes'

    def __str__(self):
        return self.produto

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
        ('varied', 'Variados'),
    ]
    category = models.CharField('Categoria', choices=CHOICES, max_length=10)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    liters = models.DecimalField('Litros/Ml', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

    def __str__(self):
        return self.produto