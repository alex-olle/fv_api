# Generated by Django 5.0.3 on 2024-03-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0003_alter_fruit_options_remove_fruit_proximity'),
        ('months', '0005_alter_month_options'),
        ('vegetables', '0002_alter_vegetable_options_remove_vegetable_proximity'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='fruits',
            field=models.ManyToManyField(blank=True, related_name='fruits', to='fruits.fruit'),
        ),
        migrations.AddField(
            model_name='month',
            name='vegetables',
            field=models.ManyToManyField(blank=True, related_name='vegetables', to='vegetables.vegetable'),
        ),
    ]