# Generated by Django 4.1.2 on 2022-10-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada_total', models.FloatField(blank=True, null=True)),
                ('saida_total', models.FloatField(blank=True, null=True)),
                ('saldo', models.FloatField()),
                ('periodo', models.CharField(max_length=50)),
            ],
        ),
    ]
