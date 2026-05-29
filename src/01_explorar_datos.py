"""
Semana 15 - Exploracion inicial del CSV

Este script permite conocer la estructura del archivo de datos antes de analizarlo.
Sirve para identificar columnas, cantidad de registros y posibles datos por revisar.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_fincas.csv"


def main():
    print("=== Exploracion inicial de datos ===")
    print("Archivo:", DATA_FILE)

    df = pd.read_csv(DATA_FILE)

    print("\nPrimeras 5 filas:")
    print(df.head())

    print("\nCantidad de filas y columnas:")
    print(df.shape)

    print("\nColumnas disponibles:")
    for columna in df.columns:
        print("-", columna)

    print("\nCalidad de los datos:")
    print(df["calidad_dato"].value_counts())

    print("\nObserva estos nombres de columnas. Los vas a necesitar para corregir los scripts siguientes.")


if __name__ == "__main__":
    main()
