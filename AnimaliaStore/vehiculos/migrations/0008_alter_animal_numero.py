# Generated by Django 4.2.2 on 2023-06-17 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0007_animal_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='numero',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]