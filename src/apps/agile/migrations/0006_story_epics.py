# Generated by Django 5.0.1 on 2024-01-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0005_epic_description_theme_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='epics',
            field=models.ManyToManyField(to='agile.epic'),
        ),
    ]