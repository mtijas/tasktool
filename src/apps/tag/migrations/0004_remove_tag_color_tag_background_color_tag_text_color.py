# Generated by Django 5.0.1 on 2024-01-26 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_tag_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='color',
        ),
        migrations.AddField(
            model_name='tag',
            name='background_color',
            field=models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$')], verbose_name='background colour'),
        ),
        migrations.AddField(
            model_name='tag',
            name='text_color',
            field=models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator('^#(?:[0-9a-fA-F]{3}){1,2}$')], verbose_name='text colour'),
        ),
    ]
