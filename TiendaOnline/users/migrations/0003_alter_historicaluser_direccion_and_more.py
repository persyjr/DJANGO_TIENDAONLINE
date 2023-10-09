# Generated by Django 4.2.5 on 2023-10-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_historicalusers_historicaluser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='direccion',
            field=models.CharField(max_length=50, null=True, verbose_name='Domicilio Cliente'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='imagen',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='tel',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=50, null=True, verbose_name='Domicilio Cliente'),
        ),
        migrations.AlterField(
            model_name='user',
            name='imagen',
            field=models.ImageField(null=True, upload_to='servicios'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
