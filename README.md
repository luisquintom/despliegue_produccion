
## APP-SPACES en contenedor docker

# Construye la imagen
docker build -t mi-app .

# Levanta el contenedor en segundo plano:
docker run -d -p 8000:8000 mi-app

### Panel de Administración
* **Admin Django:** (http://127.0.0.1:8000/admin/)

### Gestión de Usuarios
* **Registrar Usuario:** `http://127.0.0.1:8000/api/usuarios/registrar/`

### Agencias Espaciales
* **Listar Agencias:** `http://127.0.0.1:8000/api/espacio/agencias/`


### Misiones Espaciales (ViewSet)
* **Listar Misiones:** `http://127.0.0.1:8000/api/espacio/misiones-viewset/`
* **Crear Misión:** `http://127.0.0.1:8000/api/espacio/misiones-viewset/`
* **Detalle de Misión:** `http://127.0.0.1:8000/api/espacio/misiones-viewset/<id>/`
