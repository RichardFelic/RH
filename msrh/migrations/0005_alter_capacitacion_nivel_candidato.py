# Generated by Django 4.1.1 on 2022-09-30 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0004_puesto_alter_capacitacion_capacitacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Post-grado', 'Post-grado'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado'), ('Grado', 'Grado'), ('Gestión', 'Gestión'), ('Técnico', 'Técnico')], max_length=12, null=True),
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(max_length=10, null=True)),
                ('nombre', models.CharField(max_length=60, null=True)),
                ('departamento', models.CharField(max_length=60, null=True)),
                ('salarioAspira', models.DecimalField(decimal_places=2, max_digits=10)),
                ('principalesCapacitacion', models.ManyToManyField(to='msrh.capacitacion')),
                ('principalesCompetencia', models.ManyToManyField(to='msrh.compentencia')),
                ('puestoAspira', models.ManyToManyField(to='msrh.puesto')),
            ],
        ),
    ]
