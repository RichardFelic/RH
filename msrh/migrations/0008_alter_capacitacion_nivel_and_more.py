# Generated by Django 4.1.1 on 2022-10-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0007_rename_descripcompetencia_compentencia_descripcompetencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Grado', 'Grado'), ('Técnico', 'Técnico'), ('Maestría', 'Maestría'), ('Post-grado', 'Post-grado'), ('Gestión', 'Gestión'), ('Doctorado', 'Doctorado')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='puestoOcupado',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], max_length=5, null=True),
        ),
    ]
