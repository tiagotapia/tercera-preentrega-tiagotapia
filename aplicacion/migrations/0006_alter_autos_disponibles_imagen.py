# Generated by Django 5.0.1 on 2024-02-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_autos_disponibles_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos_disponibles',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]