# ## Importamos la base de datos en google colab.
import sys
from google.colab import drive

drive.mount('/content/drive', force_remount = True)
sys.path.append('/content/drive/MyDrive/ML_TSIV')

import pandas as pd
DB = pd.read_csv('/content/drive/MyDrive/ML_TSIV/car_data_for_price_estimation.csv')

# ### Mostramos los primeros 5 instancias y los títulos de los atributos.
DB.head()

# Convertimos la base de datos a un arreglo para manejarla como matriz.
DB = DB.to_numpy()

# ## Obtenemos la cantidad de atributos y de instancias por atributo.

Atributos = DB[0]
NoAtributos = len(Atributos)
Instancias = DB.T[0]
NoInstancias = len(Instancias)

print('La cantidad de atributos es igual a', str(NoAtributos), 'y la cantidad de instancia es igual a', str(NoInstancias) + '.')


# ## Definimos las estadísticas de cada uno de los atributos.

# ### Tipo de atributo.
for idx, element in enumerate(Atributos):
  if str(type(Atributos[idx]))[8 : -2] == 'int':
    TipoAtributo = 'numérico discreto'
  elif str(type(Atributos[idx]))[8 : -2] == 'float':
    TipoAtributo = 'numérico continuo'
  elif str(type(Atributos[idx]))[8 : -2] == 'str':
    TipoAtributo = 'categórico'
  else:
    TipoAtributo = 'desconocido'
  print('Un ejemplo del atributo', str(idx + 1), 'es "' + str(Atributos[idx]) + '" y es de tipo:', str(type(Atributos[idx]))[8 : -2] +  ', por lo tanto, es un atributo', TipoAtributo + '.')

# ### Máximo y mínimo.
MaximoDeAtributos = []
MinimoDeAtributos = []
for idx, element in enumerate(Atributos):
  CaractMax = max(DB.T[idx])
  CaractMin = min(DB.T[idx])
  MaximoDeAtributos.append(CaractMax)
  MinimoDeAtributos.append(CaractMin)
  print('Los elementos máximo y mínimo del atributo', str(idx + 1), 'son', str(CaractMax), 'y', str(CaractMin), 'respectivamente.')

# ### Media, varianza y desviación estandar.
medias = []
for idx, element in enumerate(Atributos):
  sumatoria = 0
  sumatoria2 = 0
  NoInsta = 0
  if str(type(Atributos[idx]))[8 : -2] != 'str':
    for idx2, element2 in enumerate(Instancias):
      if str(DB.T[idx][idx2]) != 'nan':
        sumatoria += DB.T[idx][idx2]
        NoInsta += 1
    media = (1 / NoInsta) * sumatoria
    medias.append(media)
    for idx3, element2 in enumerate(Instancias):
      if str(DB.T[idx][idx3]) != 'nan':
        sumatoria2 += ((DB.T[idx][idx3] - media) ** 2)
    s2 = (1 / (NoInsta - 1)) * sumatoria2
    s = s2 ** (1 / 2)
    print('Los valores de media, varianza y desviación estandar del atributo', str(idx + 1), 'son', str(media) + ',', str(s2), 'y', str(s), 'respectivamente.')

# ### Cuartiles
for idx, element in enumerate(Atributos):
  if str(type(Atributos[idx]))[8 : -2] != 'str':
    atrib = DB.T[idx]
    atrib.sort()

    NoCuartil1 = 0.25 * (NoInstancias + 1)
    if str(type(NoCuartil1))[8 : -2] != 'int':
      pos1 = round(NoCuartil1)
      if pos1 < NoCuartil1:
        pos2 = pos1 + 1
      else:
        pos2 = pos1 - 1
      NoCuartil1 = round((pos1 + pos2) / 2)
    Cuartil1 = atrib[NoCuartil1 + 1]
    incremento = 1
    while True:
      if str(Cuartil1) == 'nan':
          Cuartil1 = atrib[NoCuartil1]
          NoCuartil1 -= 1
      else:
        break

    NoCuartil2 = 0.5 * (NoInstancias + 1)
    if str(type(NoCuartil2))[8 : -2] != 'int':
      pos1 = round(NoCuartil2)
      if pos1 < NoCuartil2:
        pos2 = pos1 + 1
      else:
        pos2 = pos1 - 1
      NoCuartil2 = round((pos1 + pos2) / 2)
    Cuartil2 = atrib[NoCuartil2 + 1]
    while True:
      if str(Cuartil2) == 'nan':
          Cuartil2 = atrib[NoCuartil2]
          NoCuartil2 -= 1
      else:
        break

    NoCuartil3 = 0.7 * (NoInstancias + 1)
    if str(type(NoCuartil3))[8 : -2] != 'int':
      pos1 = round(NoCuartil3)
      if pos1 < NoCuartil3:
        pos2 = pos1 + 1
      else:
        pos2 = pos1 - 1
      NoCuartil3 = round((pos1 + pos2) / 2)
    Cuartil3 = atrib[NoCuartil3 + 1]
    while True:
      if str(Cuartil3) == 'nan':
          Cuartil3 = atrib[NoCuartil3]
          NoCuartil3 -= 1
      else:
        break

    print('Los valores del primer, segundo y tercer cuartil del atributo', str(idx + 1), 'son', str(Cuartil1) + ',', str(Cuartil2), 'y', str(Cuartil3), 'respectivamente.')

# ### Tipo de distribución

# Para definir el tipo, es preferible obtener la gráfica del atributo que permita determinar de manera visual y manual si el atributo presenta una distribución Uniforme, Normal, Unimodal sesgada a la izquierda, Unimodal sesgada a la derecha, multimodal o exponencial.
import matplotlib.pyplot as plt

for idx, element in enumerate(Atributos):
  if str(type(Atributos[idx]))[8 : -2] != 'str':
    if max(DB.T[idx]) >= 10000:
      datos = DB.T[idx] / 10000
    else:
      datos = DB.T[idx]

    intervalos = range(int(min(datos)), int(max(datos)) + 2)

    plt.hist(x = datos, bins = intervalos, color = '#F2AB6D', rwidth = 0.85)
    plt.title('Histograma de atributo ' + str(idx + 1) + '.')
    plt.xlabel('Características')
    plt.ylabel('Frecuencia')

    plt.show()

# ## Relaciones entre atributos.

# ### Covarianza
for idx, element in enumerate(Atributos):
  if idx < len(medias) - 2:
    if str(type(Atributos[idx]))[8 : -2] != 'str':
      MX = medias[idx]
      MY = medias[idx + 1]
      NoInsta = 0
      sumatoria = 0
      for idx2, element2 in enumerate(Instancias):
        if str(DB.T[idx][idx2]) != 'nan':
          sumatoria += (DB.T[idx][idx2] - MX) * (DB.T[idx + 1][idx2] - MY)
          NoInsta += 1
    #media = (1 / NoInstancias) * sumatoria
    Covarianza = (1 / NoInsta) * sumatoria
    print('La covarianza entre el atributo', str(idx + 1), 'y el atributo', str(idx + 2), 'es igual a', str(Covarianza) + '.')

# ## No. de datos faltantes por atributo
NoFaltantes = []
for idx, element in enumerate(Atributos):
  sumatoria = 0
  for idx2, element2 in enumerate(Instancias):
    if str(DB.T[idx][idx2]) == 'nan':
      sumatoria += 1
  NoFaltantes.append(sumatoria)
  print('La cantidad de carcaterísticas faltantes en el atributo', str(idx + 1), 'es igual a', str(sumatoria) + '.')


# ## Núm. de datos atípicos por atributo
import matplotlib.pyplot as plt
for idx, element in enumerate(Atributos):
  if str(type(Atributos[idx]))[8 : -2] != 'str':
    X = DB.T[idx]
    Y = []
    for idxX, elemento in enumerate(X):
      Y.append(idxX + 1)
  plt.scatter(X, Y, linewidths = 2, edgecolors = 'blue')
  plt.show()

# ## Balance de la base de datos
CantMax = max(NoFaltantes)
for idx, element in enumerate(Atributos):
  Proporcion = NoFaltantes[idx] * 100 / CantMax
  print('El porcentaje de carcaterísticas presentes en el atributo', str(idx + 1), 'es igual a', str(Proporcion) + '.')


# ## Normalización de los datos
DBNorm = []
MaximoNormalizado = 1
MinimoNormalizado = 0
RangoNormalizado = MaximoNormalizado - MinimoNormalizado
for idx, element in enumerate(Atributos):
  CaractNorm = []
  if str(type(Atributos[idx]))[8 : -2] != 'str':
    RangodeDatos = MaximoDeAtributos[idx] - MinimoDeAtributos[idx]
    for idx2, element2 in enumerate(Instancias):
      if str(DB.T[idx][idx2]) != 'nan':
        D = DB.T[idx][idx2] - MinimoDeAtributos[idx]
        DPct = D / RangodeDatos
        dNorm = RangoNormalizado * DPct
        Normalizado = MinimoNormalizado + dNorm
        CaractNorm.append(Normalizado)
      else:
        CaractNorm.append(DB.T[idx][idx2])
  else:
    for idx2, element2 in enumerate(Instancias):
      CaractNorm.append(DB.T[idx][idx2])
  DBNorm.append(CaractNorm)

# ## Imputación por vecino más cercano (por sus siglas en inglés NN o  K-NN)
for idx, element in enumerate(Instancias):
  for idx2, element2 in enumerate(Atributos):
    if str(DB[idx][idx2]) == 'nan':
      
      for idx3, element3 in enumerate(Atributos): 
        if str(DB[idx][idx3]) != 'nan':
          break
      
      d = []
      posd = []
      for idx4, element4 in enumerate(Instancias):
        if idx4 < idx3:
          d.append((((idx3 - idx3) ** 2) + (idx - idx4) ** 2) ** (1 / 2))
          posd.append(idx4)
        elif idx4 == idx3:
          d.append(0)
          posd.append(idx4)
        else:
          d.append((((idx3 - idx3) ** 2) + (idx4 - idx) ** 2) ** (1 / 2))
          posd.append(idx4)