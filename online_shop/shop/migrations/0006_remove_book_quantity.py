# Generated by Django 5.0.3 on 2024-03-27 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_order_book_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
    ]
