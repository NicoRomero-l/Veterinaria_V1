# Veterinaria Django

La carpeta que contiene manage.py es la raíz. Esta copia usa config/settings.py. En VS Code abre esa raíz, activa tu entorno virtual y verifica qué intérprete usas con python -m django --version.

## Antes de pegar código

Conserva tu proyecto actual como referencia. Los archivos de esta guía están organizados por ruta. El archivo settings.py incluido tiene una clave de desarrollo de ejemplo. Si integras sobre tu copia local, conserva tu propia clave y ajusta solo INSTALLED_APPS y las tres opciones de sesión. Las cuentas de carga son de demostración local.

## Las nueve evidencias

1. Estructura. Cuando estén colocados todos los archivos, abre el explorador de VS Code y expande veterinaria_servicios/models, forms, views y urls. Deben verse los archivos por entidad y sus __init__.py.
2. Migraciones. Después de pegar modelos y antes de cargar datos, ejecuta python manage.py makemigrations veterinaria_servicios y python manage.py migrate en una copia de trabajo con base nueva. Captura los cuatro Create model del primer comando y Applying veterinaria_servicios.0001_initial... OK del segundo. Si la migración ya está generada, consérvala en tu repositorio y reproduce la evidencia en una copia desechable de la app con solo migrations/__init__.py y sin db.sqlite3.
3. CRUD principal. Tras ejecutar python manage.py cargar_demo y python manage.py runserver, entra como administrador_demo. Abre /citas/ y luego Nueva cita. Toma una imagen de cada pantalla y ponlas juntas como evidencia 3.
4. Mensaje. En el formulario elige una mascota, uno o más servicios y una fecha. Pulsa Guardar y captura «Registro creado.» en el listado antes de navegar.
5. Registro y sesión. Cierra sesión, abre /registro/ y captura el formulario. Registra una cuenta de prueba nueva, inicia sesión y captura la barra con su usuario y el botón Salir. Agrupa ambas imágenes y evita mostrar la contraseña.
6. Comparación. Como administrador_demo abre el detalle de una cita de demostración y captura Editar y Eliminar. En una ventana privada entra como consultor_demo, abre la misma URL y captura el detalle con el nombre del consultor visible. Agrupa ambas imágenes.
7. Acceso directo. Como consultor_demo pega la URL de Editar que copiaste del administrador, /citas/<id>/editar/. Captura la barra de direcciones y la página 403.
8. Admin. En /admin/ entra como superdemo y captura el índice con Categorías, Mascotas, Servicios y Citas. Abre Citas y muestra sus filtros de fecha y servicios. Agrupa ambas imágenes.
9. Historial. Después de tus commits de avance, ejecuta git log --oneline -n 12 y captura al menos ocho commits reales. Usa etapas como configuración, modelos, migración, formularios, vistas y rutas, plantillas, acceso, admin y datos, y README.

## Cuentas demo

| Usuario | Contraseña |
| --- | --- |
| administrador_demo | VetAdmin2026! |
| consultor_demo | VetConsulta2026! |
| administrador_aux | VetAux2026! |
| superdemo | VetSuper2026! |

