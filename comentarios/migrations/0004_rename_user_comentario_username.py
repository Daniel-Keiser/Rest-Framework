# Generated by Django 3.2 on 2020-11-24 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_rename_usuario_comentario_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='user',
            new_name='username',
        ),
    ]
