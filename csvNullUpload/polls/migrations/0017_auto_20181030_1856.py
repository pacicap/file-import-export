# Generated by Django 2.1.2 on 2018-10-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20181030_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='Title',
            field=models.CharField(max_length=300),
        ),
    ]
