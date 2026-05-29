import pandas
import matplotlib.pyplot

matplotlib.pyplot.switch_backend("agg")

print("\n" + "-" * 7 + " Analisis de Temperatura Global " + "-" * 7 + "\n")

# Carga y limpieza de datos.
RUTA_DATOS = "datos/"
datos = pandas.read_csv(f"{RUTA_DATOS}monthly_csv.csv")
datos_limpios = datos.dropna()

# Indicadores.
temp_promedio = datos_limpios["Mean"].mean()
temp_max = datos_limpios["Mean"].max()
temp_min = datos_limpios["Mean"].min()
temp_std = datos_limpios["Mean"].std()
cantidad_registros = len(datos_limpios)
año_inicio = datos_limpios["Year"].min()
año_final = datos_limpios["Year"].max()

# Impresión de resultados.
ancho = 43
ancho_tabla3 = 45

print(f"+{'-' * ancho}+")
print(f"|{'INFORMACION DEL DATASET'.center(ancho)}|")
print(f"+{'-' * ancho}+")
print(f"| Registros analizados  | {cantidad_registros:<12}      |")
print(f"| Periodo               | {año_inicio} - {año_final} |")
print(f"+{'-' * ancho}+")

print()

print(f"+{'-' * ancho}+")
print(f"|{'INDICADORES PRINCIPALES'.center(ancho)}|")
print(f"+{'-' * ancho}+")
print(f"| Temperatura promedio      | {temp_promedio:+.2f}°C       |")
print(f"| Temperatura maxima        | {temp_max:+.2f}°C       |")
print(f"| Temperatura minima        | {temp_min:+.2f}°C       |")
print(f"| Desviacion estandar       | {temp_std:.2f}°C        |")
print(f"+{'-' * ancho}+")

print()

# Analisis adicional
temp_positivas = (datos_limpios["Mean"] > 0).sum()
temp_negativas = (datos_limpios["Mean"] < 0).sum()
porcentaje_positivas = (temp_positivas / cantidad_registros) * 100

print(f"+{'-' * ancho_tabla3}+")
print(f"|{'ANALISIS ADICIONAL'.center(ancho_tabla3)}|")
print(f"+{'-' * ancho_tabla3}+")
print(f"| Temperatura positiva      | {temp_positivas:<6} | {porcentaje_positivas:.1f}%  |")
print(f"| Temperatura negativa      | {temp_negativas:<6} | {100 - porcentaje_positivas:.1f}%  |")
print(f"+{'-' * ancho_tabla3}+")

# Primer Grafico.
RUTA_GRAFICO = "resultados/"

print("\n" + "-" * 13 + " GENERANDO GRAFICOS " + "-" * 13 + "\n")
matplotlib.pyplot.figure(figsize=(16,7))
matplotlib.pyplot.plot(datos_limpios.index, datos_limpios["Mean"], linewidth=1.5, color="#2ca02c", alpha=0.8)
matplotlib.pyplot.fill_between(datos_limpios.index, datos_limpios["Mean"], alpha=0.2, color="#2ca02c")
matplotlib.pyplot.axhline(y=0, color="white", linestyle="-", linewidth=0.8, alpha=0.5)
matplotlib.pyplot.axhline(y=temp_promedio, color="#ff7f0e", linestyle="--", linewidth=2, label=f"Promedio: {temp_promedio:+.2f}°C", alpha=0.9)
matplotlib.pyplot.title("Ecolucion de la Temperatura Global (1850 - Actualidad)", fontsize=14, fontweight="bold")
matplotlib.pyplot.xlabel("Tiempo (registros mensuales)", fontsize=12)
matplotlib.pyplot.ylabel("Anomalía de Temperatura (°C)", fontsize=12)
matplotlib.pyplot.legend(fontsize=11)
matplotlib.pyplot.grid(True, alpha=0.3)
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(f"{RUTA_GRAFICO}evolucion_temperatura.png", dpi=300, bbox_inches="tight")
print("Primer grafico: evolucion_temperatura.png")

# Segundo Grafico.
matplotlib.pyplot.figure(figsize=(12, 7))
matplotlib.pyplot.hist(datos_limpios["Mean"], bins=50, color="#9467bd", edgecolor="#e8e8e8", alpha=0.85)
matplotlib.pyplot.axvline(temp_promedio, color="#ff7f0e", linestyle="--", linewidth=2.5, label=f"Promedio: {temp_promedio:+.2f}°C")
matplotlib.pyplot.axvline(0, color="white", linestyle="-", linewidth=1, alpha=0.7, label="Línea base (0°C)")
matplotlib.pyplot.title("Distribucion de Temperaturas", fontsize=14, fontweight="bold")
matplotlib.pyplot.xlabel("Temperatura (°C)", fontsize=12)
matplotlib.pyplot.ylabel("Frecuencia", fontsize=12)
matplotlib.pyplot.legend(fontsize=11)
matplotlib.pyplot.grid(True, alpha=0.3, axis="y")
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.savefig(f"{RUTA_GRAFICO}distribucion_temperatura.png", dpi=300, bbox_inches="tight")
print("Segundo grafico: distribucion_temperatura.png")

matplotlib.pyplot.close("all")