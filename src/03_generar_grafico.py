"""
Semana 15 - Generacion de recurso visual

OBJETIVO:
Crear un grafico que ayude a comunicar resultados del reto colaborativo.

ATENCION:
Este archivo tambien contiene errores intencionales. Debes corregirlos.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTADOS_DIR = BASE_DIR / "resultados"

# ERROR INTENCIONAL 1: revisa si el archivo generado por el script anterior tiene este nombre.
RESUMEN_CSV = RESULTADOS_DIR / "resumen_finca.csv"
GRAFICO = RESULTADOS_DIR / "grafico_produccion_leche.png"


def main():
    print("=== Generacion de grafico ===")

    resumen = pd.read_csv(RESUMEN_CSV)

    # ERROR INTENCIONAL 2: revisa si esta columna existe en el resumen.
    resumen = resumen.sort_values("total_litros", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(resumen["finca"], resumen["litros_leche"])
    plt.title("Produccion total de leche por finca")
    plt.xlabel("Finca")
    plt.ylabel("Litros de leche")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(GRAFICO)

    print("Grafico generado en:", GRAFICO)


if __name__ == "__main__":
    main()
