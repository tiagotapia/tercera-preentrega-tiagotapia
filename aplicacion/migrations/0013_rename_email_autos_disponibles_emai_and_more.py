# Generated by Django 5.0.1 on 2024-02-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_rename_imagenes_agencias_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='email',
            new_name='emai',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='imagen',
            new_name='ima',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='modelo',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='nombre_auto',
            new_name='nombre_aut',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='nombre_primer_dueño',
            new_name='nombre_primer_dueñ',
        ),
    ]
