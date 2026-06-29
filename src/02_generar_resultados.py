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

DATA_FILE = BASE_DIR / "data" / "produccion_fincas.csv"

RESULTADOS_DIR = BASE_DIR / "resultados"
REPORTE_TXT = RESULTADOS_DIR / "reporte_resultados.txt"
RESUMEN_CSV = RESULTADOS_DIR / "resumen_fincas.csv"


def main():
    print("=== Generacion de resultados por finca ===")

    df = pd.read_csv(DATA_FILE)

    total_leche = df["litros_leche"].sum()
    total_maiz = df["kilos_maiz"].sum()

    resumen = df.groupby("finca").agg({
        "litros_leche": "sum",
        "kilos_maiz": "sum",
        "calidad_dato": "count"
    }).reset_index()

    resumen = resumen.rename(columns={
        "calidad_dato": "cantidad_registros"
    })
    resumen["registros_revision"] = (
        df[df["calidad_dato"].isin(["revisar", "dato_incompleto"])]
        .groupby("finca")
        .size()
        .reindex(resumen["finca"], fill_value=0)
        .to_numpy()
    )
    resumen = resumen.sort_values("litros_leche", ascending=False)

    RESULTADOS_DIR.mkdir(exist_ok=True)
    resumen.to_csv(RESUMEN_CSV, index=False, encoding="utf-8")

    finca_mayor_leche = resumen.loc[resumen["litros_leche"].idxmax()]
    finca_mayor_maiz = resumen.loc[resumen["kilos_maiz"].idxmax()]
    datos_revision = df[df["calidad_dato"].isin(["revisar", "dato_incompleto"])]
    conteo_calidad = df["calidad_dato"].value_counts()

    reporte = []
    reporte.append("REPORTE COLABORATIVO DE PRODUCCION RURAL")
    reporte.append("========================================")
    reporte.append(f"Total de leche registrado: {total_leche:.2f} litros")
    reporte.append(f"Total de maiz registrado: {total_maiz:.2f} kilos")
    reporte.append("")
    reporte.append("Respuestas principales:")
    reporte.append(
        f"- Finca con mayor produccion de leche: {finca_mayor_leche['finca']} "
        f"({finca_mayor_leche['litros_leche']:.2f} litros)."
    )
    reporte.append(
        f"- Finca con mayor cosecha de maiz: {finca_mayor_maiz['finca']} "
        f"({finca_mayor_maiz['kilos_maiz']:.2f} kilos)."
    )
    reporte.append(
        f"- Datos que requieren revision: {len(datos_revision)} registros marcados "
        "como revisar o dato_incompleto."
    )
    reporte.append("- Recurso visual recomendado: grafico de barras por finca.")
    reporte.append("")
    reporte.append("Calidad de los datos:")
    reporte.append(str(conteo_calidad))
    reporte.append("")
    reporte.append("Resumen por finca:")
    reporte.append(resumen.to_string(index=False))

    REPORTE_TXT.write_text("\n".join(reporte), encoding="utf-8")

    print("Reporte generado en:", REPORTE_TXT)
    print("Resumen CSV generado en:", RESUMEN_CSV)


if __name__ == "__main__":
    main()
