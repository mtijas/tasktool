# Generated by Django 5.0.1 on 2024-01-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0002_epic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
                'ordering': ['title'],
            },
        ),
    ]
