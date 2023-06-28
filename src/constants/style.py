import os
import platform
import PySimpleGUI as sg
from . import directions as dir
FONT_0 = ('Arial 25 bold')
FONT_1 = ('Arial 20 bold')
FONT_2 = ('Arial 19 bold')
FONT_3 = ('Arial 17 bold')
FONT_4 = ('Arial 16 bold')
FONT_5 = ('Arial 15 bold')
FONT_6 = ("Arial 13 bold")
FONT_7 = ("Arial 12 bold")
FONT_8 = ("Arial 11")



ruta = os.path.join(dir.SOURCE_DIR,"database","defaults","user.png")


IMG_DEFAULT = os.path.join(dir.SOURCE_DIR,"database","defaults","default.png")
EST_DEFAULT = os.path.join(dir.SOURCE_DIR,"database","defaults","est.png")
AVATAR_DEFAULT = ruta
GENDER_OPTIONS = ("Masculino", "Femenino", "No Binario", "Otro")
THEME_OPTIONS = sg.theme_list()
THEME_COLORS = {
    "Morning": "#fabc57",
    "Noon": "#9fdee3",
    "Afternoon": "#ff892e",
    "Evening": "#352236",
    "Rain": "#60797d",
    "White": "#f0f0f0",
}


#POR SI SE ABRE EN LINUX
def set_size() -> tuple:
    """
    Establece el tamaño de la ventana de la interfaz gráfica según el sistema operativo.

    Returns:
        tuple: Tamaño de la ventana en píxeles (ancho, alto).
    """
    if platform.system() == 'Linux':
        sg.set_options(font=('Arial', 12))
        return (1000,700)
    else:
        sg.set_options(font=('Arial', 15))
        return (940,700)
    
SIZE_DEFAULT = set_size()


FONT_ST = ["28 Days Later.ttf", "From Cartoon Blocks.ttf", "Golden Sunrise.ttf", "Montague.ttf", "youmurdererbb_reg.ttf"]