# Generated by Django 3.0.6 on 2020-07-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0003_auto_20200715_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='refrigerante',
            name='a',
            field=models.CharField(choices=[('1 l', '1 Litro'), ('2 l', '2 Litro'), ('KS', 'KS'), ('Lata', 'Lata'), ('Pequena', 'Pequena')], default=1, max_length=7, verbose_name='qq'),
            preserve_default=False,
        ),
    ]