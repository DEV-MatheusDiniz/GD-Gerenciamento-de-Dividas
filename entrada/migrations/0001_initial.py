# Generated by Django 4.1.2 on 2022-10-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('periodo', models.CharField(max_length=50)),
                ('recebido', models.BooleanField(default=False)),
            ],
        ),
    ]
