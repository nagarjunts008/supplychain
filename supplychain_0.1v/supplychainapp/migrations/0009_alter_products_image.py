# Generated by Django 3.2 on 2021-04-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainapp', '0008_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]