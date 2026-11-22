import os

from flask import Flask

from . import db
from . import auth
from . import blog


def create_app(test_config=None):
    # создаём и настраиваем приложение
    app = Flask(__name__, instance_relative_config=True)

    # на Netrun базу храним в постоянной папке /data,
    # локально — в instance, как раньше
    if os.path.isdir('/data'):
        database = os.path.join('/data', 'flaskr.sqlite')
    else:
        database = os.path.join(app.instance_path, 'flaskr.sqlite')

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=database,
    )

    if test_config is None:
        # загружаем config.py из папки instance, если он есть
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # гарантируем, что папка instance существует
    os.makedirs(app.instance_path, exist_ok=True)

    # простой тестовый маршрут
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    # делаем blog.index главной страницей "/"
    app.add_url_rule('/', endpoint='index')

    with app.app_context():
        # создаём таблицы только если базы ещё нет
        if not os.path.exists(app.config['DATABASE']):
            db.init_db()

    return app

"""запуск приложения"""
# flask --app flaskr run --debug

"""создание базы данных"""
# flask --app flaskr init-db
