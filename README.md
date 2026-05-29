# Analisis de Temperatura Global

## Integrante
Noé Ezequiel Martinez (Comision 11)

## Escenario
Analisis de Datos Climaticos - Temperatura Global

## Descripción
El presente repositorio contiene un análisis exploratorio de registros históricos de temperatura a nivel global, con el objetivo de detectar patrones asociados al cambio climático. A través del procesamiento de los datos, el script extrae métricas fundamentales —como las temperaturas medias, máximas y mínimas— y genera representaciones gráficas que ilustran la progresión térmica a lo largo del tiempo.

## Dataset
- Fuente: DataHub - Global Temperature
- Archivo: monthly_csv.csv
- Periodo: Datos historicos globales

## Indicadores Calculados
- Temperatura promedio global
- Temperatura maxima
- Temperatura minima
- Desviación estandar

## Instrucciones para ejecutar
1. Asegúrate de tener Python instalado
2. Instala las librerias necesarias: `python -m pip install matplotlib`
3. Ejecuta el script: `scripts/analisis_temperatura.py`
4. Los graficos se guardaran en la carpeta `/resultados`

## Archivos principales
- `scripts/analisis_temperatura.py` - Script principal de analisis
- `datos/monthly_csv.csv` - Dataset de temperatura
- `resultados/` - Graficos generados