# Generated by Django 5.0.4 on 2024-05-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='level',
            field=models.IntegerField(editable=False, verbose_name='Уровень'),
        ),
    ]
