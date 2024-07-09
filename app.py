from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
import os
from random import choice
from waitress import serve


############### CONFIG ###################
RESOURCES_IMAGES_DIR_PATH = 'resources/images'
IMG_SRC_LIST = [
    'https://ae01.alicdn.com/kf/Sc38b35fb096947a4b1b17a2aaa5302ccM/Two-Black-Men-Kissing-Meme-T-Shirt-100-Cotton-Meme-Gay-Black-Two-Men-Kissing-Short.jpg',
    'https://m.media-amazon.com/images/I/71c73uukcHL._AC_SY350_QL65_.jpg',
    'https://ih1.redbubble.net/image.1228442711.9112/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
    'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/newscms/2019_40/3036721/191003-2x1-tyler-hightower-ahdeem-tinsley-ew-1031a.jpg',
    'https://media.tenor.com/Cd9xHzDYBJIAAAAe/kiss-love.png'
]
##########################################


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/')
def image():
    
    # image_path = get_random_image_path()
    image_src = get_random_image_source()

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

def get_random_image_source(src_list=IMG_SRC_LIST):
    # Генерируем случайный индекс для выбора изображения
    src_index = choice(range(len(src_list)))
    # Возвращаем имя выбранного изображения
    src = src_list[src_index]
    return src

if __name__ == '__main__':
    serve(app, listen='*:8000')