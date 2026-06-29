# Plantilla de presentacion de resultados

## 1. Titulo del reto

Reto colaborativo de produccion rural - Semana 15

Nombre del equipo: Trabajo individual
Integrantes: Trabajo individual
Roles: coordinador, programador, tester, documentador, disenador visual y vocero.

## 2. Problema identificado

La actividad busca analizar registros de produccion de varias fincas rurales para comunicar resultados de forma clara. Se requiere identificar la finca con mayor produccion de leche, la finca con mayor cosecha de maiz, los datos que necesitan revision y el recurso visual mas adecuado para presentar los hallazgos.

## 3. Datos utilizados

Se uso el archivo `data/produccion_fincas.csv`, que contiene 1680 registros y 9 columnas: fecha, semana, finca, zona, responsable_equipo, litros_leche, kilos_maiz, calidad_dato y observacion. Las columnas clave para el analisis fueron `finca`, `litros_leche`, `kilos_maiz` y `calidad_dato`.

## 4. Proceso realizado

1. Se abrio y reviso el proyecto.
2. Se exploro el archivo CSV y se identificaron las columnas reales.
3. Se corrigieron errores de rutas, columnas y nombres de archivos.
4. Se genero el reporte de resultados.
5. Se genero el grafico de barras.
6. Se prepararon conclusiones y evidencias.

## 5. Resultado principal

La finca con mayor produccion de leche fue Buena Vista, con 11763.69 litros. La finca con mayor cosecha de maiz fue San Miguel, con 35408.91 kilos. Tambien se encontraron 192 registros que requieren revision por estar marcados como `revisar` o `dato_incompleto`.

## 6. Recurso visual utilizado

Se uso un grafico de barras: `resultados/grafico_produccion_leche.png`. Este recurso ayuda porque compara de forma directa la produccion total de leche de cada finca y permite identificar rapidamente las diferencias entre categorias.

## 7. Errores y mejoras

El primer error fue que `02_generar_resultados.py` buscaba `produccion_rural.csv`, pero el archivo real se llama `produccion_fincas.csv`. Tambien usaba columnas inexistentes como `litro_leche`, `maiz_kg` y `nombre_finca`; se corrigieron por `litros_leche`, `kilos_maiz` y `finca`.

El segundo error fue que `03_generar_grafico.py` intentaba leer `resumen_finca.csv` y ordenar por `total_litros`, pero el archivo y la columna correctos son `resumen_fincas.csv` y `litros_leche`.

## 8. Conclusion

El equipo aprendio que un trabajo tecnico debe combinar depuracion, analisis y comunicacion. Corregir el codigo permite generar resultados, pero la tabla, el reporte y el grafico convierten esos resultados en informacion entendible para tomar decisiones.
