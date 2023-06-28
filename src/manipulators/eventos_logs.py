import os
from src.constants.directions import EVENTS
import csv
import time

def inicializar_csv() -> None:
    """
    Inicializa el archivo CSV para el registro de eventos.

    Returns:
        None
    """
    with open(EVENTS, 'w', newline='',encoding="UTF-8") as csv_file:
        writer = csv.writer(csv_file,delimiter=";")
        writer.writerow(['Fecha y hora', 'Usuario',
                        'Operacion',"Ruta imagen","Texto"])
    


def registrar_evento_log(user: str,operacion: str,url:str = None,Texto:str = None ) -> None:
    """
    Registra un evento en el archivo de registro.

    Args:
        user (str): El nombre de usuario.
        operacion (str): La operación realizada.
        url (str, optional): La URL de la imagen relacionada (opcional).

    Returns:
        None
    """

    if not os.path.exists(EVENTS):
        print(f"El archivo {EVENTS} no existe")
        inicializar_csv()
        print("El archivo user_logs se creó")

    try:
       
        file_empty = os.stat(EVENTS).st_size == 0 
        with open(EVENTS, 'a', newline='',encoding="UTF-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            fecha_hora = time.time()
            if file_empty:
                writer.writerow(['Fecha y hora', 'Usuario',
                            'Operacion',"Ruta imagen","Texto"]) 
                
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow([fecha_hora, user, operacion,url,Texto])

    except FileNotFoundError:
        print(f"Ocurrio un error al abrir el archivo {EVENTS}")


