# Generated by Django 3.2.13 on 2022-09-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TEST2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('updated_at', models.CharField(max_length=50)),
            ],
        ),
    ]
