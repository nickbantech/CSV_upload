# Generated by Django 4.0.3 on 2022-03-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvfiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_state',
            field=models.CharField(max_length=50),
        ),
    ]
