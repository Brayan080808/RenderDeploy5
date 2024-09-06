# Generated by Django 4.2 on 2024-08-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autenticacion', '0002_rename_id_usuario_usuarios_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='targeta',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]