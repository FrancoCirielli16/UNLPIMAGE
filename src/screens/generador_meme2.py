import os
import PIL
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageDraw, ImageFont
from src.manipulators.eventos_logs import registrar_evento_log
from src.constants.directions import DATA_DIR, FONT_TYPE
from src.manipulators.resizador import redimensionar_imagen
from src.files.manipulador_de_directrios import get_user_image_location,get_image_name
from src.manipulators.settings import Settings
from src.constants.style import FONT_ST
from src.manipulators.memes import buscar_pos


def tamanio(x1:int, y1:int, x2, y2) -> tuple:
    """
    Calcula el tamaño de un rectángulo dado los puntos de las esquinas superior izquierda y la inferior derecha.

    Args:
        x1 (int): Coordenada x de la esquina superior izquierda.
        y1 (int): Coordenada y de la esquina superior izquierda.
        x2 (int): Coordenada x de la esquina inferior derecha.
        y2 (int): Coordenada y de la esquina inferior derecha.

    Returns:
        tuple: Tamaño del rectángulo en forma de una tupla (ancho, alto).
    """
    return (x2 - x1, y2 - y1)


def ajustar(tam:int, draw:any, text:str, path:str) -> int:
    """
    Ajusta el tamaño de una fuente de texto para que se ajuste a un rectángulo dado.

    Args:
        tam (tuple): Tamaño del rectángulo objetivo en forma de una tupla (ancho, alto).
        draw: Objeto ImageDraw utilizado para dibujar en una imagen.
        text (str): Texto a dibujar.
        path (str): Ruta del archivo de fuente de texto.

    Returns:
        int: Tamaño de fuente ajustado.
    """
    for i in range(100, 5, -5):
        fuente = ImageFont.truetype(path, i)
        tam2 = draw.textbbox((0, 0), text=text, font=fuente)
        tam2 = tamanio(*tam2)
        if tam[0] >= tam2[0] and tam[1] >= tam2[1]:
            return i


def actualizar_imagen(window:any, num_boton:int, json:any, values:any, img:any,  draw:any, tipo:str,color:str) -> ImageTk.PhotoImage:
    """
    Actualiza la imagen en una ventana con un texto nuevo dibujado en la posición especificada.

    Args:
        window: Ventana de PySimpleGUI.
        num_boton (int): Índice del botón que activó la actualización.
        json: Datos JSON que contienen la información del cuadro de texto.
        values: Valores de entrada actuales de la ventana.
        img: Imagen original.
        draw: Objeto ImageDraw utilizado para dibujar en la imagen.
        tipo (str): Ruta del archivo de fuente de texto.
        color (str): Color del texto.

    Returns:
        ImageTk.PhotoImage: Imagen actualizada.
    """
    tam = tamanio(json["text_boxes"][num_boton]["top_left_x"], json["text_boxes"][num_boton]["top_left_y"],
                  json["text_boxes"][num_boton]["bottom_right_x"], json["text_boxes"][num_boton]["bottom_right_y"])
    text = values["-inp-text-"+str(num_boton)]
    try:
        draw.text((json["text_boxes"][num_boton]["top_left_x"], json["text_boxes"][num_boton]["top_left_y"]), text=text, fill=color,
                font=ImageFont.truetype(font=tipo, size=(ajustar(tam, draw, text, tipo))))
    except:
        print("Error al insertar texto")
    img2 = img
    img = ImageTk.PhotoImage(img)
    window["-image-"].update(data=img, size=(400, 400))
    return img2


def create_boxes(cant:int) -> list:
    """
    Crea la lista de elementos de la interfaz de usuario para ingresar los textos en el generador de memes.

    Args:
        cant (int): Cantidad de cuadros de texto a generar.

    Returns:
        list: Lista de elementos de la interfaz de usuario.
    """
    lista = []
    fonts = [str(x) for x in FONT_ST]
    lista.append([sg.Text("Generador Meme")])
    lista.append([sg.Text("", size=(0, 2))])
    lista.append([sg.Text("", size=(0, 3))])
    lista.append([sg.Button("Borrar textos", key="-inp-volver-"), sg.Combo(
        values=fonts, default_value="Default", key="-inp-selecc-", size=(8, 3), enable_events=True), sg.Combo("", default_value="black", key="-inp-color-", visible=False), sg.ColorChooserButton("🎨"),])
    for i in range(0, cant):
        lista.append([sg.Text("", size=(0, 1))])
        lista.append([sg.Text("Text " + str(i+1)), sg.InputText(size=(20, 0),
                     key=("-inp-text-"+str(i))), sg.Button("➡", size=(2, 1), key=(str(i)))])
    return lista


def generar_meme(json_item:any) -> sg.Window:
    """
    Genera la ventana del generador de memes con los cuadros de texto y la imagen base.

    Args:
        json_item: Datos JSON del meme.

    Returns:
        sg.Window: Ventana del generador de memes.
    """
    fila = create_boxes(len(json_item["text_boxes"]))

    image_file = os.path.join(DATA_DIR, "template_memes", json_item["image"])

    colum2 = [
        [sg.VPush()],
        [sg.Push(), sg.Button("Volver", key="-inp-back-")],
        [sg.Text("", size=(0, 2))],
        [sg.Image(source=redimensionar_imagen(image_file, (400, 400)),
                  size=(400, 400), key="-image-")],
        [sg.VPush()],
        [sg.Push(), sg.Button("Guardar", key="-inp-save-")]
    ]
    layout = [[sg.Column(fila, size=(420, 620)),
               sg.Column(colum2, size=(500, 620))]]
    win = sg.Window("GENERADOR MEME", layout=layout, size=(920, 620))
    return win


def eje_generar_meme(json_tem:any):
    """
    Ejecuta el generador de memes y controla los eventos de la ventana.

    Args:
        json_tem: Datos JSON del meme.

    Returns:
        int: Valor de retorno (0 en caso de cerrar la ventana).
    """
    window = generar_meme(json_tem)
    img = ""
    img2 = os.path.join(DATA_DIR, "template_memes", json_tem["image"])
    img3 = Image.open(img2)
    img3.thumbnail((400, 400))
    img = img3.copy()
    draw = ImageDraw.Draw(img)
    selec = "Golden Sunrise.ttf"
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                window.close()
                return 0
            case "-inp-back-":
                break
            case "-inp-save-":
                i = buscar_pos()
                nom, tip = str(json_tem["image"]).split(".")
                ult = str(nom+str(i)+"."+tip)
                destino = get_user_image_location(
                Settings.get_user()["nickname"], "memes", ult)
                img.save(destino)
                texto = ""
                for i in range(0,len(json_tem["text_boxes"])):
                    texto += ","+values["-inp-text-"+str(i)]
                sg.popup_no_border (" Se guardo correctamente el meme que creo. \n Puede encontrarlo en la carpeta de tu usuario ",background_color= "white" ,text_color="black")
                registrar_evento_log(Settings.get_user()[
                                     "nickname"], "Genero-meme", json_tem["image"],texto)
            case "-inp-selecc-":
                selec = values["-inp-selecc-"]
            case "-inp-volver-":
                img = img3.copy()
                draw = ImageDraw.Draw(img)
                window["-image-"].update(data=ImageTk.PhotoImage(img),
                                         size=(400, 400))
            case __:
                tipo = os.path.join(FONT_TYPE, selec)
                img = actualizar_imagen(window, int(
                    event), json_tem, values, img, draw, tipo, values["-inp-color-"])
    window.close()