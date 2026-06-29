# Bitacora de acciones - Semana 15

Nombre(s): Trabajo individual
Fecha: 2026-06-29
Entorno utilizado: Windows, PowerShell, VS Code, Python pendiente de instalacion funcional

| No. | Accion realizada | Comando usado | Resultado obtenido | Error encontrado | Ajuste aplicado | Evidencia |
|---:|---|---|---|---|---|---|
| 1 | Abrir proyecto en VS Code | No aplica | Se reviso la estructura del proyecto: docs, src, data, evidencias y visuales. | Ninguno. | Se identificaron los archivos de trabajo. | Captura 1 |
| 2 | Verificar Python | `python --version` | El comando no ejecuto en esta maquina. | Windows mostro: "Una sesion de inicio especificada no existe". Los alias `python`, `py` y `winget` no apuntan a una instalacion funcional. | Se documento el bloqueo y se dejo el codigo corregido para ejecutarlo cuando Python este instalado. | Captura 2 |
| 3 | Instalar dependencias | `pip install -r requirements.txt` | Pendiente por falta de Python funcional. | No fue posible ejecutar `pip`. | Se verifico que `requirements.txt` pide `pandas` y `matplotlib`. | Captura 3 |
| 4 | Explorar datos | `python src/01_explorar_datos.py` | Se reviso el CSV y sus columnas: fecha, semana, finca, zona, responsable_equipo, litros_leche, kilos_maiz, calidad_dato, observacion. | Ninguno en el CSV. | Se usaron los nombres reales para corregir scripts. | Captura 4 |
| 5 | Generar resultados | `python src/02_generar_resultados.py` | Se corrigio el script y se genero `resultados/reporte_resultados.txt` y `resultados/resumen_fincas.csv`. | Ruta incorrecta `produccion_rural.csv`, columnas `litro_leche`, `maiz_kg` y `nombre_finca` inexistentes, y carpeta `resultados` no creada. | Se cambio a `produccion_fincas.csv`, columnas `litros_leche`, `kilos_maiz`, `finca`, y se agrego `RESULTADOS_DIR.mkdir()`. | Captura 5 |
| 6 | Generar grafico | `python src/03_generar_grafico.py` | Se corrigio el script y se genero `resultados/grafico_produccion_leche.png`. | Nombre de resumen incorrecto `resumen_finca.csv` y columna `total_litros` inexistente. | Se cambio a `resumen_fincas.csv` y se ordeno por `litros_leche`. | Captura 6 |
| 7 | Validar trabajo | `python src/04_validar_trabajo.py` | Los archivos esperados existen y tienen contenido: reporte, resumen CSV y grafico PNG. | No se pudo ejecutar el validador por falta de Python funcional. | Se verificaron los archivos con PowerShell y se deja listo para validar con Python instalado. | Captura 7 |

## Reflexion tecnica breve

Aprendi que la depuracion debe iniciar leyendo el mensaje de error y comparando rutas y columnas con los archivos reales. En este reto, los errores mas importantes estaban en nombres de archivo, nombres de columnas y generacion de carpetas. Tambien se evidencio que un resultado tecnico necesita comunicarse con claridad: el reporte responde las preguntas principales y el grafico de barras permite comparar rapidamente la produccion de leche por finca.
