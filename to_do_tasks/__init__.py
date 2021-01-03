import os

from flask import Flask


def create_app(test_config=None):
    # create the Flask
    app = Flask(__name__, instance_relative_config=True)

    # configure the app
    app.config.from_mapping(
        SECRET_KEY='dev1',
        DATABASE=os.path.join(app.instance_path, 'to_do_tasks.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    # import helper DB functions
    from . import db
    db.init_app(app)    


    # register the 'tasks' blueprint
    from .blueprints.tasks import tasks_bp
    app.register_blueprint(tasks_bp)

    # register the 'taskslist' blueprint
    from .blueprints.taskslist import taskslist_bp
    app.register_blueprint(taskslist_bp)

    return app