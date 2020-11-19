from flask import Blueprint
from flask import render_template

# Создание экземпляра Blueprint(название,путь,папка где хранятся шаблоны)
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    return render_template('posts/index.html')
