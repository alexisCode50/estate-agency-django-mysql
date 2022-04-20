# Generated by Django 4.0.3 on 2022-04-20 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estates', '0007_alter_informacionextra_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='informacionextra',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='informacion', to=settings.AUTH_USER_MODEL),
        ),
    ]