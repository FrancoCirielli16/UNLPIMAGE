import json
import os
from src.constants.directions import MEME_JSON


def buscar_pos() -> str:
    """
    Busca la posición actual en el archivo JSON de memes y devuelve la posición como una cadena de texto.

    Retorno:
        pos: La posición actual en el archivo JSON de memes como una cadena de texto.
    """
    with open(MEME_JSON, "r+", encoding="utf-8") as meme_file:
        meme_list = json.load(meme_file)
        meme_list[-1]["image"] = meme_list[-1]["image"] + 1
        meme_file.seek(0)
        json.dump(meme_list, meme_file)
        meme_file.truncate()
        return str(meme_list[-1]["image"] - 1)


def abrir_json(path_meme:str) -> str:
    """
    Abre el archivo JSON de memes y busca un meme específico según la ruta del meme proporcionada.
    Devuelve el meme si se encuentra en el archivo o una cadena vacía si no se encuentra.

    Parámetros:
        path_meme: La ruta del meme a buscar.

    Retorno:
        meme: El meme encontrado en el archivo JSON o una cadena vacía si no se encuentra.
    """
    try:
        with open(MEME_JSON, "r", encoding="utf-8") as meme_file:
            meme_list = json.load(meme_file)
            for meme in meme_list:
                if meme["image"] == path_meme:
                    return meme
            return ""
    except:
        with open(MEME_JSON, "w", encoding="UTF-8") as memefile:
            return ""