# Generated by Django 3.1 on 2020-09-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('emri', models.CharField(max_length=255)),
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
