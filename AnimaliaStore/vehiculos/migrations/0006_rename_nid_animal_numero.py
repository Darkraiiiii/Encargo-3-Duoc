# Generated by Django 4.2.2 on 2023-06-17 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_alter_animal_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='nid',
            new_name='numero',
        ),
    ]