import os
import random
import PySimpleGUI as sg
from tkinter import filedialog
from src.constants.style import IMG_DEFAULT, SIZE_DEFAULT
from src.screens.generador_meme2 import *
from src.manipulators import memes
from src.screens.generador_meme2 import eje_generar_meme
from src.manipulators.settings import Settings
from src.constants.directions import TEMPLATE_MEMES
import os
from src.manipulators.resizador import redimensionar_imagen


def config2(path:str, parent:str, datos:any):
    """
    Configura los datos para mostrar una estructura de archivos y carpetas en un treeview.

    Args:
        path (str): Ruta del directorio actual.
        parent (str): Nodo padre en el treeview.
        datos (treeview): Estructura de datos treeview.

    Returns:
        treeview: Estructura de datos treeview actualizada.

    """
    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    if (os.path.isdir(path)):
        file = os.listdir(path)
    else:
        file = []
    for i in file : 
        if ( not str(i).endswith(".gitkeep" )): 
            fullname = os.path.join(path,i)
            if (os.path.isdir(os.path.join(path,i))):
                datos.Insert(parent, fullname, i, values=[], icon= folder_icon)
                config2(os.path.join(path,i),fullname,datos)
            else:
                datos.Insert(parent, fullname, i, values=[], icon= file_icon)
    return datos


def meme(datos) -> sg.Window:
    """
        Funcion que crea la ventana "generador_meme"

        no requiere parametros

        retorna sg.Window
    """
    layoutUnlpImage = [[sg.Text('UNLPImage'), sg.Push(), sg.Text('Generador meme'), sg.Push(), sg.Button("⇦ Atras", key="-ATRAS-", size=(10, 2))],

                       ]

    tree = sg.Tree(data=datos,
                   headings=[" "],
                   auto_size_columns=True,
                   select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                   num_rows=12,
                   col0_width=22,
                   key='-TREE-',
                   show_expanded=True,
                   enable_events=True,
                   expand_x=False,
                   expand_y=False,
                   )

    layout = [
        [sg.Text("", size=(10, 3))],
        [sg.Text("seleccionar template:"), sg.Push()],
        [sg.Text(""), tree, sg.Text("", size=(2, 0)), sg.Push(),
         sg.Image(source=IMG_DEFAULT, size=(300, 300), key="-IMG-"), sg.Push()],
        [sg.Text("", size=(30, 0)),
         sg.Text("", size=(30, 80)), sg.Button("Generar", key="-GENERAR-", size=(10, 2))]
    ]

    # Crea la ventana de PySimpleGUI
    all = [[sg.Column(layout, justification='c',
                      element_justification='c'), layoutUnlpImage]]
    return sg.Window("Creador de meme", all, size=SIZE_DEFAULT, element_justification='c')


def generador_memes():
    """
       Funcion que ejecuta la ventana "generador_memes"
       contiene parte de la funcionalidad 

       no requiere parametros

       retorna ningun valor
    """
    datos = sg.TreeData()
    datos = config2(TEMPLATE_MEMES, "", datos)
    window = meme(datos)
    while True:

        event, values = window.read()
        
        match event:
            case sg.WIN_CLOSED:
                return 0
            case "-TREE-":
                try:
                    es_archivo = values["-TREE-"][0] != "MH"
                    if (es_archivo):
                        ruta = os.path.join(
                            TEMPLATE_MEMES, values["-TREE-"][0])
                        window["-IMG-"].update(
                            source=redimensionar_imagen(ruta, (300, 300)))

                except:
                    ruta = ""
                    window["-IMG-"].update(source=(IMG_DEFAULT),
                                           size=(300, 300))

            case "-GENERAR-":
                path = ruta.split(os.sep)[-1]
                p = memes.abrir_json(path)
                if p != "":
                    window.close()
                    event = eje_generar_meme(p)
                    window = meme(datos)
                else:
                    sg.popup_error("La imagen seleccionada no tiene las medidas cargadas")
            case"-ATRAS-":
                window.close()
                break
        if event == 0:
            return 0
            
