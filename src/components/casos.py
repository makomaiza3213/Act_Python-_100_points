from src.components import menu
from src.windows import menu_windows
import PySimpleGUI as sg
import json

def cantidades():
    """
        Calcula la cantidad de llamados y casos descartados
    """
    with open('resultados.json') as file:
        data = json.load(file)
        cant = []
        for elem in data:
            for key, value in elem.items():
                if key == 'LLAMADOS':
                    cant.append(value)
                if key == 'CASOS DESCARTADOS':
                    cant.append(value)
    return cant

def loop():
    """
        Loop de la ventana de casos que capta los eventos al apretar las opciones
    """
    window = menu_windows.llamados()
    while True:
        event , values = window.read()
        cants = cantidades()
        if event == '-LLAMADOS-':
            sg.popup(cants[0])
        if event == '-DESCARTADOS-':
            sg.popup(cants[1])
        if event == '-BACK-':
            break
    return window

def start():
    """
        Lanza la ejecucion de la ventana de casos de COVID
    """
    window = loop()
    window.close()
