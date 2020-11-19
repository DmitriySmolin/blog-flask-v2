from flask import Flask
from config import Configuration

# __name__ - имя текущего файла app.py
app = Flask(__name__)

# Подключение конфигурации
app.config.from_object(Configuration)
