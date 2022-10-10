# -*- coding: utf-8 -*-

''' 

En este proyecto trabajaremos con datos de población mundial, representados 
mediante listas. Implementaremos una serie de funciones que nos permitirán mostrar
gráficas de evolución de la población, así como, comparar la población en distintos
países.

CONJUNTOS DE DATOS:
-------------------
El proyecto incluye un conjuntos de datos de prueba:
  - population.csv: con los datos de población de diversos paises o agrupaciones de paises 
    en distintos años.
 
FUNCIONES QUE FORMAN PARTE DEL EJERCICIO:
-----------------------------------------
- lee_poblaciones(fichero):
    lee el fichero de entrada y devuelve una lista de tuplas 
    (nombre_pais, cod_pais, anyo, num_habitantes)
- calcula_paises(poblaciones):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y devuelve una lista ordenada con los nombres
    de los paises o conjuntos de paises para los que hay datos
- filtra_por_pais(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (anyo, num_habitantes)
    con los datos del pais que se pasa como parámetro. 
    El pais se puede dar con su nombre completo o con su código
- filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    devuelve una lista de tuplas (nombre_pais, num_habitantes)
    con los datos del año pasado como parámetro para los paises 
    incluidos en el parámetro paises. 
- muestra_evolucion_poblacion(poblaciones, pais):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) 
    y genera un gráfico con la evolución de la población
    del pais dado como parámetro. El pais se puede dar con su nombre completo o con
    su código
- muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    toma una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes), un año y 
    un grupo de paises y genera un gráfico 
    de barras con la población de esos países en el año dado como parámetro

'''
import csv
from matplotlib import pyplot as plt
from collections import namedtuple

Registro = namedtuple('Registro', 'nombre, codigo, año, censo')

def lee_poblaciones(fichero):
    poblacion = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f)
        for nombre, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            poblacion.append(Registro(nombre, codigo, año, censo))
        return poblacion
############################################################################################

############################################################################################
def calcula_paises(poblaciones):
    paises = {set}
    for poblacion in poblaciones:
        paises.add(poblacion.nombre)
    return list(paises)
##############################################################################################

############################################################################################## 
def filtra_por_pais(poblaciones, pais):
    paisfil = []
    for poblacion in poblaciones:
        if poblacion.nombre == pais:
            paisfil.append((poblacion.año,poblacion.censo))
    return paisfil
##############################################################################################

############################################################################################## 
def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    panafil = []
    for poblacion in poblaciones:
        if poblacion.año == anyo and poblacion.nombre in paises:
                    panafil.append((poblacion.nombre,poblacion.censo))
    return panafil
##############################################################################################

###############################################################################################
def muestra_evolucion_poblacion(poblaciones, pais):
    l_anyos = []
    l_habitantes = []
    for poblacion in poblaciones:
        if poblacion.nombre == pais:
            l_anyos.append(poblacion.año)
            l_habitantes.append(poblacion.censo)
    plt.title("Evolución de la población de " + pais)
    plt.plot(l_anyos,l_habitantes)
    plt.show()
###############################################################################################

###############################################################################################
def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    l_paises = []
    l_habitantes = []
    for poblacion in poblaciones:
        if poblacion.año == anyo:
            for pais in paises:
                if poblacion.nombre == pais:
                    l_paises.append(poblacion.nombre)
                    l_habitantes.append(poblacion.censo)
    plt.title("Población en el año " + str(anyo))
    indice = range(len(l_paises))
    plt.bar(indice, l_habitantes)
    plt.xticks(indice, l_paises, fontsize=8)
    plt.show()
###############################################################################################
