# Generated by Django 2.1.2 on 2018-10-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181010_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='output',
            fields=[
                ('Number', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('DateDeCoupure', models.CharField(max_length=500)),
                ('DateDeRetablisement', models.CharField(max_length=500)),
                ('Duree', models.CharField(max_length=500)),
                ('client', models.CharField(max_length=500)),
                ('camtel', models.CharField(max_length=500)),
                ('observation', models.CharField(max_length=500)),
            ],
        ),
    ]
