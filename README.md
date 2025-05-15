# Prueba Técnica ETL y API - Proyecto

Este proyecto contiene dos partes:

1. Proceso ETL para cargar, transformar y almacenar información de compras en MySQL.
2. API para encontrar el número faltante de un conjunto de los primeros 100 números.

## Parte 1: ETL con Python y MySQL

### Requisitos previos

- MySQL instalado y corriendo.
- Python 3.8+ instalado.
- `pip` para instalar paquetes.

### Archivos relevantes

- `data_prueba_tecnica.csv`: Dataset de compras.
- `database.sql`: Script para crear base de datos y tablas.
- `main_etl.py`: Script ETL para cargar y transformar datos.
- `.env`: Archivo con configuración de conexión a MySQL.

### Pasos para ejecutar

1. Crear la base de datos y tablas:
   ```bash
   mysql -u root -p < database.sql

   ## Sección 2: Creación de una API

### 🎯 Objetivo
Crear una API que represente un conjunto de los primeros 100 números naturales y sea capaz de:
- Extraer uno de ellos.
- Calcular cuál fue el número extraído.
- Validar entradas.
- Ejecutarse desde línea de comandos con argumentos.

---

### 🧱 Implementación

El archivo principal es: `missing_number_api.py`.

Implementa una clase llamada `NumberSet` con las siguientes funcionalidades:

- `extract(number)`: Extrae un número del conjunto.
- `find_missing()`: Calcula cuál número fue extraído.
- Validación para garantizar que el número esté en el rango 1–100.

---

### ⚙️ Cómo ejecutar

Desde la terminal, navega al directorio donde está el archivo y ejecuta:

```bash
python missing_number_api.py 37

