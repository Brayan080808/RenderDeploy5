# Generated by Django 4.2 on 2023-08-21 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_producto',
            fields=[
                ('id_categoria_producto', models.AutoField(primary_key=True, serialize=False)),
                ('name_categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proovedores',
            fields=[
                ('id_proveedores', models.AutoField(primary_key=True, serialize=False)),
                ('name_proovedor', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('name_producto', models.CharField(max_length=30)),
                ('Descripcion', models.CharField(default='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sequi, beatae. Nobis adipisci sint assumenda? Culpa beatae, fugiat et, eos, blanditiis eligendi sint odit pariatur soluta dolor delectus nam iure iusto.', max_length=255)),
                ('precio', models.IntegerField()),
                ('valoracion', models.IntegerField()),
                ('cantidad_disponible', models.IntegerField()),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.categoria_producto')),
                ('proovedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.proovedores')),
            ],
        ),
    ]
