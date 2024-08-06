# Generated by Django 5.0.7 on 2024-07-31 12:17

import products.utitls
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_category_level_remove_category_lft_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='poroduct',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rank',
            field=models.IntegerField(validators=[products.utitls.validate_rating], verbose_name='rank'),
        ),
    ]
