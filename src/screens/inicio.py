from pathlib import Path
import PySimpleGUI as sg
from ..constants.style import THEME_COLORS, FONT_0, AVATAR_DEFAULT,SIZE_DEFAULT
from src.screens.menu_perfil import menu
from src.manipulators.user import User
from src.screens.nuevo_perfil import nuevo_perfil
from src.manipulators.settings import Settings
from src.manipulators.users_logs import registrar_user_csv
from src.manipulators.resizador import redimensionar_imagen
from src.manipulators.centrador import centrador
from src.files.manipulador_de_directrios import get_user_image_location
def ventana_inicio() -> None:
    """
    Crea y devuelve una ventana de inicio para la aplicación UNLPimage.

    Returns:
        sg.Window: Ventana de inicio con los elementos gráficos y configuraciones correspondientes.
    """
    _accept_button = sg.Button(
        button_text="Confirmar", key="-CONFIRM-", size=(7, 2), border_width=10, disabled=True)

    _info_perfil = [
        [sg.Image(AVATAR_DEFAULT, key="-IMAGE-")],
        [sg.Text(" ", key="-NICK-"),],
        [sg.Text(" ", key="-NAME-"),],
        [sg.Text(" ", key="-AGE-"),],
        [sg.Text(" ", key="-GENDER-")]
    ]

    sg.set_options(font=('Open Sans', 15))
    #Es el panel con la lista de los usuarios
    _user_list = sg.Listbox(
        values=User.get_usuarios(),
        # expand_y=True,
        size=(28, 12),
        background_color=THEME_COLORS["White"],
        no_scrollbar=True,
        highlight_background_color=THEME_COLORS["Rain"],
        text_color=THEME_COLORS["Evening"],
        highlight_text_color=THEME_COLORS["Morning"],
        enable_events=True,
        key='-ENABLE-',
    )
    #En caso de querer crear un nuevo perfil.
    contenedor_seleccion = sg.Column([[sg.Text("")],
                                      [_user_list],
                                      [sg.Push(), sg.Button(button_text="+", key="-NEW-USER-",
                                                            size=(7, 2), border_width=10), _accept_button, sg.Push()]])

    layout = [[sg.Text('  UNLPimage', size=(0, 2), font=FONT_0)],
              [centrador([contenedor_seleccion, sg.Column(
                  _info_perfil, key="-AVATAR-", visible=False)], horizontal_only=True)],
              [sg.Text("")],
              ]
    return sg.Window('UNLPimage', layout, size=SIZE_DEFAULT, finalize=True) # type: ignore


def inicio() -> None:
    """
    Función principal que inicia la aplicación UNLPimage.

    Muestra la ventana de inicio, carga las rutas predeterminadas de configuración,
    y maneja los eventos de la ventana hasta que se cierre. Dependiendo del evento
    seleccionado, actualiza la información del usuario seleccionado, crea un nuevo
    perfil de usuario o confirma la selección del usuario y avanza al menú principal.

    Returns:
        None
    """
    usuario = ""
    fuente = ('Open Sans', 13)
    inicio_window = ventana_inicio()
    inicio_window["-AVATAR-"].update(visible=False)
    while True:
        event, values = inicio_window.read() # type: ignore
        if event == sg.WIN_CLOSED:
            break
        match event:
            #Muestra los datos de los datos del usuario seleccionado.
            case "-ENABLE-":
                try:
                    usuario = values["-ENABLE-"][0]
                    user = User.get_usuario(usuario)
                    inicio_window["-NICK-"].update("Nickname: " +
                                                   user[0]["nickname"], font=fuente)
                    inicio_window["-NAME-"].update("Nombre: " +
                                                   user[0]["name"], font=fuente)
                    inicio_window["-AGE-"].update("Edad: " +
                                                  user[0]["age"], font=fuente)
                    inicio_window["-GENDER-"].update(
                        "Genero: "+user[0]["gender"], font=fuente)
                    inicio_window["-AVATAR-"].update(visible=True)
                    inicio_window["-IMAGE-"].update(source=redimensionar_imagen(get_user_image_location(user[0]["nickname"],"avatars",user[0]["avatar"]),(250, 250)), size=(255, 255))
                    inicio_window['-CONFIRM-'].update(disabled=False)
                except IndexError:
                    continue
            #En caso de quere generar un nuevo usuario.
            case "-NEW-USER-":
                
                if (inicio_window["-AVATAR-"].visible):
                    inicio_window["-AVATAR-"].update(visible=False)
                inicio_window.close()
                event = nuevo_perfil()
                inicio_window = ventana_inicio()
            #Ingresa al menu perfil con el usuario seleccionado.
            case "-CONFIRM-":
                Settings.set_user(User.get_usuario(usuario)[0])
                Settings.cargar_rutas_default()
                registrar_user_csv(User.get_usuario(usuario)[0])
                inicio_window.close()
                event = menu()
        if event == 0:
            inicio_window.close()
            break
            
            
