# Generated by Django 5.0.3 on 2024-03-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0004_remove_month_fruits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='month',
            options={'ordering': ['number']},
        ),
    ]
