# Generated by Django 3.0.6 on 2020-09-08 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0008_precopizza_preco_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taberna.Produto')),
                ('category', models.CharField(choices=[('beer', 'Cerveja'), ('whisky', 'Whisky'), ('vodka', 'Vodka'), ('energetic', 'Energético'), ('cognac', 'Conhaque'), ('cachaça', 'Cachaça'), ('rum', 'Rum'), ('varied', 'Variados')], max_length=10, verbose_name='Categoria')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('liters', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Litros/Ml')),
            ],
            options={
                'verbose_name': 'Bebida',
                'verbose_name_plural': 'Bebidas',
            },
            bases=('taberna.produto',),
        ),
    ]
