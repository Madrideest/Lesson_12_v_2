from flask import Blueprint, render_template, request

from functions import add_post_in_file

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/', methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/', methods=["POST"])
def page_post_upload():
    picture = request.files.get('picture')
    if picture:
        filename = picture.filename
        picture.save(f'./uploads/images/{filename}')
        content = request.form.get('content')

        data = add_post_in_file(f'{filename}', content)

        return render_template('post_uploaded.html', data=data)
    else:
        return 'Ошибка загрузки'
