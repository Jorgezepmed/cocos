# Generated by Django 3.0.3 on 2020-04-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutas',
            name='ruta',
            field=models.CharField(choices=[('2', 'Ruta 8'), ('0', 'Ruta 6'), ('1', 'Ruta 10'), ('3', 'Ruta 1')], max_length=1, verbose_name='Ruta'),
        ),
    ]
