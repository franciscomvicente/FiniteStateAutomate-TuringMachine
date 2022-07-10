# Generated by Django 4.0 on 2021-12-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AFD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('alfabeto', models.CharField(max_length=200)),
                ('estados', models.CharField(max_length=200)),
                ('estadoinicial', models.CharField(max_length=200)),
                ('estadosdeaceitacao', models.CharField(max_length=200)),
                ('tabeladetransicoes', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='TM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('estados', models.CharField(max_length=200)),
                ('estadoinicial', models.CharField(max_length=200)),
                ('estadodeaceitacao', models.CharField(max_length=200)),
                ('tabeladetransicoes', models.CharField(max_length=600)),
            ],
        ),
    ]
