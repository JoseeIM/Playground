# Generated by Django 4.1.2 on 2022-12-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_duda'),
    ]

    operations = [
        migrations.AddField(
            model_name='duda',
            name='asunto',
            field=models.CharField(default='nada', max_length=40),
        ),
        migrations.AddField(
            model_name='duda',
            name='desarrollo',
            field=models.CharField(default='nada', max_length=1000),
        ),
        migrations.AddField(
            model_name='duda',
            name='materia',
            field=models.CharField(default='nada', max_length=40),
        ),
    ]
