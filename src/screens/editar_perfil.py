import PySimpleGUI as sg
from src.manipulators.settings import Settings
from src.manipulators.resizador import redimensionar_imagen
from src.constants.style import GENDER_OPTIONS,SIZE_DEFAULT,AVATAR_DEFAULT



def ventana_editar_perfil() -> sg.Window:
    """ 
        Funcion que crea la ventana "editar_perfil" 

        no requiere argumentos

        retorna sg.Window
        La función screen_editar_perfil es para modificar un perfil ya creado, en esta ventana se podrá modificar:
        El nombre, la edad, el género y avatar, lo único que no se puede modificar, es el nick del usuario.
        
    """
    user = Settings.get_user()
    layout = [[sg.Text("Editar Perfil")],
              [sg.Text(" ", size=(0, 6))],
              [sg.Push(), sg.Text("CAMBIAR DATOS DE LA CUENTA"), sg.Push()],
              [sg.Text(size=(0, 2))],
              #Modificar el nombre del usuario
              [sg.HorizontalSeparator(), sg.Text("Nuevo Nombre ⬇️"),
               sg.HorizontalSeparator()],
              [sg.Text(" ", (8, 0)), sg.InputText(user["name"], key="-inp-newname-",size=(35, 3)), sg.Button("❓", key="-inp-help-name-")],
               #Modificar la edad del usuario.
              [sg.HorizontalSeparator(), sg.Text("Edad ⬇️"),sg.HorizontalSeparator()],
              [sg.Push(), sg.InputText(user["age"], key=("-inp-newage-"),size=(35, 3)), sg.Button("❓", key="-inp-help-age-")],
              #Modificar el genero del usuario.
              [sg.HorizontalSeparator(), sg.Text("Nuevo Genero ⬇️"),sg.HorizontalSeparator()],
              [sg.Push(), sg.Combo(default_value=(user["gender"]),values=list(GENDER_OPTIONS), key="-inp-newgender-"),sg.Push(),
               sg.Button("❓", key="-inp-help-gender-")]
              ]

    layout2 = [[sg.Text(" ", size=(22, 0)), sg.Button("⇦ Atras", key="-inp-back-", size=(9, 2))],
               [sg.Text("",size=(0,5))],
               #Modificar el avatar del usuario.
               [sg.Push(),sg.Image(source=redimensionar_imagen(user["avatar"],(250,250)), key="-inp-changeavatar-", size=(250, 250)),sg.Input(user["avatar"],visible=False, enable_events=True, key="-inp-brw-"),sg.FileBrowse("🔎",key="-act-"), sg.Push()],
               [sg.Text("",size=(0,2))],
               [sg.Text(" ", size=(22, 0)),sg.Button("Guardar ✔️", key="-inp-save-", size=(9, 2))],
               [sg.Text("",size=(8,0)),sg.Text("¿desea cambiar los datos?"), sg.Checkbox("", key="-inp-changedata-")]
               ]

    all = [[sg.Column(layout, size=(500, 620)),
            sg.Column(layout2, size=(620, 620))]]

    return sg.Window("EDITAR PERFIL", all, size=SIZE_DEFAULT)


def editar_perfil():
    
    """
        Funcion que ejecuta la ventana "editar_perfil"
        contiene toda la funcionalidad de la ventana

        no requiere parametros

        retorna ningun valor
    """
    win = ventana_editar_perfil()
    while True:
        event, values = win.read()
        match event:
            case sg.WIN_CLOSED:
                win.close()
                return 0
            case "-inp-back-":
                win.close()
                break
            case "-inp-brw-":
                try:
                    ruta = values["-inp-brw-"]
                    win["-inp-changeavatar-"].update(source=redimensionar_imagen(ruta,(250,250)))
                    win["-inp-brw-"].update(ruta)
                except:
                    ruta = Settings.get_user()["avatar"]
                    win["-inp-brw-"].update(ruta)
                    win["-inp-changeavatar-"].update(source=redimensionar_imagen(ruta,(250,250)))
            case "-inp-save-":
                #Guarda los cambios que hizo el usuario
                if (values["-inp-changedata-"] == True):
                    if(values["-inp-newname-"] != ""):
                        win["-inp-changeavatar-"].update(source=redimensionar_imagen(values["-inp-brw-"],(250,250)))
                        Settings.actualizar_usuario(values["-inp-newname-"], values["-inp-newage-"], values["-inp-newgender-"], values["-inp-brw-"])
                        Settings.actualizar_json()
                        win.close()
                        break
                    sg.popup_ok("Debe llenar todos los campos")
                else:
                    sg.popup_ok("Debe marcar la checkbox antes de continuar")

                
