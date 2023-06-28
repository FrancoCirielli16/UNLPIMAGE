import PySimpleGUI as sg
from src.constants.style import *
from src.manipulators.user import init_user, User
from src.constants.directions import IMAGE_DIR, COLLAGE_DIR, MEMES_DIR
from src.files.manipulador_de_directrios import get_user_location,get_user_image_location

class Settings():
    """
    Clase que almacena la configuración y las opciones de usuario de la aplicación UNLPimage.

    Atributos:
        user (User): Objeto de la clase User que representa al usuario actual.
        theme (str): Tema de PySimpleGUI utilizado en la aplicación.
        path_img (str): Ruta predeterminada para las imágenes.
        path_collage (str): Ruta predeterminada para los collages.
        path_meme (str): Ruta predeterminada para los memes.
        fonts (str): Fuente utilizada en la aplicación.
    """
    user: User
    theme: str = sg.theme("Dark Grey15")
    path_img: str
    path_meme: str
    path_collage: str
    fonts: str

    def cargar_rutas_default() -> None:
        """
        Carga las rutas predeterminadas para imágenes, collages y memes.

        Args:
            img (str): Ruta predeterminada para las imágenes.
            collage (str): Ruta predeterminada para los collages.
            meme (str): Ruta predeterminada para los memes.

        Returns:
            None
        """
        Settings.path_img = IMAGE_DIR
        Settings.path_collage = get_user_location(Settings.user["nickname"],"collages")
        Settings.path_meme = get_user_location(Settings.user["nickname"],"memes")

    def cargar_rutas(img, collage, meme) -> None:
        """
        Carga las rutas predeterminadas para imágenes, collages y memes.

        Args:
            img (str): Ruta predeterminada para las imágenes.
            collage (str): Ruta predeterminada para los collages.
            meme (str): Ruta predeterminada para los memes.

        Returns:
            None
        """
        Settings.path_img = img
        Settings.path_collage = collage
        Settings.path_meme = meme

    def actualizar_json() -> None:
        """
        Actualiza la información del usuario en el archivo JSON.

        Esta función actualiza la información del usuario actual en el archivo JSON
        correspondiente.

        Returns:
            None
        """
        User.actualizar_json()

    def actualizar(user: User, theme: dict) -> None:
        """
        Actualiza la configuración con un nuevo usuario y tema.

        Args:
            user (User): Nuevo objeto de usuario.
            theme (str): Nuevo tema de la aplicación.

        Returns:
            None
        """
        Settings.set_user(user)
        Settings.set_theme(theme)

    def actualizar_usuario(name: str, age: int, gender: str, avatar: str) -> None:
        """
        Actualiza la información del usuario actual.

        Args:
            name (str): Nuevo nombre del usuario.
            age (int): Nueva edad del usuario.
            gender (str): Nuevo género del usuario.
            avatar (str): Nueva ruta del avatar del usuario.

        Returns:
            None
        """
        Settings.user["name"] = name
        Settings.user["age"] = age
        Settings.user["avatar"] = avatar
        Settings.user["gender"] = gender

    def get_user() -> User:
        """
        Obtiene el usuario actual.

        Returns:
            User: Objeto de la clase User que representa al usuario actual.
        """
        if(not os.path.isabs(Settings.user["avatar"])):
            Settings.user["avatar"] = get_user_image_location(Settings.user["nickname"],"avatars",Settings.user["avatar"])
        return Settings.user

    def get_theme() -> str:
        """
        Obtiene el tema de la aplicación.

        Returns:
            str: Tema de PySimpleGUI utilizado en la aplicación.
        """
        return Settings.theme

    def get_path_img() -> str:
        """
        Obtiene la ruta predeterminada para las imágenes.

        Returns:
            str: Ruta predeterminada para las imágenes.
        """
        return Settings.path_img

    def get_path_collage() -> str:
        """
        Obtiene la ruta predeterminada para los collages.

        Returns:
            str: Ruta predeterminada para los collages.
        """
        return Settings.path_collage

    def get_path_meme() -> str:
        """
        Obtiene la ruta predeterminada para los memes.

        Returns:
            str: Ruta predeterminada para los memes.
        """
        return Settings.path_meme

    def set_user(user: User) -> None:
        """
        Establece el usuario actual.

        Args:
            user (User): Objeto de la clase User que representa al usuario actual.

        Returns:
            None
        """
        Settings.user = user

    def set_theme(theme: str):
        """
        Establece el tema de la aplicación.

        Args:
            theme (str): El nombre del tema a establecer.

        Returns:
            None
        """
        Settings.theme = theme
        sg.theme(theme)

    def set_path_img():
        """
        Establece la ruta por defecto para las imágenes.

        Args:
            path (str): La ruta por defecto para las imágenes.

        Returns:
            None
        """
        return Settings.path_img

    def set_path_collage():
        """
        Establece la ruta por defecto para los collages.

        Args:
            path (str): La ruta por defecto para los collages.

        Returns:
            None
        """
        return Settings.set_path_collage

    def set_path_meme():
        """
        Establece la ruta por defecto para los memes.

        Args:
            path (str): La ruta por defecto para los memes.

        Returns:
            None
        """
        return Settings.path_meme


Settings.user = init_user(Settings)
