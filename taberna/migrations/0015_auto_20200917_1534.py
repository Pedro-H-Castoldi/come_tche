# Generated by Django 3.0.6 on 2020-09-17 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0014_auto_20200917_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precopizza',
            old_name='criado',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='modificado',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='preco_a',
            new_name='price_a',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='preco_g',
            new_name='price_b',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='preco_f',
            new_name='price_f',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='preco_m',
            new_name='price_m',
        ),
        migrations.RenameField(
            model_name='precopizza',
            old_name='preco_p',
            new_name='price_s',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='criado',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='imagem',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='modificado',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='produto',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='refrigerante',
            old_name='preco',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='refrigerante',
            old_name='tipo',
            new_name='type',
        ),
    ]
