import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # на Netrun базу храним в постоянной папке /data
    if os.path.isdir('/data'):
        database = os.path.join('/data', 'flaskr.sqlite')
    else:
        database = os.path.join(app.instance_path, 'flaskr.sqlite')

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=database,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    with app.app_context():
        # создаём таблицы только если базы ещё нет
        if not os.path.exists(app.config['DATABASE']):
            db.init_db()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
