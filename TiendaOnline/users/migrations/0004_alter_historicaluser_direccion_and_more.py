# Generated by Django 4.2.5 on 2023-10-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_historicaluser_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Domicilio Cliente'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='imagen',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='tel',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Domicilio Cliente'),
        ),
        migrations.AlterField(
            model_name='user',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
