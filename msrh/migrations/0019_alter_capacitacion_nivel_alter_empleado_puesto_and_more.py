# Generated by Django 4.1.1 on 2022-10-12 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0018_alter_capacitacion_nivel_alter_empleado_fechaingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Doctorado', 'Doctorado'), ('Grado', 'Grado'), ('Gestión', 'Gestión'), ('Técnico', 'Técnico'), ('Post-grado', 'Post-grado'), ('Maestría', 'Maestría')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='msrh.puesto'),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Medio', 'Medio'), ('Alto', 'Alto'), ('Bajo', 'Bajo')], max_length=5, null=True),
        ),
    ]
