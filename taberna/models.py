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

    preco_f = models.DecimalField('Preço Família', max_digits=8, decimal_places=2)
    preco_g = models.DecimalField('Preço Grande', max_digits=8, decimal_places=2)
    preco_m = models.DecimalField('Preço Média', max_digits=8, decimal_places=2)
    preco_p = models.DecimalField('Preço Pequena', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'