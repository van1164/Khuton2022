# Generated by Django 3.2.13 on 2022-09-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0006_everytime_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='etc',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]