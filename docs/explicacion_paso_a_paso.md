# Explicacion paso a paso del laboratorio

## Paso 1: Abrir el entorno

Abre VS Code y selecciona la carpeta completa del laboratorio. No abras solo la carpeta `src`, porque los scripts usan rutas relativas hacia `data` y `resultados`.

## Paso 2: Comprender la estructura

- `data`: contiene el archivo CSV con registros de produccion.
- `src`: contiene scripts de Python.
- `resultados`: aqui se guardaran reportes y graficos.
- `evidencias`: aqui completas bitacoras y registros de trabajo.
- `visuales`: contiene la plantilla para comunicar resultados.
- `docs`: contiene guias, rubrica y checklist.

## Paso 3: Explorar antes de corregir

El archivo `01_explorar_datos.py` es clave. Te muestra los nombres reales de columnas. Muchos errores de los scripts siguientes estan relacionados con columnas mal escritas o rutas incorrectas.

## Paso 4: Corregir errores con metodo

Cuando un script falle, no borres todo. Lee el error. Por ejemplo, si aparece `FileNotFoundError`, revisa el nombre y ubicacion del archivo. Si aparece `KeyError`, revisa el nombre de la columna.

## Paso 5: Comunicar resultados

El grafico no es decoracion. Debe ayudar a responder el reto. Una buena comunicacion visual permite que otra persona entienda rapidamente el resultado mas importante del analisis.
