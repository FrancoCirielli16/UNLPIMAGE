
import os
from src.constants.directions import USER_LOG
import time 
import csv

def inicializar_user_csv():
    with open(USER_LOG, 'w', newline='') as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(["fecha sy hora","nickname"])
   

def registrar_user_csv(user: dict):

    if not os.path.exists(USER_LOG):
        print(f"El archivo {USER_LOG} no existe")
        inicializar_user_csv()
        print("El archivo user_logs se creó")

    try:
        file_empty = os.stat(USER_LOG).st_size == 0 

        with open(USER_LOG, 'a', newline='') as file:                
            writer = csv.writer(file, delimiter=';')
            if file_empty:
                writer.writerow(["fecha y hora", "nickname"]) 

            fecha_hora = time.time()

            
            writer.writerow([fecha_hora,user["nickname"]])

    except FileNotFoundError:
        print(f"Ocurrió un error al abrir el archivo {USER_LOG}")




