import os.path

TOPLEVEL_PATH = os.path.split(os.path.realpath(__file__))[0]
IMAGE_FOLDER = os.path.join(TOPLEVEL_PATH, "generated-images")

def save_image_path(name):
    return os.path.join(IMAGE_FOLDER, name)