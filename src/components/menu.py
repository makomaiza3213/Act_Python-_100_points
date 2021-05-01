import PySimpleGUI as sg
from src.windows import menu_windows
from src.components import peces,casos
from src.components import funciones_operate_data as op
import csv
import json

def loop():
    """
        Loop de la ventana de menu que capta los eventos al presionar opciones
    """
    window = menu_windows.interfaz()

    while True:
        event, values = window.read()
        if(event == '-DATASET1-'):
            sg.theme('LightGreen')
            info1 = op.operateData1()
            casos.start()
            window.BringToFront() #por algun motivo cuando ejecutaba el run.py,se ocultaba la ventana del menu y el codigo estaba todo perfecto,
        if(event == '-DATASET2-'):
            op.operateData2()
            peces.start()
            window.BringToFront() #incluso lo vio el profe, como ultima solucion implementamos esta instruccion para que la ventana no se oculte
        if(event == '-EXIT-'):
            sg.popup("aplicación finalizada")
            #ok = False
            break
    return window

def start():
    """
        Ejecucion de la ventana del menu
    """
    window = loop()
    window.close()
