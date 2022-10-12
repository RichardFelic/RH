# Generated by Django 4.1.1 on 2022-10-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msrh', '0009_remove_candidato_principalescapacitacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='principalesCapacitacion',
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nivel',
            field=models.CharField(choices=[('Post-grado', 'Post-grado'), ('Grado', 'Grado'), ('Maestría', 'Maestría'), ('Gestión', 'Gestión'), ('Doctorado', 'Doctorado'), ('Técnico', 'Técnico')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='nivelRiesgo',
            field=models.CharField(choices=[('Medio', 'Medio'), ('Bajo', 'Bajo'), ('Alto', 'Alto')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='candidato',
            name='principalesCapacitacion',
            field=models.ManyToManyField(to='msrh.capacitacion'),
        ),
    ]