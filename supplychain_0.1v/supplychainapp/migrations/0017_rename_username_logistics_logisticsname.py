# Generated by Django 3.2 on 2021-05-01 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainapp', '0016_logistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logistics',
            old_name='username',
            new_name='logisticsname',
        ),
    ]
