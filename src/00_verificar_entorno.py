"""
Semana 15 - Verificacion del entorno

Este script comprueba que Python funcione correctamente y orienta al estudiante
sobre las librerias necesarias para el laboratorio.
"""

import sys
from pathlib import Path

print("=== Verificacion del entorno ===")
print("Version de Python:", sys.version)
print("Carpeta actual:", Path.cwd())

try:
    import pandas  # noqa: F401
    print("pandas: instalado correctamente")
except ImportError:
    print("pandas: no instalado. Ejecuta: pip install -r requirements.txt")

try:
    import matplotlib  # noqa: F401
    print("matplotlib: instalado correctamente")
except ImportError:
    print("matplotlib: no instalado. Ejecuta: pip install -r requirements.txt")

print("\nSi todo aparece correctamente, continua con src/01_explorar_datos.py")
