# Proyecto Autos

## Descripción

Proyecto de Ingeniería de Datos y Desarrollo de Aplicaciones para el análisis de vehículos mediante procesos ETL, almacenamiento en base de datos, API REST, visualización interactiva y despliegue con Docker.

El sistema integra múltiples fuentes de datos, realiza procesos de limpieza y transformación, almacena la información consolidada y permite su consulta mediante una API y un dashboard interactivo.

---

## Arquitectura del Proyecto

```text
Fuentes CSV
    │
    ▼
Proceso ETL
(Limpieza y Transformación)
    │
    ▼
Base de Datos SQLite
    │
    ▼
Dataset Final
    │
    ├──────────────► API FastAPI
    │
    └──────────────► Dashboard Streamlit
```

---

## Estructura del Proyecto

```text
Proyecto_autos/
│
├── api/
│   └── api.py
│
├── dashboards/
│   └── dashboard.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docker/
│   └── dockerfile
│
├── docs/
│
├── etl/
│   └── etl_final.py
│
├── scripts/
│
├── tests/
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Tecnologías Utilizadas

* Python
* Pandas
* SQLite
* FastAPI
* Streamlit
* Plotly
* Requests
* Docker
* Docker Compose

---

## Fuentes de Datos

El proyecto integra múltiples conjuntos de datos de vehículos:

* car data.csv
* CAR DETAILS FROM CAR DEKHO.csv
* Car details v3.csv
* Car details v4.csv

Además, se utiliza una API externa de conversión de monedas para obtener tasas de cambio actualizadas.

---

## Proceso ETL

El proceso ETL realiza:

### Extracción

* Lectura de múltiples archivos CSV.
* Obtención de tasas de cambio mediante API externa.

### Transformación

* Limpieza de registros.
* Homogeneización de nombres de columnas.
* Eliminación de valores nulos.
* Conversión de monedas.
* Integración de datasets.

### Carga

* Almacenamiento en SQLite.
* Generación de dataset_final.csv.

---

## Base de Datos

Base de datos utilizada:

```text
autos.db
```

Contiene la información consolidada y procesada de los vehículos.

---

## API REST

La API fue desarrollada utilizando FastAPI.

### Iniciar API

```bash
uvicorn api.api:app --reload
```

### Documentación Swagger

```text
http://localhost:8000/docs
```

### Endpoints

#### Inicio

```http
GET /
```

Respuesta:

```json
{
  "mensaje": "API de Vehículos"
}
```

---

#### Vehículos

```http
GET /vehiculos
```

Retorna los primeros registros del dataset.

---

#### Estadísticas

```http
GET /estadisticas
```

Ejemplo:

```json
{
  "cantidad": 1000,
  "precio_promedio": 12500.5
}
```

---

## Dashboard

El dashboard fue desarrollado con Streamlit.

### Ejecutar

```bash
streamlit run dashboards/dashboard.py
```

### Funcionalidades

* Vista Ejecutiva
* Vista Técnica
* Filtros por marca
* Filtros por combustible
* Métricas de negocio
* Gráficos interactivos
* Tabla dinámica de resultados

---

## Docker

### Construcción

```bash
docker compose build
```

### Ejecución

```bash
docker compose up
```

### Acceso Dashboard

```text
http://localhost:8501
```

---

## Instalación Local

### Clonar repositorio

```bash
git clone <url-del-repositorio>
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar ETL

```bash
python etl/etl_final.py
```

### Ejecutar Dashboard

```bash
streamlit run dashboards/dashboard.py
```

### Ejecutar API

```bash
uvicorn api.api:app --reload
```

---

## Manejo de Errores

El proyecto contempla:

* Validación de archivos de entrada.
* Control de errores de lectura.
* Verificación de datos nulos.
* Manejo de excepciones en consultas API.
* Validación de rutas de archivos.

---

## Autores

* Sebastián Aird Gutierrez
* Integrantes del equipo

---

## Licencia

Proyecto desarrollado con fines académicos.
