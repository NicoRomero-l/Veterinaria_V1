# Veterinaria

Aplicación de servicios veterinarios. Permite consultar categorías, servicios y mascotas, y gestionar categorías y citas según los permisos del usuario.

## Modelo de datos

| Tabla | Contenido | Relaciones |
| --- | --- | --- |
| Categoría | Nombre y descripción | Una categoría tiene muchos servicios |
| Servicio | Nombre y precio decimal | Pertenece a una categoría y puede aparecer en varias citas |
| Mascota | Nombre, especie y propietario | Una mascota puede tener varias citas |
| Cita | Fecha | Pertenece a una mascota, incluye varios servicios y conserva su usuario creador |

Las llaves foráneas usan `PROTECT` para evitar borrar categorías, mascotas o usuarios con registros asociados. Django crea la tabla intermedia de la relación entre citas y servicios.

## Levantar el proyecto

Desde la carpeta que contiene `manage.py`, con Python 3.12 o posterior:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo
python manage.py check
python manage.py runserver
```

Si tu terminal es Fish, usa `source venv/bin/activate.fish`. Abre http://127.0.0.1:8000/ y entra al panel de Django desde http://127.0.0.1:8000/admin/.


## Estructura

```text
config/
veterinaria_servicios/
    models/
    forms/
    views/
    urls/
    templates/veterinaria_servicios/
    migrations/
manage.py
requirements.txt
```

La vista de cada entidad se conecta con su archivo de rutas. Las plantillas de cada entidad viven en una subcarpeta propia. `views/auth_views.py` contiene el registro y las funciones de sesión.
