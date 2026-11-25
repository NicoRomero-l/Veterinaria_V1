
import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'categoría',
                'verbose_name_plural': 'categorías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otra', 'Otra')], max_length=10)),
                ('propietario', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascotas',
                'ordering': ['nombre', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servicios', to='veterinaria_servicios.categoria')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='citas_creadas', to=settings.AUTH_USER_MODEL)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='citas', to='veterinaria_servicios.mascota')),
                ('servicios', models.ManyToManyField(related_name='citas', to='veterinaria_servicios.servicio')),
            ],
            options={
                'verbose_name': 'cita',
                'verbose_name_plural': 'citas',
                'ordering': ['-fecha', '-pk'],
            },
        ),
    ]
