# Generated by Django 4.0.1 on 2022-02-25 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0002_product_created_product_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategorys',
            new_name='ProductCategories',
        ),
    ]
