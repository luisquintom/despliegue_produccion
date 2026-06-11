# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-04

### Añadido (Added)
- **Despliegue:** Creación del archivo `Dockerfile` para empaquetar la aplicación en una imagen base de `python:3.12-slim`.
- **Datos iniciales:** Integración de comandos en el Dockerfile para ejecutar migraciones (`migrate`) y cargar datos de prueba (`loaddata`) todo automáticamente durante la construcción de la imagen.

### Cambiado (Changed)
- **Base de Datos:** Migración del motor de base de datos de MySQL a SQLite3 



