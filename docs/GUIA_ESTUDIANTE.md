# Guia del estudiante - Semana 15
## Reto colaborativo, comunicacion de resultados y recursos visuales

### 1. Sentido de la actividad

En esta practica vas a trabajar como si hicieras parte de un equipo tecnico que debe analizar informacion rural y comunicar los resultados de forma clara. El objetivo no es solo ejecutar codigo, sino aprender a organizarse, tomar decisiones, registrar evidencias y transformar datos en una explicacion visual comprensible.

Un proyecto tecnico no termina cuando aparece un resultado en la terminal. Tambien debe poder explicarse: que problema se abordo, que datos se usaron, que proceso se siguio, que resultados se obtuvieron, que errores aparecieron y como se corrigieron.

### 2. Caso contextualizado

La comunidad educativa de una zona rural tiene registros de produccion de varias fincas. Cada finca reporta litros de leche, kilos de maiz, zona, semana y calidad del dato. El equipo debe procesar esos datos y preparar una comunicacion visual que permita responder:

- Cual finca registro mayor produccion de leche?
- Cual finca registro mayor cosecha de maiz?
- Que datos requieren revision?
- Que grafico ayuda mejor a explicar los resultados?
- Como se organizo el equipo para resolver el reto?

### 3. Roles sugeridos

Si trabajas en pareja o equipo, asignen responsabilidades. Si trabajas individualmente, debes asumir todos los roles.

| Rol | Responsabilidad |
|---|---|
| Coordinador | Organiza pasos, tiempos y decisiones. |
| Programador | Ejecuta y corrige scripts. |
| Tester | Verifica resultados y detecta errores. |
| Documentador | Registra comandos, errores, ajustes y evidencias. |
| Disenador visual | Selecciona tabla, grafico o esquema para comunicar. |
| Vocero | Prepara la explicacion final de resultados. |

### 4. Ruta de trabajo

1. Abre la carpeta completa en VS Code.
2. Lee este documento antes de ejecutar codigo.
3. Revisa la estructura del proyecto.
4. Abre la terminal integrada.
5. Ejecuta `python --version`.
6. Instala dependencias con `pip install -r requirements.txt`.
7. Ejecuta `python src/00_verificar_entorno.py`.
8. Ejecuta `python src/01_explorar_datos.py` y observa los nombres reales de columnas.
9. Ejecuta `python src/02_generar_resultados.py`. Debe fallar. Lee el error.
10. Corrige el primer error y vuelve a ejecutar.
11. Repite hasta que el script genere resultados.
12. Ejecuta `python src/03_generar_grafico.py`. Debe fallar hasta que corrijas sus errores.
13. Ejecuta `python src/04_validar_trabajo.py`.
14. Completa las plantillas de evidencias.
15. Prepara una explicacion visual breve.

### 5. Regla importante de depuracion

No adivines. Cada error debe diagnosticarse siguiendo este orden:

1. Leer el mensaje de error completo.
2. Identificar el archivo y la linea donde ocurre.
3. Comprender la causa probable.
4. Revisar nombres de archivos, rutas o columnas.
5. Corregir solo una cosa a la vez.
6. Ejecutar de nuevo.
7. Registrar el ajuste en la bitacora.

### 6. Producto final

Debes entregar evidencias de:

- Proyecto abierto en VS Code.
- Comandos ejecutados.
- Errores encontrados y corregidos.
- Reporte generado.
- Grafico generado.
- Roles del equipo.
- Recurso visual o plantilla de presentacion.
- Reflexion breve sobre colaboracion y comunicacion.
