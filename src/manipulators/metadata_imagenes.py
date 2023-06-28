import os
from src.constants.directions import METADATA
import csv
import time
from src.manipulators.eventos_logs import registrar_evento_log
from src.files.manipulador_de_directrios import get_image_name

def inicializar_csv():
    """ Esta funcion inicializa las columnas del archivo .csv 


        no requiere argumentos

        no retorna ningun valor
    """
    with open(METADATA, 'w', newline="", encoding="UTF-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(['Ruta', 'Descripcion',
                        'Resolucion', "Tamaño", "Tipo", "Lista de tags", "Perfil que actualizo", "Ultima actualizacion"])


def registrar_evento(ruta: str, desc: str, resolucion: tuple, tam: str, tipo: str, lista: str, user: str):
    """
        Funcion que registra un evento en un archivo csv
        Parametros obligatorios=
            "ruta = str"
            "desc = str"
            "resolucion = tuple"
            "tam = str"
            "tipo = str"
            "lista = str"
            "user = str"
        No retorna ningun valor 
        Agrega en cualquiera de los casos ** 
    """
   
    ruta = get_image_name(ruta)
    if not os.path.exists(METADATA):
        print(f"El archivo {METADATA} no existe")
        inicializar_csv()
        print("El archivo user_logs se creó")

    try:
        with open(METADATA, 'r+', newline="", encoding="UTF-8") as csv_file:

            reader = csv.reader(csv_file, delimiter=';')

            writer = csv.writer(csv_file, delimiter=";")
            eventos = list(reader)
            if len(eventos) == 0:
                eventos.append((['Ruta', 'Descripcion',
                                 'Resolucion', "Tamaño", "Tipo", "Lista de tags", "Perfil que actualizo", "Ultima actualizacion"]))
            encontre = False
            for item in eventos:
                if (item[0] == ruta):
                    item[1] = desc
                    item[5] = lista
                    item[6] = user
                    encontre = True
                    break
            if not encontre:
                fecha_hora = time.time()
                eventos.append([ruta, desc,str(str(resolucion[0])+","+str(resolucion[1])), tam, tipo,
                                lista, user, fecha_hora])
                registrar_evento_log(user, "imagen-clasificada", ruta)
            else:
                registrar_evento_log(
                    user, "modificacion-imagen", ruta)

            csv_file.seek(0)
            csv_file.truncate()
            writer.writerows(eventos)

    except FileNotFoundError:
        eventos = []
        eventos.append((['Ruta', 'Descripcion',
                         'Resolucion', "Tamaño", "Tipo", "Lista de tags", "Perfil que actualizo", "Ultima actualizacion"]))
        
        fecha_hora = time.time()
        eventos.append([ruta, desc, resolucion, tam, tipo,
                        lista, user, fecha_hora])
        print(f"Ocurrió un error al abrir el archivo {METADATA}")
        try:
            with open(METADATA, 'w', encoding="UTF-8") as csv_file:

                writer = csv.writer(csv_file, delimiter=";")
                writer.writerows(eventos)
        except:
            print("Error irrecuperable")



def obtener_desc_csv(ruta: str):
    """
        Funcion que busca descripcion de una ruta* en especial del .csv

        parametros obligatorios =
            "ruta* = str"
        
        retorna str 
    """
    ruta = get_image_name(ruta)
    try:
        with open(METADATA, 'r',newline="", encoding="UTF-8") as csv_file:
            reader = csv.reader(csv_file,delimiter=";")
            next(reader)
            for data in reader:
                if (data[0] == ruta):
                    return data[1]
            return ""
    except:
        return ""

def obtener_imgs_csv():
    lista_img = []
    try:
        with open(METADATA, 'r',newline="", encoding="UTF-8") as csv_file:
            reader = csv.reader(csv_file,delimiter=";")
            next(reader)
            for data in reader:
                lista_img.append(data[0])
        return lista_img
    except:
        return []
    
def obtener_tags_csv(ruta: str) -> list:
    """ 
        Funcion que busca las tags de una ruta* en especial del .csv


        parametros obligatorio =
            "ruta* = str"

        retorna list
    """
    ruta = get_image_name(ruta)
    try:
        with open(METADATA, 'r', newline="", encoding="UTF-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for data in reader:
                if (data[0] == ruta):
                    if (data[5] != ""):
                        return list(data[5].split(","))
            return []
    except:
        return []

