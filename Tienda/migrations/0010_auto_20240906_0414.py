# Generated by Django 5.1.1 on 2024-09-06 02:14

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0009_rename_valoracion_products_rating'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS pg_trgm;"),
    ]