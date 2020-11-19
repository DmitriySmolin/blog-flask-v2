# Model описание данных, которые хранятся в бд
# View - controller отображение пользователю данных
# Templates связующее звено между бд и пользователем (получение от п-ля запроса, обработка и перенаправление для выполнения)
from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html',n=name)
