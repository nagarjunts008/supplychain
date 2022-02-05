# Generated by Django 3.2 on 2021-04-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainapp', '0003_rename_manufacture_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
