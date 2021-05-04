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

def loop(tops):
    """
        Loop de la ventana de peces que capta los eventos al apretar las opciones
    """
    window = menu_windows.peces()

    while True:
        event, values = window.read()
        if event == '-MAS-':
            sg.popup(tops[0])
        if event == '-MENOS-':
            sg.popup(tops[1])
        if event == '-BACK-':
            break
    #actualizar_json(min_max)
    return window

def start(tops):
    """
        Lanza la ejecucion de la ventana de peces
    """
    window = loop(tops)
    window.close()
