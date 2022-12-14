# Generated by Django 4.1.1 on 2022-10-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0017_alter_capacitacion_nivel_alter_empleado_fechaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Maestría', 'Maestría'), ('Gestión', 'Gestión'), ('Técnico', 'Técnico'), ('Grado', 'Grado'), ('Post-grado', 'Post-grado'), ('Doctorado', 'Doctorado')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaIngreso',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
