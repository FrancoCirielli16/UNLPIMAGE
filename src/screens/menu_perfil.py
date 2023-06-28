import subprocess
import PySimpleGUI as sg
from src.constants.directions import *
from src.constants.style import *
from src.screens.editar_perfil import editar_perfil
from src.screens.etiquetar_imagen import etiquetar_imagen
from src.screens.generador_memes import generador_memes
from src.screens.configuracion import configuracion
from src.screens.generador_collage import generador_collage
from src.manipulators.settings import Settings
from src.manipulators.resizador import redimensionar_imagen
from src.constants.style import SIZE_DEFAULT,EST_DEFAULT
from src.files.manipulador_de_directrios import get_user_image_location
def menu_perfil() -> sg.Window:
    """
    Funcion menu_perfil que retorna la pantalla de menu principal con los botones de etiquetar meme, generar collage, configuración
    ayuda y salir
    """
 
    # lista botones de opciones
    lista_opcion = [[sg.Button(button_text="Etiquetar imagenes", key="-ETIQUETAR-", size=(21, 4))],
                    [sg.Button(button_text="Generar meme",
                               key="-MEME-", size=(21, 4))],
                    [sg.Button(button_text="Generar collage",
                               key="-COLLAGE-", size=(21, 4))],
                    [sg.Button(button_text="Salir",
                               key="-SALIR-", size=(21, 4))]
                    ]

    # centralizo botones de opciones en la pantalla
    colum_opciones = [[sg.Column(lista_opcion)]]

    layout = [[sg.Column([[sg.Button(image_data=redimensionar_imagen(Settings.get_user()["avatar"], (80,80)) , key= "-USUARIO-",border_width=5)]]), sg.Push(),sg.Column([[sg.Button(button_text="❔", key="-AYUDA-"), sg.Button(button_text="⚙️", key="-CONFIGURACION-")]],size=(100,60))],
              [sg.Text("",size=(0,2))],
              [sg.Push(), sg.Column(colum_opciones,element_justification="center"), sg.Push()],
              [sg.Push(),sg.Column([[sg.Button(image_data=redimensionar_imagen(EST_DEFAULT, (40,60)), key="-ESTAD-")]])]
            ]

    return sg.Window("MENU", layout, size=SIZE_DEFAULT)



def menu():

    """
    Funcion menu que realizan las conexiones de los botones con las funcionalidades del sistema y el 
    retorno al menu
    """
   
    menu_window = menu_perfil()
    while True: 
        event ,values = menu_window.read()
        if (event == sg.WIN_CLOSED):
            menu_window.close()
            break
        match event:
            case "-CONFIGURACION-":
                menu_window.close()
                event = configuracion()
                menu_window = menu_perfil()
            case "-AYUDA-":
                sg.popup_no_border("UNLPIMAGE: crea memes, edita y etiqueta iamgenes \n \n 👉 Si queres cambiar el directorio de donde se guardan las imagenes, haz click en ⚙️ \n \n 👉 Si queres editar tu perfil, haz click en tu foto \n" ,background_color= "white" ,text_color="black")
            case "-ETIQUETAR-":
                if (Settings.get_user() != None):
                    menu_window.hide()
                    event = etiquetar_imagen()
                    menu_window.un_hide()
            case "-MEME-":
                menu_window.hide()
                event = generador_memes()
                menu_window.un_hide()
            case "-COLLAGE-":
                menu_window.close()
                event = generador_collage()
                menu_window = menu_perfil()
            case "-USUARIO-":
                menu_window.close()
                event = editar_perfil()
                menu_window = menu_perfil()
            case "-SALIR-":
                menu_window.close()
            case "-ESTAD-":
                decision = sg.popup_yes_no("La app puede tardar en abrir\n¿Esta seguro que quieres abrirla?",background_color= "white" ,text_color="black")
                if(decision == "Yes"):
                    if(platform.system() == 'Linux'):
                        subprocess.check_output("python -m streamlit run ."+os.sep+"src"+os.sep+"screens"+os.sep+"Pandas"+os.sep+"Strlit"+os.sep+"Inicio.py",shell=True)
                    else:
                        subprocess.Popen("python -m streamlit run ."+os.sep+"src"+os.sep+"screens"+os.sep+"Pandas"+os.sep+"Strlit"+os.sep+"Inicio.py",creationflags=subprocess.CREATE_NEW_CONSOLE)
        if event == 0:
            menu_window.close()
            break