# Generated by Django 2.1b1 on 2018-07-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGener', '0006_compose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compose',
            name='ingre',
        ),
        migrations.AddField(
            model_name='compose',
            name='ingre',
            field=models.ManyToManyField(to='AutoGener.CanGet'),
        ),
    ]