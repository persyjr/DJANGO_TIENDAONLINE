# Generated by Django 4.2.5 on 2023-10-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_historicaluser_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='nombre',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]