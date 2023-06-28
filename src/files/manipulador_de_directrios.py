import os
from pathlib import Path
from PIL import Image
from typing import Literal
from src.constants.directions import BASE_USER_IMG_DIR,IMAGE_DIR,MEMES_DIR,COLLAGE_DIR

user_img_folders = ['avatars', 'collages', 'memes']

UserImagesTypes = Literal['avatars', 'collages', 'memes']

def create_user_images_dirs(username: str) -> None:
    user_dir = Path(os.path.sep.join([BASE_USER_IMG_DIR, username]))
    user_dir.mkdir(parents=True, exist_ok=True)
    for folder in user_img_folders:
        user_dir.joinpath(folder).mkdir(parents=True, exist_ok=True)
    cargar_memes_defults(username)
    cargar_collages_defults(username)

def get_image_name(abs_path: str) -> str:
    return Path(abs_path).name

def get_user_image_location(username: str, tipo: UserImagesTypes, name: str) -> str:
    return os.path.sep.join([BASE_USER_IMG_DIR,username,tipo,name])

def get_user_location(username: str, tipo: UserImagesTypes) -> str:
    return os.path.sep.join([BASE_USER_IMG_DIR, username, tipo])

def save_image(path: str, tipo:UserImagesTypes, username:str) -> None:
    name_img = get_image_name(path)
    image = Image.open(path)
    destin = get_user_image_location(username,tipo,name_img)
    image.save(destin)

def cargar_memes_defults(username: str) -> None:
    user_dir = os.path.sep.join([BASE_USER_IMG_DIR, username,"memes",".gitkeep"])
    archivo = open(user_dir, 'w')
    archivo.close()

def cargar_collages_defults(username: str) -> None:
    user_dir = os.path.sep.join([BASE_USER_IMG_DIR, username,"collages",".gitkeep"])
    archivo = open(user_dir, 'w')
    archivo.close()