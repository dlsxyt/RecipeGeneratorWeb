# Generated by Django 2.1b1 on 2018-07-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canget',
            name='cal',
            field=models.PositiveIntegerField(),
        ),
    ]