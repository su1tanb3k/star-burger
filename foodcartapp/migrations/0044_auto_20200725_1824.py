# Generated by Django 3.0.7 on 2020-07-25 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0043_auto_20200725_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('online', 'Электронно'), ('cash', 'Наличностью')], default='cash', max_length=20, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 25, 18, 24, 30, 438490), verbose_name='Дата создания заказа'),
        ),
    ]
