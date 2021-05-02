from src.components import menu
from src.windows import menu_windows
import PySimpleGUI as sg
import json

def write_json(data, filename='resultados2.json'):
    """
        Escribe datos recibidos en formato json
    """
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def actualizar_json(news):
    """
        Agrega la informacion de los peces más y menos pescados al archivo
    """
    with open('resultados2.json') as json_file:
        data = json.load(json_file)
        new = {"EL MAS PESCADO":news[0],"EL MENOS PESCADO":news[1]}
        data.append(new)
    write_json(data)

def max_min_pez():
    """
        Calcula el pez con más y menos pesca entre los 10 mas conocidos , previamente seleccionados
    """
    with open('resultados2.json') as file:
        data = json.load(file)
        max_key = ''
        max_val = 0
        min_key = ''
        min_val = 90000000
        for elem in data:
            for key, value in elem.items():
                if value > max_val:
                    max_key = key
                    max_val = value
                if value < min_val:
                    min_key = key
                    min_val = value
    return [max_key,min_key]

def loop():
    """
        Loop de la ventana de peces que capta los eventos al apretar las opciones
    """
    window = menu_windows.peces()
    while True:
        event, values = window.read()
        min_max = max_min_pez()

        if event == '-MAS-':
            sg.popup(min_max[0])
        if event == '-MENOS-':
            sg.popup(min_max[1])
        if event == '-BACK-':
            break
    actualizar_json(min_max)
    return window

def start():
    """
        Lanza la ejecucion de la ventana de peces
    """
    window = loop()
    window.close()
