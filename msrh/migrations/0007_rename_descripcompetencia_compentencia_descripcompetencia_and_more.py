# Generated by Django 4.1.1 on 2022-10-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0006_alter_capacitacion_nivel_alter_puesto_nivelriesgo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compentencia',
            old_name='DescripCompetencia',
            new_name='descripCompetencia',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='puestoAspira',
            new_name='puesto',
        ),
        migrations.AddField(
            model_name='candidato',
            name='expeiencia',
            field=models.ManyToManyField(to='msrh.experiencialaboral'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='recomendacion',
            field=models.ManyToManyField(to='msrh.empleado'),
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Gestión', 'Gestión'), ('Grado', 'Grado'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado'), ('Post-grado', 'Post-grado'), ('Técnico', 'Técnico')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Alto', 'Alto'), ('Bajo', 'Bajo'), ('Medio', 'Medio')], max_length=5, null=True),
        ),
    ]