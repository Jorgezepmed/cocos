# Generated by Django 3.0.3 on 2020-04-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20200404_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='cel',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]