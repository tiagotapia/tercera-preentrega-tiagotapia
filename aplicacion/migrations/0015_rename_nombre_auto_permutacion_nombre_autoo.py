# Generated by Django 5.0.1 on 2024-02-26 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_rename_emai_autos_disponibles_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permutacion',
            old_name='nombre_auto',
            new_name='nombre_autoo',
        ),
    ]
