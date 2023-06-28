import os
from pathlib import Path

#SRC 

SOURCE_DIR = Path(__file__).resolve().parent.parent

 
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = os.path.join(Path(CURRENT_DIR).parent,"database")

USERS_DIR = os.path.join(DATA_DIR,"users","users.json")

MEME_JSON = os.path.join(DATA_DIR,"info_memes","memes.json")

COLLAGE_JSON = os.path.join(DATA_DIR,"template_collage","collage.json")

#SETTINGS
MEMES_DIR =  os.path.join(Path(CURRENT_DIR).parent,"database","defaults","memes")

IMAGE_DIR =  os.path.join(Path(CURRENT_DIR).parent,"database","defaults","images")

COLLAGE_DIR =  os.path.join(Path(CURRENT_DIR).parent,"database","defaults","collage")

TEMPLATE_MEMES =  os.path.join(Path(CURRENT_DIR).parent,"database","template_memes")

TEMPLATE_COLLAGE = os.path.join(Path(CURRENT_DIR).parent,"database","template_collage") 


#DATASETS

USER_LOG = os.path.join(Path(CURRENT_DIR).parent,"dataset","user_log.csv")

EVENTS = os.path.join(Path(CURRENT_DIR).parent,"dataset","events.csv")

METADATA = os.path.join(Path(CURRENT_DIR).parent,"dataset","metadata_images.csv")

#DIR_SETTINGS USERS

USERS_IMG_DIRNAME = 'users_confing'
BASE_USER_IMG_DIR = f'{DATA_DIR}{os.sep}{USERS_IMG_DIRNAME}'

FONT_TYPE = os.path.join(Path(CURRENT_DIR).parent,"database","font_types")

