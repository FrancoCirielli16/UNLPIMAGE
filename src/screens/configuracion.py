import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
from src.constants.directions import IMAGE_DIR,MEMES_DIR,COLLAGE_DIR
from src.constants.style import THEME_OPTIONS,SIZE_DEFAULT
from src.manipulators.settings import Settings
from pathlib import Path
from src.manipulators.eventos_logs import registrar_evento_log


def obtener_ruta(ruta_cruda:str):
    ruta_cruda = ruta_cruda.strip()
    if not ruta_cruda:
        return False
    
    ruta = Path(ruta_cruda)
    if not ruta.is_dir():
        return False
    return str(ruta.resolve())


def screen_configuracion() -> sg.Window:
    """ 
        Funcion que crea la ventana "configuracion"

        no requiere parametros

        retorna sg.Window
        Esta funcion es para configurar donde se van a guardar las imagenes que se vayan generando 
        en la aplicacion la funcionalidad que tiene es:
        Guardar y busca las imagenes en las carpetas correspondientes
    """

    layout = [[sg.Push(), sg.Text("Configuración", size=(17,2), font="Arial 15 bold")]
             ]
    
    layout2 = [[sg.Text("", size=(2,4))],
               [sg.HorizontalSeparator()],
                #Selecciona la carpeta donde se guarda las imagenes.
               [sg.Text("DIRECTORIO DE IMAGENES")],
               [sg.InputText(Settings.get_path_img(), key="-inp-pathimg-", size=(40, 2),
                             border_width=3), sg.FolderBrowse("🔎", size=(2, 1)), sg.Text("⚠️")],
               [sg.HorizontalSeparator()],
               #Seleccionar donde se guardan los collages generados.
               [sg.Text("DIRECTORIO DE COLLAGES")],
               [sg.InputText(Settings.get_path_collage(), key="-inp-pathcollage-", size=(
                   40, 2), border_width=3), sg.FolderBrowse("🔎", size=(2, 1)), sg.Text("⚠️")],
               [sg.HorizontalSeparator()],
               #Selecciona donde se guardan los memes generados.
               [sg.Text("DIRECTORIO DE MEMES")], 
               [sg.InputText(Settings.get_path_meme(),key="-inp-pathmemes-",size=(40,2), border_width=3), sg.FolderBrowse("🔎", size=(2,1)), sg.Text("⚠️")],
               [sg.HorizontalSeparator()],
               #Cambia los temas de la interfaz.
               [sg.Text("TEMAS DE LA INTERFAZ")],
               [sg.Combo(default_value=Settings.get_theme(),values= THEME_OPTIONS,key="-TEMA-",enable_events=True)]
               ]
    
    layout3 = [[sg.Button("⇦ Atras", key="-inp-backbut-",size=(10,2))],
               [sg.Text("",size=(0,19))],
               [sg.Button("Guardar ✔️",key="-inp-savebut-",size=(10,2))]
                ]

    all = [[sg.Column(layout, size=(160,620)),sg.Column(layout2, size=(590,620)), sg.Column(layout3, size=(180,620))]]
 
    return sg.Window("CONFIGURACION", all, size=SIZE_DEFAULT)

def configuracion():
    """
        Funcion que ejecuta la ventana "Connfiguracion"
        contiene toda la funcionalidad de esta ventana

        no requiere parametros

        retorna ningun valor
    """
    window = screen_configuracion()
    while True:
        event, values = window.read()
        match event:
            #Si el usuario selecciona el boton con la key "-input-backbut-"" cierra la ventana
            case  "-inp-backbut-":
                window.close()
                break
            case sg.WIN_CLOSED:
                window.close()
                return 0
            case "-inp-savebut-":
                ruta_1 = obtener_ruta(values["-inp-pathimg-"])
                if not ruta_1:
                    sg.popup_error("La ruta que selecciono para directorio de imagenes no existe",background_color= "white" ,text_color="black")
                    continue
                ruta_2 = obtener_ruta(values["-inp-pathcollage-"])
                if not ruta_2:
                    sg.popup_error("La ruta que selecciono para el direcotrio collage no existe",background_color= "white" ,text_color="black")
                    continue
                ruta_3 = obtener_ruta(values["-inp-pathmemes-"])
                if not ruta_3:
                    sg.popup_error("La ruta que selecciono para el direcotrio memes no existe",background_color= "white" ,text_color="black")
                    continue
                tema = values["-TEMA-"] 
                if tema not in THEME_OPTIONS: 
                    sg.popup_error("El tema que selecciono no es una opcion valida",background_color= "white" ,text_color="black")
                    continue
                Settings.cargar_rutas(ruta_1 ,ruta_2, ruta_3)
                Settings.set_theme(values["-TEMA-"])
                registrar_evento_log(Settings.get_user()["nickname"],"configuracion-modificada")
                window.close()
                break
                    
                    
                
