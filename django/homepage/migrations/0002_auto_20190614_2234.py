# Generated by Django 2.2 on 2019-06-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerystore',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
