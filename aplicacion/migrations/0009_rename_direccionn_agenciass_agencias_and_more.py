# Generated by Django 5.0.1 on 2024-02-23 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_rename_agencias_agenciass_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenciass',
            old_name='direccionn',
            new_name='agencias',
        ),
        migrations.RenameField(
            model_name='agenciass',
            old_name='nombre_agenciass',
            new_name='dueño',
        ),
        migrations.RenameField(
            model_name='agenciass',
            old_name='imagenn',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='agenciass',
            old_name='nombre_dueñoo',
            new_name='local',
        ),
    ]