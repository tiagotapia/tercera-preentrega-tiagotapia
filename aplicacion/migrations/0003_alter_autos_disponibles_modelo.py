# Generated by Django 5.0.1 on 2024-02-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_metodo_pago_efectivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos_disponibles',
            name='modelo',
            field=models.CharField(max_length=50),
        ),
    ]
