import PySimpleGUI as sg

def interfaz():
    """
        Construye la ventana del menu de la aplicación
    """
    sg.theme('LightGreen')
    layout = [[sg.Text("¿QUÉ DATOS ANALIZAMOS?",justification = 'center', font = ('Helvetica', 15), key = '-TITULO-')],
              [sg.Button("LLAMADOS LINEA 107 COVID-19", size = (35,3),font = ('Helvetica', 10), key = '-DATASET1-')],
              [sg.Button("CAPTURA DE PECES ARGENTINA 2019", size = (35,3),font = ('Helvetica', 10), key = '-DATASET2-')],
              [sg.Button("SALIR", size = (35,3),font = ('Helvetica', 10), key = '-EXIT-')]]

    window = sg.Window('Actividad 1 x Py+ - TEORIA -', layout, no_titlebar = True)
    return window

def llamados():
    """
        Construye la ventana del menu de opciones a procesar, COVID
    """
    layout = [[sg.Button('TOTAL DE LLAMADOS',key = '-LLAMADOS-')],
              [sg.Button('CASOS DESCARTADOS',key = '-DESCARTADOS-')],
              [sg.Button('BACK', key = '-BACK-')]]

    window = sg.Window('Datos oficiales 2020 - 2021', layout, no_titlebar = True)
    return window

def peces():
    """
        Construye la ventana del menu de opciones a procesar, peces
    """
    layout = [[sg.Button('MÁS PESCADO', key = '-MAS-')],
              [sg.Button('MENOS PESCADO', key = '-MENOS-')],
              [sg.Button('Back', key = '-BACK-')]]
    window = sg.Window('Peces',layout, no_titlebar = True)
    return window
