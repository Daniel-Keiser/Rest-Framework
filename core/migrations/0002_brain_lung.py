# Generated by Django 3.2 on 2020-11-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lung', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brain',
            name='lung',
            field=models.ManyToManyField(to='lung.Lung'),
        ),
    ]
