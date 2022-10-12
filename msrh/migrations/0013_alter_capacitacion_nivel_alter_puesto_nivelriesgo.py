# Generated by Django 4.1.1 on 2022-10-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0012_remove_candidato_puestoaspira_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Técnico', 'Técnico'), ('Doctorado', 'Doctorado'), ('Grado', 'Grado'), ('Maestría', 'Maestría'), ('Gestión', 'Gestión'), ('Post-grado', 'Post-grado')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo')], max_length=5, null=True),
        ),
    ]
