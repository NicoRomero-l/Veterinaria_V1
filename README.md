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

`migrate` crea los grupos y sus permisos. `cargar_demo` carga cinco registros por modelo en una base vacía y puede ejecutarse de nuevo.

## Cuentas de prueba locales

| Usuario | Grupo o rol | Contraseña |
| --- | --- | --- |
| superdemo | Superusuario | `VetSuper2026!` |
| administrador_demo | administradores | `VetAdmin2026!` |
| consultor_demo | consultores | `VetConsulta2026!` |
| administrador_aux | administradores | `VetAux2026!` |

Los consultores pueden leer citas. Los administradores pueden crear categorías y citas, editar y eliminar categorías disponibles, y editar y eliminar sus propias citas. El superusuario puede gestionar cualquier cita y acceder al panel de Django. El registro web asigna el grupo `consultores`.

Para probar la propiedad, abre una cita de demostración como `administrador_demo` y copia la URL de edición. Entra como `administrador_aux` y vuelve a abrir esa URL. Django devuelve 403. Si creas una cita con esa segunda cuenta, podrás editarla desde su detalle.

## Estructura

```text
config/
veterinaria_servicios/
    models/
    forms/
    views/
    urls/
    templates/veterinaria_servicios/
    management/commands/
    migrations/
manage.py
requirements.txt
```

La vista de cada entidad se conecta con su archivo de rutas. Las plantillas de cada entidad viven en una subcarpeta propia. `views/auth_views.py` contiene el registro y las funciones de sesión.
