# Generated by Django 4.2.2 on 2023-06-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_rename_nid_animal_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]