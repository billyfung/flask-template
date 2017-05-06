from extensions import db
from config import DefaultConfig, INSTANCE_FOLDER_PATH

from app.api import ApiFlask, ApiException


def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = ApiFlask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)
    configure_hook(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    # TODO production.cfg (not in git)
    # app.config.from_pyfile('production.cfg', silent=True)
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)


def configure_blueprints(app):
    from api import api
    from frontend.views import frontend

    for bp in [api, frontend]:
        app.register_blueprint(bp)


def configure_hook(app):
    app.register_error_handler(
        ApiException, lambda err: err.to_result())
