# Generated by Django 3.0.3 on 2020-04-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0011_auto_20200408_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rutas',
            options={'ordering': ['ruta'], 'verbose_name': 'Rutas', 'verbose_name_plural': 'Rutas'},
        ),
        migrations.AlterField(
            model_name='rutas',
            name='ruta',
            field=models.CharField(choices=[('1', 'Ruta 10'), ('0', 'Ruta 6'), ('3', 'Ruta 1'), ('2', 'Ruta 8')], max_length=1, verbose_name='Ruta'),
        ),
    ]
