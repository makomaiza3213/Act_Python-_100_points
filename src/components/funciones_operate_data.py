import PySimpleGUI as sg
from src.windows import menu_windows
from src.components import menu
import csv
import json
import operator

def mostrar_en_csv(ruta):
    """
        IMPRIME EN CONSOLA LOS RESULTADOS CORRESPONDIENTES EN FORMATO JSON
    """
    archivo = open(ruta, 'r')
    datos = json.load(archivo)
    datos_a_mostrar = json.dumps(datos, indent=4)
    print(datos_a_mostrar)
    archivo.close()

def count_calls():
    """
        retorna la cantidad total de llamados
    """
    archivo = open("llamados_107_covid.csv","r")
    csvreader = csv.reader(archivo, delimiter=',')
    encabezado = next(csvreader)
    list_calls = list(map(lambda x:x[1], csvreader))
    calls_res = list(map(int, list_calls))
    cant_call = sum(calls_res)
    return cant_call

def count_descs():
    """
        retorna la cantidad total de casos descartados
    """
    archivo = open("llamados_107_covid.csv","r")
    csvreader = csv.reader(archivo, delimiter=',')
    encabezado = next(csvreader)
    list_desc = list(map(lambda x:x[3], csvreader))
    desc_res = list(map(int,list_desc))
    cant_desc = sum(desc_res)
    return cant_desc

def operateData1():
    """
        Proceso la información del DATASET1
    """
    archivo2 = open("resultados.json","w")
    cant_call = count_calls()
    cant_desc = count_descs()

    res = [{"FECHA": "2020-2021", "LLAMADOS": cant_call, "CASOS DESCARTADOS": cant_desc}]
    json.dump(res, archivo2, indent = 4)
    archivo2.close()
    #mostrar_en_csv('resultados.txt')
    return [cant_call,cant_desc]

def max_sort(peces):
    """
        calcula y retorna la lista con los nombres de los peces mas pescados
    """
    archivo2 = open("resultados2.json","a+")
    items = peces.items()
    peces_max = sorted(peces.items(), key=operator.itemgetter(1), reverse=True)
    maximos = []
    for i in range(0,10):
        maximos.append(peces_max[i])
    json.dump(maximos, archivo2, indent = 4)
    nom_max = [pez[0] for pez in maximos]
    return nom_max

def min_sort(peces):
    """
        calcula y retorna la lista con los nombres de los peces menos pescados
    """
    archivo2 = open("resultados2.json","a+")
    items = peces.items()
    minimos = []
    peces_min = sorted(peces.items(),key = operator.itemgetter(1))
    for i in range(0,10):
        minimos.append(peces_min[i])
    json.dump(minimos, archivo2, indent = 4)
    nom_min = [pez[0] for pez in minimos]
    return nom_min

def operateData2():
    """
        Proceso la información del DATASET2
    """
    archivo = open('captura-puerto-flota-2019.csv')
    csvreader = csv.reader(archivo, delimiter = ',')
    encabezado = next(csvreader)

    peces = {}
    for linea in csvreader:
        if linea[10] in peces:
            peces[linea[10]] += int(linea[12])
        else:
            peces[linea[10]] = int(linea[12])
    #items = peces.items()
    max = max_sort(peces)
    min = min_sort(peces)
    return [max,min]
