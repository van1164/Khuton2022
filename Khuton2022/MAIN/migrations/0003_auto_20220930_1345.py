# Generated by Django 3.2.13 on 2022-09-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_dahwe_subject_table_timetable_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Win',
        ),
        migrations.AddField(
            model_name='user',
            name='Win',
            field=models.ManyToManyField(to='MAIN.Dahwe'),
        ),
    ]
