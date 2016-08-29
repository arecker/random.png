import os
import random
import shutil

from PIL import Image
from flask import Flask, send_file, request


app = Flask(__name__)
here = os.path.dirname(os.path.realpath(__file__))
images = os.path.join(here, 'images')
cache = os.path.join(here, 'cache')

extensions = {
    '.bmp': 'image/bmp',
    '.gif': 'image/gif',
    '.jpeg': 'image/jpeg',
    '.jpg': 'image/jpeg',
    '.png': 'image/png',
}


def has_allowed_extension(path):
    _, ext = os.path.splitext(path)
    return ext in extensions.keys()


def get_mimetype(path):
    _, ext = os.path.splitext(path)
    return extensions[ext]


def get_thumbnail(filename, width=500, height=None):
    target = os.path.join(cache, filename)

    if os.path.exists(target):
        return target

    image = Image.open(os.path.join(images, filename)).copy()
    original_width, original_height = image.size
    image.thumbnail((width or original_width, height or original_height))
    image.save(target)

    return target


@app.route('/')
def serve_random_image():
    choices = filter(has_allowed_extension, os.listdir(images))
    choice = random.choice(choices)
    image = get_thumbnail(choice)
    return send_file(image, mimetype=get_mimetype(image))


@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


if __name__ == '__main__':
    if not os.path.exists(images):
        print('No images directory')
        exit(1)

    try:
        os.makedirs(cache)
    except OSError:
        pass

    try:
        app.run(host='0.0.0.0')
    finally:
        try:
            shutil.rmtree(cache)
        except:
            pass
