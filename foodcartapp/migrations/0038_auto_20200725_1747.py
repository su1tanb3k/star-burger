# Generated by Django 3.0.7 on 2020-07-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0037_orderproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('unprocessed', 'Необработанный'), ('processed', 'Обработанный')], default='unprocessed', max_length=20, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='цена'),
        ),
    ]
