Claro, aquí tienes el README con las imágenes más pequeñas y organizadas:

---

# NoteFlow

**NoteFlow** es una aplicación de administración de tareas y notas, que permite a los usuarios gestionar sus pendientes y obtener información climática de diferentes ciudades. La interfaz gráfica está construida con la biblioteca `customtkinter`, proporcionando una experiencia de usuario moderna y atractiva.

## Funcionalidades

- **Gestión de Tareas y Notas:**
  - Crear y organizar tareas en una lista de pendientes.
  - Añadir notas para cada tarea.
  - Eliminar tareas completadas o no deseadas.
  - Guardar el estado de las tareas (seleccionadas o no seleccionadas).

- **Información Climática:**
  - Consultar el clima actual de cualquier ciudad.
  - Mostrar la temperatura actual, temperatura máxima y una descripción del clima.
  - Traducción automática de la descripción del clima al español.

- **Configuración:**
  - Cambiar la apariencia de la aplicación (modos claro, oscuro o sistema).
  - Acceso a enlaces de contacto y soporte.
  - Cerrar sesión y advertencias sobre la pérdida de datos.

## Requisitos

- Python 3.x
- Bibliotecas necesarias: `requests`, `customtkinter`, `datetime`, `webbrowser`, `screeninfo`, `googletrans`, `sqlalchemy`.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias con el siguiente comando:

   ```
   pip install requests customtkinter googletrans screeninfo sqlalchemy
   ```

3. Asegúrate de tener configuradas las bases de datos necesarias (`User`, `UserTokens`, `User_values`) y las sesiones de SQLAlchemy correspondientes.

## Uso

1. Ejecuta la aplicación con el siguiente comando:

   ```
   python nombre_del_archivo.py
   ```

2. La aplicación se abrirá con la interfaz gráfica principal, mostrando las opciones de gestión de tareas y la búsqueda de información climática.

3. Agrega tareas y notas a través de la sección correspondiente, y consulta el clima ingresando el nombre de una ciudad.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía tus cambios al repositorio (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia [MIT](https://opensource.org/licenses/MIT).

## Capturas de Pantalla

### Interfaz login
![IMG-20230919-WA0002](https://github.com/user-attachments/assets/9403c101-2d65-4528-ac36-6081f42e9490)

### Interfaz login
![IMG-20230919-WA0011](https://github.com/user-attachments/assets/4ca0aaed-47fa-438d-bf74-3d22f7d89119)

### Interfaz login
![IMG-20230919-WA0009](https://github.com/user-attachments/assets/aa2170cb-db1c-4fef-ba1c-bd71b1271e36)

### Interfaz login
![IMG-20230919-WA0008](https://github.com/user-attachments/assets/77cacc0a-4a7d-4efd-b411-2973a4df0b46)

### Interfaz principal
![IMG-20230919-WA0005](https://github.com/user-attachments/assets/9b3f69a9-528d-4356-b500-0432f14495a5)

### Interfaz principal
![IMG-20230919-WA0003](https://github.com/user-attachments/assets/0a180a49-b7a5-452a-9973-5424a7b035ba)

---

Recuerda ajustar la información según el contenido y las especificaciones reales de tu aplicación.
