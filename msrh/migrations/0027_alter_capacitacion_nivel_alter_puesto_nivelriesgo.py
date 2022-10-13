# Generated by Django 4.1.1 on 2022-10-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0026_alter_capacitacion_nivel_alter_puesto_nivelriesgo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Grado', 'Grado'), ('Técnico', 'Técnico'), ('Post-grado', 'Post-grado'), ('Doctorado', 'Doctorado'), ('Gestión', 'Gestión'), ('Maestría', 'Maestría')], max_length=12, null=True, verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Medio', 'Medio'), ('Alto', 'Alto'), ('Bajo', 'Bajo')], max_length=5, null=True, verbose_name='Nivel Riesgo'),
        ),
    ]