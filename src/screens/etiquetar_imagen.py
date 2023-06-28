
import random
import PySimpleGUI as sg
from src.constants.directions import IMAGE_DIR
from src.constants.style import IMG_DEFAULT,THEME_COLORS,SIZE_DEFAULT
from src.manipulators.settings import Settings
from PIL import ImageTk
import PIL.Image
import os 
from tkinter import *
from src.manipulators.metadata_imagenes import registrar_evento, obtener_tags_csv, obtener_desc_csv
from src.manipulators.resizador import redimensionar_imagen
import random

def get_tags(lista, ruta):
    """
        Funcion que acumula tags almacenados en la lista(set)

        parametros obligatorios=
            "lista = set"
            "ruta = str"

        retorna str
    """
    try:
        tags = ""
        for item in lista:
            tags += ","+item
        return tags[1:]
    except:
        sg.popup_ok("No hay nada para guardar")




def config2 (path, parent, datos):
    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'
    if (os.path.isdir(path)):
        file = os.listdir(path)
    else:
        file = []
    for i in file : 
        fullname = os.path.join(path,i)
        if (os.path.isdir(os.path.join(path,i))):
            datos.Insert(parent, fullname, i, values=[], icon= folder_icon)
            config2(os.path.join(path,i),fullname,datos)
        else:
            datos.Insert(parent, fullname, i, values=[], icon= file_icon)
             
    return datos



def info(ruta) -> str:
    """
        Funcion que busca informacion de una imagen

        parametros obligatorios=
            "ruta = str"
        
            
        retorna str, Resolucion, TipoDeArchivo y tamaño en KB
    """
    img = PIL.Image.open(ruta)
    x, y = img.size
    type = img.format
    tam = os.path.getsize(ruta) // 1024
    ret = (f"\n size: {tam} kb \n resolution: {x}x{y} px \n type: {type} ")
    return ret, str(x+y), type, tam


def screen_etiquetar_imagen(datos) -> sg.Window:
    """
        Funcion que genera una ventana "Etiquetar_Imagen"

        parametros obligatorios =
            "datos = sg.TreeData"
        
            
        retorna sg.Window ya creada* 
    """

    _user_list = sg.Listbox(
        values=[],
        # expand_y=True,
        size=(27, 3),
        background_color="black",
        no_scrollbar=True,
        highlight_background_color=THEME_COLORS["Rain"],
        text_color="violet",
        highlight_text_color=THEME_COLORS["Morning"],
        enable_events=True,
        key='-tags-',
    )
    _accept_button = sg.Button(
        button_text="Eliminar", key="-CONFIRM-", size=(6, 1), border_width=10, disabled=True)

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

    layout = [[sg.Text("ETIQUETAR IMAGEN"), sg.Push(), sg.Text("", size=(20, 0)), sg.Button("⇦ Atras", key="-inp-back-", size=(10, 2))],
              [sg.Text("", size=(2, 0)), tree, sg.Text("", size=(2, 0)),
                sg.Image(source=IMG_DEFAULT, size=(300, 300), key="-IMG-"), sg.Button("🛈", key="-info-", size=(2, 1), visible=True), sg.Push()],
              [sg.Text("", size=(5, 0)), sg.InputText("#Tags",size=(20, 3), key="-tag-"), sg.Button(
                  "Agregar", key="-inp-tags-", size=(7, 1)), sg.Text("", size=(2, 0)), _user_list, _accept_button],
              [sg.Text("", size=(5, 0)), sg.InputText("Descripcion",size=(20, 2), key="-text-desc-"), sg.Button("Agregar", key="-inp-desc-", size=(7, 1))
                  ,sg.Text("", size=(2, 0)), sg.Text("", size=(40, 3), key="-desc-")],
              [sg.Text("", size=(30, 0)),
               sg.Text("", size=(28, 0)), sg.Text("", size=(9, 0)), sg.Button("Guardar ✔️", key="-inp-save-", size=(10, 2))]]

    return sg.Window('ETIQUETAR IMAGEN', layout, size=SIZE_DEFAULT)


def etiquetar_imagen():
    """
        Funcion que ejecuta la ventana "Etiquetar_Imagen"
        obtiene la funcionalidad de toda la ventana

        no requiere parametros

        no retorna ningun valor


    """
    ret = """"""
    ruta = ""
    datos = sg.TreeData()
    rootnodes = []
    lista = set()
    guardado = True
    descripcion = obtener_desc_csv(ruta)
    datos = config2(Settings.get_path_img(),"",datos)
    window = screen_etiquetar_imagen(datos)
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                window.close()
                return 0
            case "-inp-tags-":
                if (ruta != ""):
                    guardado = False
                    tag = values["-tag-"].strip()
                    if (tag != ""):
                        lista.add(tag)
                        window["-tags-"].update(values=get_tags(lista,
                                                ruta).split(","))
                else:
                    sg.popup_error("Seleccione una imagen primero",background_color= "white" ,text_color="black")
            case "-TREE-":
                try:
                    if(not guardado):
                        eleccion = sg.popup_ok_cancel("Cambios sin guardar, ¿quieres continuar? ",background_color= "white" ,text_color="black")
                        if eleccion == "Cancel":
                            continue
                    guardado = True
                    es_archivo= values["-TREE-"][0] != "MH"
                    if (es_archivo):
                        ruta = os.path.join(
                            Settings.get_path_img(), values["-TREE-"][0])
                        window["-IMG-"].update(source=redimensionar_imagen(ruta, (300, 300)))
                        lista = set(obtener_tags_csv(ruta))
                        window["-tags-"].update(values=list(lista))
                        descripcion = obtener_desc_csv(ruta)
                        window["-desc-"].update("Descripcion: '"+obtener_desc_csv(ruta)+"'")
                except:
                    ruta = ""
                    window["-IMG-"].update(source=(IMG_DEFAULT), size=(300,300))                    
            case "-tags-":
                window["-CONFIRM-"].update(disabled=False)
            case "-CONFIRM-":
                try:
                    lista.remove(values["-tags-"][0])
                    window["-tags-"].update(list(lista))
                except:
                    sg.popup_ok("Seleccione una #TAG valida",background_color= "white" ,text_color="black")
            case "-inp-back-":
                break
            case "-inp-desc-":
                if (ruta != ""):
                    guardado = False
                    descripcion = values["-text-desc-"].strip()
                    window["-desc-"].update(f"Descripcion: '{descripcion}'")
                else:
                    sg.popup_error("Seleccione una imagen primero",background_color= "white" ,text_color="black")
            case "-info-":
                try:
                    ret = info(ruta)[0]
                    sg.popup_no_border( ret,background_color= "white" ,text_color="black")
                    
                except:
                    sg.popup_error("Seleccione una imagen primero",background_color= "white" ,text_color="black")
            case "-inp-save-":
                if(ruta != ""):     
                    ret, res, typ, tam = info(ruta)
                    img = PIL.Image.open(ruta)
                    top = img.size
                    registrar_evento(ruta, descripcion, top, str(tam), typ, get_tags(
                        lista, ruta), Settings.get_user()["nickname"])
                    guardado = True
                    sg.popup_no_border( " Se guardo correctamente la metadata de la imagen ",background_color= "white" ,text_color="black")
                else:
                    sg.popup_error("Seleccione una imagen primero",background_color= "white" ,text_color="black")
            
    window.close()
