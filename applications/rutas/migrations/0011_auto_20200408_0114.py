# Generated by Django 3.0.3 on 2020-04-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0010_auto_20200407_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutas',
            name='ruta',
            field=models.CharField(choices=[('3', 'Ruta 1'), ('1', 'Ruta 10'), ('0', 'Ruta 6'), ('2', 'Ruta 8')], max_length=1, verbose_name='Ruta'),
        ),
    ]
