from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# __name__ - имя текущего файла app.py
app = Flask(__name__)

# Инициализация бд
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Подключение конфигурации
app.config.from_object(Configuration)

