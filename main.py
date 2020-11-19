from app import app
import view
from app import db
from posts.blueprint import posts

# Регистрация blueprint (экземпляр класса Blueprint,путь до нашего blueprint)
app.register_blueprint(posts, url_prefix='/blog')

# Создание точки входа
if __name__ == '__main__':
    app.run()
