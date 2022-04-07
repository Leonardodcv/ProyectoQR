# Generated by Django 2.2.13 on 2021-07-18 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=220)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad o Stock')),
                ('imagen', models.ImageField(blank=True, max_length=255, null=True, upload_to='libros/', verbose_name='Imagen')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_dias', models.SmallIntegerField(default=7, verbose_name='Cantidad de Dias a Reservar')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_vencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento de la reserva')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Libro')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
