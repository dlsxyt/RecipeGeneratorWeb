# Generated by Django 2.1b1 on 2018-07-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGener', '0007_auto_20180718_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compose',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='compose',
            name='ingre',
        ),
        migrations.AddField(
            model_name='cando',
            name='ingre',
            field=models.ManyToManyField(to='AutoGener.CanGet'),
        ),
        migrations.DeleteModel(
            name='Compose',
        ),
    ]
