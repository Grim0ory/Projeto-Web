# Generated by Django 4.2.7 on 2023-11-08 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbearia', '0002_alter_agenda_usuario_delete_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agenda',
        ),
    ]
