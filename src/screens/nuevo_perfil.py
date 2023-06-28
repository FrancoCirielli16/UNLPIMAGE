import PySimpleGUI as sg
from src.manipulators.user import User 
from PIL import Image, ImageTk
import string
import random as ram
from src.constants.style import GENDER_OPTIONS,AVATAR_DEFAULT,SIZE_DEFAULT
from src.manipulators.resizador import redimensionar_imagen
from src.files.manipulador_de_directrios import get_image_name,create_user_images_dirs,save_image


def check(dato):
    """
        Funcion que comprueba si la edad ingresada es un numero válido

        Parametros obligatorios=
            "dato = any"
        
        retorna Boolean
    """
    try:
        if(int(dato)<0):
            sg.popup_ok("Numero negativos no!")
            return False
        return True
    except:
        sg.popup_ok("La edad debe ingresar como un numero")
        return False


def ventana_nuevo_perfil () -> sg.Window:
    """  
        Funcion que crea la ventana "nuevo_perfil"
        
        no requiere argumentos

        retorna sg.Window
        
        Esta función es para generar un nuevo perfil, el usuario va a poder elegir su nickname posteriormente
       tendrá que rellenar los espacios de nombre, edad, género y seleccionar un avatar.
    """
    layout = [[sg.Text("Nuevo Perfil", font="Harry")],
              [sg.Text(" ", size=(0, 8))],
              #El usuario va a ingresar un Nickname.
              [sg.HorizontalSeparator(), sg.Text("NICKNAME ⬇️"),
               sg.HorizontalSeparator()],
              [sg.Push(), sg.InputText("", key="-inp-user-", size=(35, 3)),
               sg.Button("🎲", key="-inp-help-user-"), sg.Push()],
               #El usuario tendra que ingresar su nombre.
              [sg.HorizontalSeparator(), sg.Text("NOMBRE ⬇️"),
               sg.HorizontalSeparator()],
              [sg.Push(), sg.InputText("", key="-inp-name-", size=(35, 3)),
               sg.Button("❓", key="-inp-help-name-"), sg.Push()],
               #El usuario tendra que ingresar su edad.
              [sg.HorizontalSeparator(), sg.Text("EDAD ⬇️"),
               sg.HorizontalSeparator()],
              [sg.Push(), sg.InputText("", key=("-inp-age-"), size=(35, 3)),
               sg.Button("❓", key="-inp-help-age-"), sg.Push()],
               #El usuario tendra que elegir o seleccionar el genero por el cual el mismo se percibe.
              [sg.HorizontalSeparator(), sg.Text("GENERO ⬇️"),
               sg.HorizontalSeparator()],
              [sg.Push(), sg.Combo(GENDER_OPTIONS, key="-inp-gender-"),
               sg.Button("❓", key="-inp-help-gender-"), sg.Push()],
              ]

    layout2 = [[sg.Text(" ",size=(22,0)), sg.Button("⇦ Atras", key="-inp-back-", size=(10,2))],
                [sg.Text(" ",size=(0,4))],
                #El usuario tendra que seleccionar una imagen para su avatar.
                [sg.Image(source=redimensionar_imagen(AVATAR_DEFAULT,(250,250)), key= "-image-", size=(250,250)),sg.Input(AVATAR_DEFAULT,visible=False, enable_events=True, key="-inp-brw-"),sg.FileBrowse()],
                [sg.Text(" ",size=(0,3))],
                [sg.Text(" ",size=(22,0)),sg.Button("Guardar ✔️", key="-inp-save-", size=(9,2))] 
                ]

    all = [[sg.Column(layout, size=(500, 620)),
            sg.Column(layout2, size=(420, 620))]]

    return sg.Window(title="NUEVO PERFIL", layout=all, size=SIZE_DEFAULT)


def nuevo_perfil():
    """
        Funcion que ejecuta la ventana "nuevo_perfil"
        contiene toda la funcionalidad de la ventana

        no requiere argumentos

        retorna ningun valor
    """
    win = ventana_nuevo_perfil()
    while True:
         event, values = win.read()
         if(event == sg.WINDOW_CLOSED):
             win.close()
             return 0
         match event:
            case "-inp-back-": 
               win.close()
               break
            #Se guardan los datos del usuario, pero si este tiene un nickname ya existente tendra que elegir otro.
            case "-inp-save-":
               if(not User.esta_repetido(values["-inp-user-"])):
                    if ((win["-inp-user-"].get() != "") and (win["-inp-name-"].get() != "")):
                        if(check(win["-inp-age-"].get())):
                            User.crear_nuevo_usuario(values["-inp-name-"],values["-inp-user-"], values["-inp-age-"], values["-inp-gender-"], get_image_name(values["-inp-brw-"]))
                            create_user_images_dirs(values["-inp-user-"])

                            save_image(values["-inp-brw-"],"avatars",values["-inp-user-"])
                            win.close()
                            break
                    else:
                        sg.popup_ok("Debe ingresar todos los datos")
               else:
                   sg.popup_no_border("El usuario que quieres crear ya existe, intente con otro nickname")
            case "-inp-help-user-":
                win["-inp-user-"].update(
                    "".join(ram.choices(string.ascii_letters, k=8)))
            case "-inp-help-name-":
                win["-inp-name-"].update("NOMBRE QUE FIGURA EN TU DNI")
            case "-inp-help-gender-":
                win["-inp-gender-"].update("other")
            case "-inp-help-age-":
                win["-inp-age-"].update("EDAD QUE FIGURA EN TU DNI")
            case "-inp-brw-":
                try:
                    ruta = values["-inp-brw-"]
                    win["-image-"].update(source=redimensionar_imagen(ruta,(250,250)))
                    win["-inp-brw-"].update(ruta)
                except:
                    win["-inp-brw-"].update(AVATAR_DEFAULT)
                    win["-image-"].update(source=redimensionar_imagen(AVATAR_DEFAULT,(250,250)))
