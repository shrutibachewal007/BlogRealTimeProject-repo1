# Generated by Django 5.1.2 on 2024-10-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('sal', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
