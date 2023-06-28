import json
from src.constants.directions import USERS_DIR

Settings = "" 


class User:
    """
    Clase que representa a un usuario en la aplicación UNLPimage.

    Atributos:
        name (str): Nombre del usuario.
        nickname (str): Apodo del usuario.
        age (int): Edad del usuario.
        gender (str): Género del usuario.
        avatar (str): Ruta del avatar del usuario.
    """
    name: str
    nickname: str
    age: int
    gender: str
    avatar: str

    
    @staticmethod
    def crear_usuario_dic(name: str, nickname: str, age: int, gender: str, avatar: str) -> dict:
        """
        Crea un diccionario con la información del usuario.

        Args:
            name (str): Nombre del usuario.
            nickname (str): Apodo del usuario.
            age (int): Edad del usuario.
            gender (str): Género del usuario.
            avatar (str): Ruta del avatar del usuario.

        Returns:
            dict: Diccionario con la información del usuario.
        """
        return {
            "name": name,
            "nickname": nickname,
            "gender": gender,
            "age": age,
            "avatar": avatar
        }
    
    @staticmethod
    def crear_nuevo_usuario(name: str, nickname: str, age: int, gender: str, avatar: str) -> dict:
        """
        Crea un nuevo usuario con la información proporcionada y lo guarda en el archivo de usuarios.

        Args:
            name (str): Nombre del usuario.
            nickname (str): Apodo del usuario.
            age (int): Edad del usuario.
            gender (str): Género del usuario.
            avatar (str): Ruta del avatar del usuario.

        Returns:
            dict: Diccionario con la información del nuevo usuario.
        """
        new_user = User.crear_usuario_dic(name, nickname, age, gender, avatar)
        try:

            with open(USERS_DIR, "r", encoding="UTF-8", newline="") as users_file:
                users_list = json.load(users_file)
                users_list.append(new_user)
            with open(USERS_DIR, "w", encoding="UTF-8", newline="") as users_file:
                json.dump(users_list, users_file)

        except (FileNotFoundError, json.decoder.JSONDecodeError, TypeError, ValueError):
            with open(USERS_DIR, "w", encoding="utf-8", newline="") as users_file:
                json.dump([new_user], users_file)

        return new_user
    
    @staticmethod
    def actualizar(name: str, gender: str, age: int, avatar: str) -> None:
        """
        Actualiza la información del usuario actual.

        Args:
            name (str): Nuevo nombre del usuario.
            gender (str): Nuevo género del usuario.
            age (int): Nueva edad del usuario.
            avatar (str): Nueva ruta del avatar del usuario.

        Returns:
            None
        """
        User.set_name(name)
        User.set_avatar(avatar)
        User.set_gender(gender)
        User.set_age(age)

    @staticmethod
    def actualizar_json() -> None:
        """
        Actualiza el archivo de usuarios con la información del usuario actual.

        Returns:
            None
        """
        with open(USERS_DIR, "r", encoding="utf-8") as users_file:
            users_list = json.load(users_file)
            i = 0
            for user in users_list:
                if (user["nickname"] == Settings.get_user()["nickname"]):
                    position = i
                i += 1

            users_list[position] = User.crear_usuario_dic(
                Settings.get_user()["name"], Settings.get_user()["nickname"], Settings.get_user()["age"], Settings.get_user()["gender"], Settings.get_user()["avatar"])
        with open(USERS_DIR, "w", encoding="utf-8") as users_file:
            json.dump(users_list, users_file)

    @staticmethod
    def get_usuarios() -> list:
        """
        Obtiene una lista de los apodos de todos los usuarios registrados.

        Returns:
            list: Lista de apodos de usuarios.
        """
        try:
            with open(USERS_DIR, "r", encoding="UTF-8") as users_file:
                users_list = json.load(users_file)
                return list(map(lambda u: u["nickname"], users_list))
        except (FileNotFoundError, json.decoder.JSONDecodeError, ValueError):
            return []
        
    @staticmethod
    def get_usuario(nickname: str) -> dict:
        """
        Obtiene la información de un usuario según su apodo.

        Args:
            nickname (str): Apodo del usuario a buscar.

        Returns:
            dict: Diccionario con la información del usuario encontrado.
        """
        try:
            with open(USERS_DIR, "r", encoding="UTF-8") as users_file:
                users_list = json.load(users_file)
                return list(filter(lambda u: u["nickname"] == nickname, users_list))
        except (FileNotFoundError, json.decoder.JSONDecodeError, ValueError):
            return None
    
    @staticmethod
    def get_usuarioygenero() -> dict:
        """
        Obtiene la información de género de todos los usuarios.

        Returns:
            dict: Diccionario con los apodos de los usuarios como claves y sus géneros como valores.
        """
        usuarios_generos = {}

        try:
            with open(USERS_DIR, "r", encoding="UTF-8") as users_file:
                users_list = json.load(users_file)

                for usuario in users_list:
                    nickname = usuario.get("nickname")
                    genero = usuario.get("gender")

                    if nickname and genero:
                        usuarios_generos[nickname] = genero
            return usuarios_generos
        except (FileNotFoundError, json.decoder.JSONDecodeError, ValueError):
            return None

        return usuarios_generos
    @staticmethod
    def esta_repetido(nickname: str) -> bool:
        """
        Verifica si existe un usuario con el apodo dado.

        Args:
            nickname (str): Apodo del usuario a verificar.

        Returns:
            bool: True si el apodo está repetido, False en caso contrario.
        """
        try:
            with open(USERS_DIR, "r", encoding="UTF-8") as users_file:
                users_list = json.load(users_file)
                return any(u for u in users_list if u["nickname"] == nickname)
        except (FileNotFoundError, json.decoder.JSONDecodeError, ValueError):
            return False
        
    @staticmethod
    def get_nickname() -> str:
        """
        Obtiene el nombre del usuario actual.

        Returns:
            str: Nombre del usuario.
        """
        return User.nickname
    
    @staticmethod
    def get_name() -> str:
        """
        Obtiene el nombre del usuario actual.

        Returns:
            str: Nombre del usuario.
        """
        return User.name
    
    @staticmethod
    def get_gender() -> str:
        """
        Obtiene el genero del usuario actual.

        Returns:
            str: Nombre del usuario.
        """
        return User.gender
    
    @staticmethod
    def get_age() -> str:
        """
        Obtiene la edad del usuario actual.

        Returns:
            str: Nombre del usuario.
        """
        return User.age
    
    @staticmethod
    def get_avatar() -> str:
        """
        Obtiene el avatar del usuario actual.

        Returns:
            str: Nombre del usuario.
        """
        return User.avatar
    
    @staticmethod
    def set_name(name) -> None:
        """
        Establece el nombre del usuario.

        Args:
            name (str): Nuevo nombre del usuario.

        Returns:
            None
        """
        User.name = name
    
    @staticmethod
    def set_avatar(avatar) -> None:
        """
        Establece la ruta del avatar del usuario.

        Args:
            avatar (str): Nueva ruta del avatar del usuario.

        Returns:
            None
        """
        User.avatar = avatar
    
    @staticmethod
    def set_gender(gender) -> None:
        """
        Establece el género del usuario.

        Args:
            gender (str): Nuevo género del usuario.

        Returns:
            None
        """
        User.gender = gender
    
    @staticmethod
    def set_age(age) -> None:
        """
        Establece la edad del usuario.

        Args:
            age (int): Nueva edad del usuario.

        Returns:
            None
        """
        User.age = age

def init_user(settings) -> User:
    """
    Inicializa el módulo de usuarios con la configuración proporcionada.

    Esta función establece la configuración global `Settings` del módulo de usuarios
    con el objeto `settings` proporcionado como argumento. Esto se hace para evitar
    una importación circular entre módulos.

    Args:
        settings: Objeto de configuración para el módulo de usuarios.

    Returns:
        User: Clase `User` actualizada con la configuración `settings`.
    """
    global Settings
    Settings = settings
    return User
