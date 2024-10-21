from flask_login import current_user
import os
from PIL import Image
import secrets


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,p_ext= os.splitext(form_picture.filename)
    picture_fn = random_hex + p_ext
    picture_path = os.path.join(current_app.rootpath, 'static/profile_pics', picture_fn)
    i = Image.open(form_picture)
    output_size = (125,125)
    i.thumbnail(output_size)
    i.save_picture(picture_path)
    return picture_fn