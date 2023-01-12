import logging

from flask import Flask, request, render_template, send_from_directory

from functions import search_posts_by_key

from main.views import main_blueprint
from loader.views import loader_blueprint


logger_search = logging.getLogger('search')
logger_load_not_pic = logging.getLogger('not_pic')
logger_error_load = logging.getLogger('error_load')

file_handler_search = logging.FileHandler("search_log.txt")
file_handler_not_pic = logging.FileHandler("not_pic_log.txt")
file_handler_error_load = logging.FileHandler("error_load_log.txt")

formatter_all = logging.Formatter("%(asctime)s : %(message)s")
# Применяем форматирование к обработчику
file_handler_search.setFormatter(formatter_all)
file_handler_not_pic.setFormatter(formatter_all)
file_handler_error_load.setFormatter(formatter_all)

logger_search.addHandler(file_handler_search)
logger_load_not_pic.addHandler(file_handler_not_pic)
logger_error_load.addHandler(file_handler_error_load)



POST_PATH = "../posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint, url_prefix='/post')


@app.route('/search')
def search_page():
    s = request.args.get('s')
    data = search_posts_by_key(s)

    logger_search.info(f'Поиск по значению {s}')

    return render_template('post_list.html', data=data, s=s)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images/", path)


if __name__ == "__main__":
    app.run()
