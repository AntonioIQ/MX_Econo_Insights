# 📊 MX_Econo_Insights

## 📝 Descripción

El proyecto **MX_Econo_Insights** explora la interacción entre el **tipo de cambio PESO/USD**, la **tasa de interés**, y la **inflación** en México 🇲🇽, utilizando datos del **Banco de México (Banxico)** y el **Instituto Nacional de Estadística y Geografía (INEGI)**.

## 🎯 Objetivo

Implementar una solución de **ETL** y **ELT** para análisis profundos de indicadores económicos clave, facilitando la toma de decisiones basada en datos.

## 🏗 Arquitectura

![Arquitectura del Proyecto](Images/Arquitectura.png)

## 🚀 Implementación

### Extracción de Datos

- **Banco de México (Banxico)**: Fuente de datos sobre el **tipo de cambio** y **tasa de interés**. 🏦
  - Utiliza [sie-banxico](https://pypi.org/project/sie-banxico/).
- **INEGI**: Proveedor de estadísticas oficiales, incluida la **inflación**. 📈
  - Emplea [INEGIpy](https://pypi.org/project/INEGIpy/).

### Almacenamiento en AWS S3

Almacenamiento de datos limpios en `itam-analytics-NOMBRE/raw` en **Amazon S3**.

### AWS Glue y Amazon Athena

- Base de datos `econ` en **AWS Glue**.
- Consultas SQL en **Amazon Athena** para integración y preparación de datos.

### Análisis de Datos

Construcción de modelos de regresión lineal y visualización de relaciones entre indicadores económicos.

## 📦 Entregables

- **ETLs Notebook**: Scripts para extracción, limpieza, y carga de datos.
- **ELTs Notebook**: Scripts para transformación de datos y carga en estructuras analíticas.
- **Analytics Notebook**: Análisis de datos, modelos de regresión, y visualizaciones.

## 📚 Referencias

- **[Banco de México (Banxico)](https://www.banxico.org.mx/)**: Entidad central de México encargada de la política monetaria y financiera del país.
- **[INEGI](https://www.inegi.org.mx/)**: Instituto encargado de proporcionar información estadística para entender la realidad social y económica de México.
- **Tipo de Cambio**: Valor de la moneda nacional en relación con una moneda extranjera.
- **Tasa de Interés**: Porcentaje que se paga por el uso del dinero en un período determinado.

# MX_Econo_Insights
