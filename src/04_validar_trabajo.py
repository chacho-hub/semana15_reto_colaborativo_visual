"""
Semana 15 - Validacion del trabajo

Ejecuta este archivo al final. Si todo esta corregido, debe confirmar que los
archivos principales fueron generados correctamente.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTADOS_DIR = BASE_DIR / "resultados"
ARCHIVOS_ESPERADOS = [
    RESULTADOS_DIR / "reporte_resultados.txt",
    RESULTADOS_DIR / "resumen_fincas.csv",
    RESULTADOS_DIR / "grafico_produccion_leche.png",
]

print("=== Validacion del laboratorio Semana 15 ===")

faltantes = []
for archivo in ARCHIVOS_ESPERADOS:
    if archivo.exists() and archivo.stat().st_size > 0:
        print("OK:", archivo.relative_to(BASE_DIR))
    else:
        print("FALTA O ESTA VACIO:", archivo.relative_to(BASE_DIR))
        faltantes.append(archivo)

if faltantes:
    print("\nResultado: aun hay elementos por corregir o generar.")
    print("Revisa los errores, ejecuta nuevamente los scripts y documenta tus ajustes.")
else:
    print("\nResultado: laboratorio completado correctamente.")
    print("Ahora completa la bitacora, roles del equipo y plantilla de presentacion.")
