# Generated by Django 3.2 on 2020-11-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='user',
            new_name='usuario',
        ),
    ]
