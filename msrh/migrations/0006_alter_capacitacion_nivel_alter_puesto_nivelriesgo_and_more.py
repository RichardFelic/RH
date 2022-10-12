# Generated by Django 4.1.1 on 2022-09-30 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0005_alter_capacitacion_nivel_candidato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Técnico', 'Técnico'), ('Grado', 'Grado'), ('Post-grado', 'Post-grado'), ('Gestión', 'Gestión'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Medio', 'Medio'), ('Bajo', 'Bajo'), ('Alto', 'Alto')], max_length=5, null=True),
        ),
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200, null=True)),
                ('fechaDesde', models.DateField()),
                ('fechaHasta', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('puestoOcupado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='msrh.puesto')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, null=True)),
                ('cedula', models.IntegerField(max_length=10, null=True)),
                ('fechaIngreso', models.DateField()),
                ('departamento', models.CharField(max_length=50, null=True)),
                ('salarioMensual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=False)),
                ('puestoAspira', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='msrh.puesto')),
            ],
        ),
    ]