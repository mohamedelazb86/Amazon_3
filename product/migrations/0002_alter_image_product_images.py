# Generated by Django 4.2 on 2025-03-24 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_product',
            name='images',
            field=models.ImageField(upload_to='images'),
        ),
    ]
