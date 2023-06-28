
import os
from PIL import ImageDraw
import PIL
import PySimpleGUI as sg
from src.manipulators.collage import calcular_path, imagenes_para_hacer_collage, actualizar_imagen
from src.constants.style import SIZE_DEFAULT
from src.manipulators.collage import abrir_json, cargar_collage, obtener_medidas
from src.files.manipulador_de_directrios import get_user_location, get_image_name
from src.manipulators.settings import Settings
from src.manipulators.eventos_logs import registrar_evento_log


def habilitado(value:any, index:int, window:any) -> bool:
    """
    Verifica si todas las cajas de selección de imágenes anteriores están llenas.

    Args:
        value (dict): Diccionario de valores actuales de la ventana.
        index (int): Índice máximo de las cajas de selección de imágenes.
        window (sg.Window): Ventana de PySimpleGUI.

    Returns:
        bool: True si todas las cajas anteriores están llenas, False en caso contrario.

    """
    for x in range(0, index):
        try:
            if value["-inp-brw-" + str(x)] == "":
                return False
        except:
            return False
    window["-inp-save-"].update(disabled=False)
    return True


def create_boxes(cant:int) -> list:
    """
    Crea las cajas de selección de imágenes y los elementos relacionados en la ventana.

    Args:
        cant (int): Cantidad de cajas de selección de imágenes.

    Returns:
        list: Lista de listas que contiene los elementos de las cajas de selección de imágenes.

    """
    lista = []
    for i in range(0, cant):
        lista.append([sg.Combo(default_value="", values=imagenes_para_hacer_collage(),
                               key="-inp-brw-" + str(i), enable_events=True)])
    lista.append([sg.InputText("Titulo", size=(15, 2), key="-text-title-"),
                  sg.Button("➡", key="-inp-title-", size=(3, 1)),
                  sg.Button("↻", size=(2, 1), key="-inp-reset")])
    lista.append([sg.Button("Generar✔️", key="-inp-save-", size=(12, 2), disabled=True)])
    return lista


def subir_foto(path_collage:str, position_index:int, path_img:str, col:any, window:any):
    """
    Carga una imagen y la superpone en la posición especificada en el collage.

    Args:
        path_collage (str): Ruta del archivo JSON que contiene la información del collage.
        position_index (int): Índice de la posición en el collage donde se superpondrá la imagen.
        path_img (str): Ruta de la imagen a cargar.
        col (PIL.Image): Objeto de imagen del collage actual.
        window (sg.Window): Ventana de PySimpleGUI.

    """
    medidas = abrir_json(path_collage)
    tam = obtener_medidas(medidas["text_boxes"][position_index])
    img = PIL.Image.open(path_img[0])
    col = cargar_collage(img, tam, medidas["text_boxes"][position_index]["top_left_x"],
                         medidas["text_boxes"][position_index]["top_left_y"], col)
    imagen = PIL.ImageTk.PhotoImage(col)
    window["-IMG-"].update(data=imagen)


def collage(x:int) -> sg.Window:
    """
    Genera una ventana para crear un collage de imágenes.

    Args:
        x (int): Cantidad de cajas de selección de imágenes.

    Returns:
        sg.Window: Ventana de PySimpleGUI.

    """

    layout = [[sg.Text("GENERADOR COLLAGE"), sg.Push(), sg.Text("", size=(20, 0)), sg.Button("⇦ Atras", key="-inp-back-", size=(10, 2))],
              [sg.Text("", size=(2, 0)), sg.Column(create_boxes(x)), sg.Push(), sg.Image(size=(600, 600), key="-IMG-")]]

    return sg.Window('ETIQUETAR IMAGEN', layout, size=SIZE_DEFAULT, finalize=True)


def generador_collage2(x:int, path_collage:str):
    """
    Función que contiene la funcionalidad de la ventana "collage" (no contiene su totalidad de funcionalidades).

    Args:
        x (int): Cantidad de cajas de selección de imágenes.
        path_collage (str): Ruta del archivo JSON que contiene la información del collage.

    Returns:
        int: 0 si la ventana se cierra.

    """
    window = collage(x)
    col = PIL.Image.new("RGBA", (600, 600), "black")
    imagen = PIL.ImageTk.PhotoImage(col)
    window["-IMG-"].update(data=imagen)
    while True:
        col2 = PIL.Image.new("RGBA", (600, 600), "black")
        event, values = window.read()
        habilitado(values, x, window)
        match event:

            case sg.WIN_CLOSED:
                window.close()
                return 0
            case "-inp-back-":
                window.close()
                break
            case "-inp-save-":
                destino = get_user_location(Settings.get_user()["nickname"], "collages") + os.sep + values["-text-title-"] + ".png"
                col.save(destino, format="PNG")
                sg.popup_no_border (" Se guardo correctamente el collage que creo. \n Puede encontrarlo en la carpeta de tu usuario ",background_color= "white" ,text_color="black")
                registrar_evento_log(Settings.get_user()["nickname"], "Genero-collage", get_image_name(path_collage), values["-text-title-"])
            case "-inp-title-":
                draw = ImageDraw.Draw(col)
                actualizar_imagen(window, values, col, draw, path_collage)
            case "-inp-reset":
                col = col2
                imagen = PIL.ImageTk.PhotoImage(col)
                window["-IMG-"].update(data=imagen)
                for x in range(0, x):
                    window["-inp-brw-"+str(x)].update("")
            case __:
                index = int(event.split("-")[-1])
                subir_foto(path_collage, index, calcular_path(values[event]), col, window)