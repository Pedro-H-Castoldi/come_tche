# Generated by Django 3.0.6 on 2020-07-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0004_refrigerante_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refrigerante',
            name='a',
        ),
        migrations.AddField(
            model_name='refrigerante',
            name='tipo',
            field=models.CharField(choices=[('1 l', '1 Litro'), ('2 l', '2 Litro'), ('KS', 'KS'), ('Lata', 'Lata'), ('Pequena', 'Pequena')], default=1, max_length=7, verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]