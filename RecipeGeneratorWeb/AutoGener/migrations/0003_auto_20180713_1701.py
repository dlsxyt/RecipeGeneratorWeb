# Generated by Django 2.1b1 on 2018-07-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGener', '0002_auto_20180713_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cando',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
