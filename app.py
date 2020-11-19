from flask import Flask
from config import Configuration
from posts.blueprint import posts
from goods.blueprint import goods
from tests.blueprint import tests

# __name__ - имя текущего файла app.py
app = Flask(__name__)

# Подключение конфигурации
app.config.from_object(Configuration)

# Регистрация blueprint (экземпляр класса Blueprint,путь до нашего blueprint)
app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(goods, url_prefix='/goods')
app.register_blueprint(tests, url_prefix="/tests"
                                         "")
