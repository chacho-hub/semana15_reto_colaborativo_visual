"""
Semana 15 - Generacion de resultados

OBJETIVO:
Leer el CSV de produccion rural, calcular resultados por finca y generar archivos
para comunicar resultados.

ATENCION:
Este archivo contiene errores intencionales. Debes diagnosticarlos, corregirlos
y registrar cada ajuste en evidencias/bitacora_acciones.md.

Pistas generales:
- Ejecuta primero src/01_explorar_datos.py para conocer columnas reales.
- Revisa si la ruta del archivo CSV coincide con el nombre real.
- Revisa si los nombres de columnas existen en el CSV.
- Verifica que la carpeta resultados exista antes de guardar archivos.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

# ERROR INTENCIONAL 1: el nombre del archivo no coincide con el CSV real.
DATA_FILE = BASE_DIR / "data" / "produccion_rural.csv"

RESULTADOS_DIR = BASE_DIR / "resultados"
REPORTE_TXT = RESULTADOS_DIR / "reporte_resultados.txt"
RESUMEN_CSV = RESULTADOS_DIR / "resumen_fincas.csv"


def main():
    print("=== Generacion de resultados por finca ===")

    df = pd.read_csv(DATA_FILE)

    # ERROR INTENCIONAL 2: estas columnas no existen exactamente con estos nombres.
    total_leche = df["litro_leche"].sum()
    total_maiz = df["maiz_kg"].sum()

    # ERROR INTENCIONAL 3: esta agrupacion usa una columna incorrecta.
    resumen = df.groupby("nombre_finca").agg({
        "litros_leche": "sum",
        "kilos_maiz": "sum",
        "calidad_dato": "count"
    }).reset_index()

    resumen = resumen.rename(columns={
        "calidad_dato": "cantidad_registros"
    })

    # ERROR INTENCIONAL 4: falta crear la carpeta resultados antes de guardar.
    resumen.to_csv(RESUMEN_CSV, index=False, encoding="utf-8")

    reporte = []
    reporte.append("REPORTE COLABORATIVO DE PRODUCCION RURAL")
    reporte.append("========================================")
    reporte.append(f"Total de leche registrado: {total_leche:.2f} litros")
    reporte.append(f"Total de maiz registrado: {total_maiz:.2f} kilos")
    reporte.append("")
    reporte.append("Resumen por finca:")
    reporte.append(str(resumen))

    REPORTE_TXT.write_text("\n".join(reporte), encoding="utf-8")

    print("Reporte generado en:", REPORTE_TXT)
    print("Resumen CSV generado en:", RESUMEN_CSV)


if __name__ == "__main__":
    main()
