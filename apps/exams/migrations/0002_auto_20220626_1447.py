# Generated by Django 3.2.5 on 2022-06-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='bead',
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.CharField(max_length=10, verbose_name='Data de Realizacao'),
        ),
    ]
