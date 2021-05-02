import PySimpleGUI as sg
from src.windows import menu_windows
from src.components import menu
import csv
import json

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

def sum_fish(cant,nom_peces,archivo2):
    """
        procesa el csv de peces y retorna una list de dict con la cantidad pescada de cada pez
    """
    archivo = open('captura-puerto-flota-2019.csv')
    csvreader = csv.reader(archivo, delimiter = ',')
    encabezado = next(csvreader)
    datos = []

    for linea in csvreader:
        if(linea[10] == nom_peces[0]):
            cant[0] += int(linea[12])
        elif(linea[10] == nom_peces[1]):
            cant[1] += int(linea[12])
        elif(linea[10] == nom_peces[2]):
            cant[2] += int(linea[12])
        elif(linea[10] == nom_peces[3]):
            cant[3] += int(linea[12])
        elif(linea[10] == nom_peces[4]):
            cant[4] += int(linea[12])
        elif(linea[10] == nom_peces[5]):
            cant[5] += int(linea[12])
        elif(linea[10] == nom_peces[6]):
            cant[6] += int(linea[12])
        elif(linea[10] == nom_peces[7]):
            cant[7] += int(linea[12])
        elif(linea[10] == nom_peces[8]):
            cant[8] += int(linea[12])
        elif(linea[10] == nom_peces[9]):
            cant[9] += int(linea[12])
    datos = [{nom_peces[i]:cant[i]} for i in range(0,len(nom_peces))]
    json.dump(datos, archivo2, indent = 4)
    return datos

def operateData2():
    """
        Proceso la información del DATASET2
    """
    archivo2 = open('resultados2.json', 'w')
    cant = [0,0,0,0,0,0,0,0,0,0]
    nom_peces = ['Abadejo','Cangrejo','Caracol','Caballa','Palometa','Langostino','Besugo','Bagre','Mero','Gatuzo']
    datos = sum_fish(cant,nom_peces,archivo2)
    archivo2.close()
    #mostrar_en_csv('resultados2.txt')
    return datos
