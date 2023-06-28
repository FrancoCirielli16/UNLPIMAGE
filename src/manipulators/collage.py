import glob
import json
import os
from PIL import ImageTk, ImageFont
import PIL
from src.constants.directions import FONT_TYPE
from src.manipulators.metadata_imagenes import obtener_imgs_csv
from src.manipulators.settings import Settings
from src.constants.directions import COLLAGE_JSON


def actualizar_imagen(window:any, values:any, img:any, draw:any, path:str) -> ImageTk:
    """
    Actualiza la imagen en la ventana con el texto ingresado por el usuario.

    Parámetros:
        window (object): Objeto de la ventana en la que se mostrará la imagen.
        values (dict): Diccionario de valores que contiene el texto ingresado por el usuario.
        img: Imagen original.
        draw: Objeto de dibujo para realizar operaciones en la imagen.
        path: Ruta de la imagen.

    Retorno:
        img2: Imagen original.
    """
    src = path.split(os.sep)[-1]
    json = abrir_json(src)

    font = os.path.join(FONT_TYPE, "Golden Sunrise.ttf")
    font = ImageFont.truetype(font=font, size=40)

    text = values["-text-title-"]

    draw.text((json["text_boxes"][-1]["top_left_x"], json["text_boxes"][-1]["top_left_y"]), text=text, fill="red", font=font)

    img2 = img

    img = ImageTk.PhotoImage(img)
    window["-IMG-"].update(data=img, size=(600, 600))

    return img2


def imagenes_para_hacer_collage() -> list:
    """
    Devuelve una lista de nombres de archivos de imágenes disponibles para hacer un collage.

    Retorno:
        nombres_imagen: Lista de nombres de archivos de imágenes.
    """
    extensiones_imagen = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    archivos_imagen = [os.path.basename(archivo) for extension in extensiones_imagen for archivo in glob.glob(f'{Settings.get_path_img()}/{extension}')]
    nombres_imagen = []
    imagenes_etq = obtener_imgs_csv()
    for archivo_imagen in archivos_imagen:
        nombre_archivo = os.path.basename(archivo_imagen)
        if archivo_imagen in imagenes_etq:
            nombres_imagen.append(nombre_archivo)

    return nombres_imagen


def calcular_path(nombre:str)-> str:
    """
    Calcula la ruta completa de una imagen basada en el nombre recibido como parámetro.

    Parámetros:
        nombre: Nombre del archivo de imagen.

    Retorno:
        imagen_encontrada: Ruta completa de la imagen correspondiente al nombre.
    """
    extensiones_imagen = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    archivos_imagen = [archivo for extension in extensiones_imagen for archivo in glob.glob(f'{Settings.get_path_img()}/{extension}')]

    imagen_encontrada = [archivo for archivo in archivos_imagen if os.path.basename(archivo) == nombre]
    return imagen_encontrada


def abrir_json(path_collage) -> None:
    """
    Abre un archivo JSON que contiene información sobre un collage y busca el collage correspondiente a la ruta de la imagen recibida como parámetro.

    Parámetros:
        path_collage: Ruta de la imagen correspondiente al collage.

    Retorno:
        c: Collage encontrado en el archivo JSON.
    """
    with open(COLLAGE_JSON, "r", encoding="utf-8") as collage_file:
        collage_list = json.load(collage_file)
        for c in collage_list:
            if c["image"] == path_collage:
                return c


def obtener_medidas(img_box:dict) -> tuple:
    """
    Calcula las dimensiones de una caja delimitadora de una imagen.

    Parámetros:
        img_box: Diccionario que contiene las coordenadas de la caja delimitadora de la imagen.

    Retorno:
        medidas: Tupla que contiene las dimensiones de la caja delimitadora (ancho, alto).
    """
    medidas = (
        img_box["bottom_right_x"] - img_box["top_left_x"],
        img_box["bottom_right_y"] - img_box["top_left_y"]
    )
    return medidas


def cargar_collage(archivo:any, medida:int, x:int, y:int, collage:any) -> ImageTk:
    """
    Carga una imagen en un collage en una posición específica.

    Parámetros:
        archivo: La imagen a cargar.
        medida: El tamaño de la imagen.
        x: La posición X en la que se desea colocar la imagen en el collage.
        y: La posición Y en la que se desea colocar la imagen en el collage.
        collage: El collage en el que se va a cargar la imagen.

    Retorno:
        collage: El collage actualizado con la imagen cargada.
    """
    imagen = PIL.ImageOps.fit(archivo, medida)
    collage.paste(imagen, (x, y))
    return collage

