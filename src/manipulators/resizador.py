import base64
import io
import os
import PIL
import PySimpleGUI as sg
from src.constants.style import AVATAR_DEFAULT



def redimensionar_imagen(ruta_imagen, redimensionar=None):
    """
    Redimensiona una imagen.

    Args:
        ruta_imagen (str): Ruta de la imagen a redimensionar.
        redimensionar (tuple): Tamaño deseado de redimensionamiento en píxeles. 
                              El formato debe ser (ancho, alto). 
                              Si no se especifica, no se realiza redimensionamiento.

    Returns:
        bytes: Los bytes de la imagen redimensionada en formato PNG.
    """
    if not os.path.exists(ruta_imagen):
        ruta_imagen = AVATAR_DEFAULT

    try:
        if isinstance(ruta_imagen, str):
            img = PIL.Image.open(ruta_imagen)
        else:
            try:
                img = PIL.Image.open(io.BytesIO(base64.b64decode(ruta_imagen)))
            except Exception as e:
                data_bytes_io = io.BytesIO(ruta_imagen)
                img = PIL.Image.open(data_bytes_io)

        ancho_actual, alto_actual = img.size
        if redimensionar:
            nuevo_ancho, nuevo_alto = redimensionar
            escala = min(nuevo_alto/alto_actual, nuevo_ancho/ancho_actual)
            img = img.resize((int(ancho_actual*escala), int(alto_actual*escala)), PIL.Image.ANTIALIAS)
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    except PIL.UnidentifiedImageError:
        sg.popup_error("Debe ingresar un archivo .jpg .png o cualquiera que refiera a una imagen")
        raise
 
