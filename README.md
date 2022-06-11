# DataAnalytics

0.1 Introducción

En el mundo, cada vez nos vemos más abrumados por los datos. Con datos en cada uno de
los dispositivos que manejamos diariamente, datos dentro de la web y la nube. Conforme esta
cantidad aumenta, las oportunidades para obtener información útil de los datos también. No solo
es acerca de observar los datos, es sobre lo que estos nos pueden decir sobre quienes o las cosas
que los generan.

Hoy en día podemos encontrar información sobre las técnicas de análisis de datos, conocimiento
que nos permitirá no solo poder obtener oportunidades de aprovechamiento con los datos, si no
también de conocer las mejores maneras de generar la información y utilizarla.
Por ende, se recomienda tener un acercamiento hacia la técnicas de análisis de datos, lo cual se
comienza con este escrito. [1]

En este reporte, se pueden encontrar algoritmos generalizados para utilizar con cualquier base de
datos y poder extraer así sus primeras características para el análisis. Además, de encontrar un
par de técnicas correctivas que ayudarán a mejorar la base de datos que se ingresa.

0.2 Metodología
DEFINICIONES ESTADÍSTICAS
• La media muestral (Promedio)
Indica el centro de los datos.
Promedio = (1 / n) * sumatoria de Xi [2]
• Desviaciones ((X1 - Xpromedio), . . . , (Xn - Xpromedio)) Distancias de cada valor de la muestra
a la media de la muestra. Al ser una resta, genera valores tanto positivos como negativos,
por eso se eleva al cuadrado al utilizarse en la varianza y en la desviación estándar, para
hacer todos los resultados de la resta positivos.
• Varianza muestral Constituye el promedio de las desviaciones al cuadrado, excepto que lo
dividimos entre n-1 en lugar de n.
s2 = (1 / (n - 1)) * sumatoria de ((Xi - Xpromedio)2) [2]
• Desviación estándar Mide el grado de dispersión.
s = (s2)1 / 2 o raíz cuadrada de s2 [2]
• Cuartiles
La mediana divide la muestra a la mitad, los cuartiles lo dividen, tanto como sea posible, en
cuartos.
Primer cuartil = 0.25 (n + 1) [2]
Segundo cuartil = 0.5 (n + 1) [2] –> Idéntico a la mediana
Tercer cuartil = 0.75 (n + 1) [2]
El resultado te dice el número del valor que representa el X cuartil, de los datos ordenados de
forma ascendente.
Solo si el resultado es un entero, si no, se toma el promedio de los valores de la muestra de
cualquier lado de este valor, tomando la muestra de forma ordenada ascendente.
• Covarianza
Es una medida de la intensidad de la relación entre dos variables aleatorias [2].
cov(X, Y) = promedio((Xi - promedio de X) * (Yi - promedio de Y)) [2]

CONCEPTOS EN EL MANEJO DE DATOS
• Instancias
Cada instancia se caracteriza por los valores de los atributos que miden diferentes aspectos
por cada medición. Si lo vemos en el sentido de una base de datos, las instancias serían los
registros de esta, es decir, las filas.
• Atributos
Si lo vemos como una base de datos, los atributos serían el equivalente a las columnas. El
valor de un atributo para una particular instancia es la medición de la cantidad a la cual el
atributo se refiere.
• Clasificación de atributos
-Atributo categórico:
Categóricos ( cualitativos): representan categorías más que números. Se dividen a su vez en:
Nominales: no tienen orden significativo.
Ordinales: tienen orden definido.
-Atributo numérico:
Numéricos(cuantitativos): son atributos que son núemros, se dividen a su vez en:
Intervalo: no existe un .
Tasa: el cero existe.
Atributo discreto: Tiene un número finito o contable de valores.
Atributo continuo: Tiene un número infinito de valores posibles.
• Tipos de distribución según histogramas
Histograma Uniforme
Histograma Normal (Unimodal)
Histograma Unimodal sesgado izquierda
Histograma Unimodal sesgado derecha
Histograma multimodal
Histograma exponencial
• Problema de calidad en los datos cualquier dato inusual que se encuentre en la base de datos.
Los problemas más comunes de los datos son:
Valores faltantes.
Problemas de cardinalidad irregular. Se da cuando una característica tiene un dato que no es lo
que se esperaría de una característica.

Valores atípicos outliers. Valores que se localizan muy alejados de la tendencia central de una
característica. Se puede categorizar en válidos y no válidos [1].
• Balance entre clases
Se busca tener la misma cantidad de ejemplos por cada clase.
• Normalizar los datos
Algunos algoritmos de inteligencia artificial requieren que todos los datos se centren en un rango
específico de valores, normalmente de -1 a 1 o de 0 a 1. Incluso si no se requiere que los datos se
encuentren dentro de los valores, es buena idea generalmente asegurarse de que los valores se
encuentran dentro de un rango específico.
Normalización de valores ordinales
Para normalizar un set ordinal, se tiene que preservar el orden.
Normalización de valores cuantitativos
Lo primero que se tiene que hacer es observar el rango en el cual se encuentran dichos valores y
el intervalo al que se quiere normalizar. No todos los valores requieren ser normalizados.
Es necesario realizar los cálculos de las siguientes variables para encontrar el valor normalizado:
-Máximo de los datos = el valor más alto de la observación sin normalizar. [1]
-Mínimo de los datos = el menor alto de la observación sin normalizar. [1]
-Máximo normalizado = el valor más alto limítrofe al que el máximo de los datos será normalizado.
[1]
-Mínimo normalizado = el valor más bajo limítrofe al que el mínimo de los datos será normalizado.
[1]
-Rango de datos = Máximo de los datos - Mínimo de los datos [1]
-Rango normalizado = Máximo normalizado - Mínimo normalizado [1]
-D = Valor a normalizar - Mínimo de los datos [1]
-DPct = D / Rango de datos [1]
-dNorm = Rango normalizado * DPct [1]
-Normalizado = Mínimo normalizado + dNorm [1]
De esta forma se obtiene el valor normalizado.
• Imputación de los datos
En ciencia de datos, usualmente, se tienen dos enfoques para lidiar con estos valores faltantes:
omitir las instancias con valores faltantes o realizar técnicas de imputación y estimar los datos
faltantes utilizando los valores existentes.

La imputación es una técnica para reemplazar valores perdidos con valores que se encuentran.
El objetivo es la de tener una base de datos con la menor cantidad de instancias faltantes que
contengan la misma distribución que lo datos existentes para que puedan ser analizados.
Técnicas determínisticas de imputación Funcionan cuando, de acuerdo a las mimas condiciones
de los datos, producen las mismas respuestas. Entre estas técnicas se encuentra la imputación por
vecino más cercano.
Imputación por vecino más cercano: Se calcula la distancia entre la instancia a imputar, usualmente,
por medio de la distancia euclidiana y los datos que tienen valor establecido. Una vez que
se calcula el dato más cercano, se utiliza este para imputar la instancia faltante.
• Distancia euclidiana
La distancia euclidiana está basada en la distancia bidimensional entre dos vectores. Esto es, la
distancia entre dos puntos como si se dibujara una línea con una regla de un punto a otro. Específicamente,
si se tienen dos punto (x1, y1) y (x2, y2), la distancia euclidiana puede ser calculada
mediante la ecuación [1]:
d = raíz cuadrada((x2 - x1)ˆ2 + (y2 - y1)ˆ2) [1]

0.3 Referencias
[1] M. A. Aceves Fernández, Inteligencia Artificial para programadores con prisa. UNIVERSO de
LETRAS, 2021.
[2] W. Navidi, Estadística para ingenieros. México: Mc Graw Hill, 2006.
