# Generated by Django 5.0.1 on 2024-01-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
            ],
            options={
                'verbose_name': 'theme',
                'verbose_name_plural': 'themes',
                'ordering': ['title'],
            },
        ),
    ]