# Generated by Django 2.2 on 2019-06-15 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20190614_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Store_A_Bombastic',
            new_name='Store',
        ),
    ]
