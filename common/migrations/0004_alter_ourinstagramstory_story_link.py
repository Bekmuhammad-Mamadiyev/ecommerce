# Generated by Django 5.0.7 on 2024-07-31 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_country_options_alter_customerfeedback_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourinstagramstory',
            name='story_link',
            field=models.URLField(validators=[django.core.validators.URLValidator(schemes=['https://instagram.com'])], verbose_name='Story Link'),
        ),
    ]
