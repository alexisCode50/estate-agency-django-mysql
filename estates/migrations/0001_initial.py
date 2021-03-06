# Generated by Django 4.0.3 on 2022-04-07 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField()),
                ('opcion', models.IntegerField(choices=[[0, 'Venta'], [1, 'Renta']])),
                ('ubicacion', models.CharField(max_length=200)),
                ('destacado', models.BooleanField()),
                ('portada', models.ImageField(upload_to='covers')),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estates.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.ImageField(upload_to='extra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='estates.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensiones', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('cuartos', models.IntegerField()),
                ('ba??os', models.IntegerField()),
                ('garage', models.BooleanField()),
                ('picina', models.BooleanField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='estates.propiedad')),
            ],
        ),
    ]
