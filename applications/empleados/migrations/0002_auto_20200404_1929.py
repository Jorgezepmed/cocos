# Generated by Django 3.0.3 on 2020-04-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='cel',
            field=models.IntegerField(max_length=50, verbose_name='Telefono'),
        ),
    ]