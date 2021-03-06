# Generated by Django 2.1b1 on 2018-07-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('荤', '荤'), ('素', '素'), ('both', 'both'), ('暂不选择', '暂不选择'), ('主食', '主食')], default='暂不选择', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CanGet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cal', models.PositiveIntegerField(help_text='千卡/100g')),
            ],
        ),
    ]
