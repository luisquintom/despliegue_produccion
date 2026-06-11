# Imagen base 
FROM python:3.12-slim

# Variables de entorno 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutamos migraciones para crear db.sqlite3
RUN python manage.py migrate

# Cargamos datos de prueba 
RUN python manage.py loaddata datos_prueba.json

#  puerto
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]