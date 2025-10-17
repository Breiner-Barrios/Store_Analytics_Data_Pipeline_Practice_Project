# Store Analytics - Data Pipeline Practice Project

Este proyecto implementa una pipeline de datos completa para una tienda ficticia. Incluye scripts para generar datos sintéticos, poblar una base de datos PostgreSQL, ejecutar consultas analíticas, visualizar los resultados y explorarlos de forma interactiva.

## Características

- **Generación de Datos**: Crea datos falsos realistas para clientes, productos y ventas.
- **Persistencia de Datos**: Carga los datos generados en una base de datos PostgreSQL.
- **Análisis de Datos**: Ejecuta consultas complejas para obtener información de negocio, como los productos más vendidos y las tendencias de ventas.
- **Visualización de Datos**: Genera gráficos informativos a partir de los datos analizados.
- **Exploración Interactiva**: Un Jupyter Notebook para análisis y visualización en tiempo real.

---

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- **Python 3.8+**
- **PostgreSQL**: Un servidor de base de datos PostgreSQL en funcionamiento.

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto.

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Breiner-Barrios/Store_Analytics_Data_Pipeline_Practice_Project.git
```

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

### 3. Instalar Dependencias

Instala todas las librerías de Python necesarias.

```bash
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos

**a. Crear las Tablas:**
Necesitas ejecutar el script SQL para crear el esquema y las tablas en tu base de datos. Puedes usar una herramienta como `psql`, DBeaver, o pgAdmin.

- Conéctate a tu servidor PostgreSQL.
- Ejecuta el contenido del archivo `database/script.sql`. Esto creará el esquema `store_analytics` y las tablas `customers`, `products` y `sales`.

**b. Configurar la Conexión:**
Crea un archivo llamado `.env` en la raíz del proyecto. Puedes copiar el archivo `.env.example` como plantilla.

```bash
# Copia la plantilla (en Windows)
copy .env.example .env

# Copia la plantilla (en macOS/Linux)
cp .env.example .env
```

---

## 🚀 Uso del Proyecto (Poblar las Tablas)

El proceso para poblar la base de datos se divide en dos pasos:

### Paso 1: Generar los Archivos CSV

Ejecuta el script `mainwithout.py` para generar los datos de prueba. El script te pedirá que introduzcas el número de registros que deseas para clientes, productos y ventas.

```bash
python mainwithout.py
```

Esto creará (o sobrescribirá) los archivos `customers.csv`, `products.csv` y `sales.csv` dentro de una carpeta `seeders/`.

### Paso 2: Cargar los Datos a la Base de Datos

Una vez que los archivos CSV estén listos, ejecuta el script `load_data.py` para cargarlos en tus tablas de PostgreSQL.

```bash
python load_data.py
```

El script leerá los archivos de la carpeta `seeders/` y los insertará en el orden correcto para respetar las claves foráneas.

---

## 📊 Ejecutar Consultas de Análisis

Para ver los resultados de los análisis de datos (ej. productos más vendidos, tendencias mensuales), ejecuta el script `query_data.py`.

```bash
python query_data.py
```


## 📈 Visualizar los Datos

Para generar los gráficos basados en los análisis (productos más vendidos, tendencia mensual, etc.), ejecuta el script `visualize_data.py`.

```bash
python visualize_data.py
```

## 🔬 Análisis Interactivo con Jupyter Notebook

El archivo `query_data_notebook.ipynb` te permite explorar los datos y las funciones de consulta de forma interactiva. Es ideal para probar nuevas consultas o realizar análisis exploratorios sobre la marcha.

Para usarlo, asegúrate de tener Jupyter instalado (`pip install notebook`) y ejecuta el siguiente comando en tu terminal.

