# Generated by Django 5.0.1 on 2024-02-26 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_rename_email_autos_disponibles_emai_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='emai',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='ima',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='model',
            new_name='modelo',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='nombre_aut',
            new_name='nombre_auto',
        ),
        migrations.RenameField(
            model_name='autos_disponibles',
            old_name='nombre_primer_dueñ',
            new_name='nombre_primer_dueño',
        ),
    ]