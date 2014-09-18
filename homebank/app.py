from logging import StreamHandler, WARNING, Formatter
from logging.handlers import WatchedFileHandler
from flask.app import Flask
from flask.templating import render_template
from werkzeug.utils import import_string


def make_app(import_name=__name__,
             config='homebank.settings.Configuration',
             debug=False):

    app = Flask(import_name)
    app.config.from_object(config)
    app.config.from_envvar('FLASK_SETTINGS', silent=True)
    app.debug = debug

    if app.debug:
        import_string('flask.ext.debugtoolbar:DebugToolbarExtension')(app)

    @app.errorhandler(404)
    def not_found(ex):
        return render_template("404.html"), 404

    for blueprint in ['__init__']:
        app.register_blueprint(import_string(
            'homebank.blueprints.%s:root' % blueprint))

    if not app.debug:
        handler = StreamHandler()
        if 'ERROR_LOG' in app.config:
            handler = WatchedFileHandler(app.config['ERROR_LOG'])

        handler.setLevel(WARNING)
        handler.setFormatter(Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        app.logger.addHandler(handler)

    return app