# Generated by Django 4.1.2 on 2022-11-16 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_comison_curso_comision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='profesion',
        ),
    ]
