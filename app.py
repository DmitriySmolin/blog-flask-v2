from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

# __name__ - имя текущего файла app.py
app = Flask(__name__)

# Инициализация бд
db = SQLAlchemy(app)

# Подключение конфигурации
app.config.from_object(Configuration)



