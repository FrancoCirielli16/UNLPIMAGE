import tkinter
import PySimpleGUI as sg
from src.manipulators.collage import imagenes_para_hacer_collage
from src.constants.style import IMG_DEFAULT, SIZE_DEFAULT
from src.constants.directions import TEMPLATE_COLLAGE
import os
from src.manipulators.resizador import redimensionar_imagen
from src.screens.generador_collage2 import generador_collage2


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
    for i in file:
        if (not str(i).endswith(".gitkeep")):
            fullname = os.path.join(path, i)
            if (os.path.isdir(os.path.join(path, i))):
                datos.Insert(parent, fullname, i, values=[], icon=folder_icon)
                config2(os.path.join(path, i), fullname, datos)
            else:
                 if i.endswith(".jpg"):
                    datos.Insert(parent, fullname, i, values=[], icon=file_icon)
                
    return datos


def collage(datos:any) -> sg.Window:
    """
        Funcion que crea la ventana "generador_meme"

        no requiere parametros

        retorna sg.Window

        La función "generador_collage" es para un collage de imágenes que el usuario tenga almacenada,
        las funcionalidades que debería la ventana son:
        "Abrir imágenes" busca localmente las imágenes que vayas a usar para hacer el collage,
        muestra una lista donde está la ubicación de donde están las imágenes seleccionadas en la interfaz,
        crea el collage una vez las imágenes fueron seleccionadas y por último, guarda el collage en la
        Ubicación que el usuario desee
    """
    layoutUnlpImage = [[sg.Text('UNLPImage'), sg.Push(), sg.Text(
        'Generador collage'), sg.Push(), sg.Button("⇦ Atras", key="-ATRAS-", size=(10, 2))]]

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
        [sg.Text("Seleccionar collage:"), sg.Push()],
        [sg.Text(""), tree, sg.Text("", size=(2, 0)), sg.Push(),
         sg.Image(source=IMG_DEFAULT, size=(350, 350), key="-IMG-"), sg.Push()],
        [sg.Text("", size=(30, 0)),
         sg.Text("", size=(30, 80)), sg.Button("Elegir collage", key="-GENERAR-", size=(11, 2))]
    ]

    # Crea la ventana de PySimpleGUI
    all = [[sg.Column(layout, justification='c',
                      element_justification='c'), layoutUnlpImage]]

    return sg.Window("Creador de collage", all, size=SIZE_DEFAULT, element_justification='c')


def generador_collage():
    """
       Funcion que ejecuta la ventana "generador_memes"
       contiene parte de la funcionalidad 

       no requiere parametros

       retorna ningun valor
    """
    datos = sg.TreeData()
    datos = config2(TEMPLATE_COLLAGE, "", datos)
    window = collage(datos)
    while True:

        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                window.close()
                return 0
            case "-TREE-":
                try:
                    es_archivo = values["-TREE-"][0] != "MH"
                    if (es_archivo):
                        ruta = os.path.join(TEMPLATE_COLLAGE,
                                            values["-TREE-"][0])
                        window["-IMG-"].update(
                            source=redimensionar_imagen(ruta, (350, 350)))
                except:
                    ruta = ""
                    window["-IMG-"].update(source=(IMG_DEFAULT),
                                           size=(350, 350))
            case "-GENERAR-":
                if(imagenes_para_hacer_collage() == []):
                    sg.popup_no_border( "Usted no tiene ninguna imagen estiquetada, \n debe tener al menos una imagen etiquetada ",background_color= "white" ,text_color="black")
                    continue
                else:
                    window.hide()
                    valor = os.path.basename(values["-TREE-"][0])
                    try:
                        event = generador_collage2(int(valor[0:2]), valor)
                    except ValueError:
                        event = generador_collage2(int(valor[0]), valor)
                    window.un_hide()
            case"-ATRAS-":
                window.close()
                break
        
        if event == 0:
            window.close()
            return 0
