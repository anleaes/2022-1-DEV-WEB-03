# Generated by Django 3.2.5 on 2022-06-26 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacients', '0001_initial'),
        ('exams', '0003_alter_exam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='pacient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pacients.pacient'),
            preserve_default=False,
        ),
    ]
