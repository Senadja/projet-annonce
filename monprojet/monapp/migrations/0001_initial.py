# Generated by Django 3.2.24 on 2024-02-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaModele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ1', models.CharField(max_length=100)),
                ('champ2', models.IntegerField()),
                ('champ3', models.DateTimeField()),
            ],
        ),
    ]
