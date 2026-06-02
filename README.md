# Evidencia-Generacion-y-Limpieza-de-Gramatica

## Inaki Mancera Llano

## Contexto
Esta evidencia trabaja con la generación y limpieza de una gramática para un subconjunto de Javascript. El objetivo no es representar todo el lenguaje Javascript, ya que este incluye muchas estructuras como funciones, objetos, arreglos, clases, ciclos y condicionales. En su lugar, se seleccionó una parte más específica y manejable del lenguaje: las asignaciones con expresiones aritméticas.

## Lenguaje seleccionado
JavaScript, subconjunto de asignaciones con expresiones aritméticas.

## Implementación
La implementación se realiza con NLTK, una librería de Python que permite definir gramáticas libres de contexto mediante CFG. En este caso, la gramática limpia se escribe como un conjunto de producciones y se utiliza un parser para analizar si las cadenas tokenizadas pueden derivarse desde el símbolo inicial. La clase CFG de NLTK permite representar formalmente una gramática libre de contexto con un símbolo inicial y un conjunto de producciones.

Para analizar las cadenas se utiliza ChartParser, una herramienta de NLTK que permite generar árboles de análisis sintáctico a partir de una gramática libre de contexto. Este parser construye posibles derivaciones de la cadena y permite verificar si existe al menos un árbol válido. Por eso, en la implementación, si el parser genera uno o más árboles, la cadena se considera aceptada; si no genera árboles, se rechaza.

## Consideraciones
para correr el codigo primero asegurese de tener instalado Python y NLTK. Si no tiene NLTK, puede instalarlo con:
- pip install nltk

Después, desde la terminal, entre a la carpeta con los dos documentos de python y ejecute de la siguiente manera:
- python puebas.py
