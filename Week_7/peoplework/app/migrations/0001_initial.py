# Generated by Django 5.0.2 on 2024-03-10 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('person_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.works')),
            ],
        ),
    ]