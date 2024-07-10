from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
import os
from random import choice
from waitress import serve
import yaml


############### CONFIG ###################

RESOURCES_IMAGES_DIR_PATH = 'resources/images'
WEB_SOURCES_FILE_PATH = 'web_sources.yml'

##########################################


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/')
def image():
    global web_sources
    global last_served

    # image_path = get_random_image_path()
    image_src = get_random_image_source(web_sources, last_served)
    last_served = image_src
    return render_template('image.html', image_src=image_src)

def get_random_image_path():
    # Получаем список файлов в директории ресурсов
    images = [f for f in os.listdir(RESOURCES_IMAGES_DIR_PATH) if os.path.isfile(os.path.join(RESOURCES_IMAGES_DIR_PATH, f))]
    # Генерируем случайный индекс для выбора изображения
    image_index = choice(range(len(images)))
    # Возвращаем имя выбранного изображения
    image_name = images[image_index]
    image_path = os.path.join(RESOURCES_IMAGES_DIR_PATH, image_name)
    return image_path

def get_random_image_source(sources: tuple, last_served: str = None):
    # Убираем уже использованную картинку, если есть
    if last_served and isinstance(last_served, str):
        sources = (src for src in sources if src != last_served)
    # Генерируем случайный индекс для выбора изображения
    src_index = choice(range(len(sources)))
    # Возвращаем имя выбранного изображения
    src = sources[src_index]
    return src

def get_image_web_sources_list(file_path: str, key: str):
    with open(file_path, 'r') as web_sources_stream:
        web_sources = yaml.safe_load(web_sources_stream)
        web_sources_list = web_sources[key]
    return web_sources_list

if __name__ == '__main__':
    web_sources = get_image_web_sources_list(WEB_SOURCES_FILE_PATH, 'ryan-gosling')
    last_served = None
    serve(app, listen='*:8000')