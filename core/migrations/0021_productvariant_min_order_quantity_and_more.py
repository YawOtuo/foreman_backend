# Generated by Django 5.0.6 on 2024-07-19 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_cartitem_product_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='min_order_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='min_order_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='core.productvariant'),
        ),
    ]