# Generated by Django 4.0.3 on 2022-08-08 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_cart_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
