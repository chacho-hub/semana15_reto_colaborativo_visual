# Guia de depuracion

## Errores esperados

Durante el laboratorio puedes encontrar errores como:

| Error | Posible causa | Como revisarlo |
|---|---|---|
| FileNotFoundError | El nombre o ruta del archivo no existe | Verifica la carpeta `data` y el nombre real del CSV |
| KeyError | La columna no existe en el DataFrame | Ejecuta `01_explorar_datos.py` y copia el nombre correcto |
| OSError | La carpeta de salida no existe | Crea la carpeta con `mkdir` desde Python o revisa `resultados/` |
| NameError | Variable no definida | Revisa si escribiste el mismo nombre de variable en todo el script |
| SyntaxError | Error de escritura en el codigo | Revisa parentesis, comillas y dos puntos |

## Pistas sin dar la solucion

- El CSV real se llama `produccion_fincas.csv`.
- Las columnas reales se pueden ver ejecutando `01_explorar_datos.py`.
- Si vas a guardar archivos, asegúrate de que la carpeta exista.
- El grafico depende de que primero se genere el resumen CSV.
- El validador final te dice que archivos faltan.
