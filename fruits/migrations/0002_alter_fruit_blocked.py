# Generated by Django 5.0.3 on 2024-03-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='blocked',
            field=models.BooleanField(default=True),
        ),
    ]
