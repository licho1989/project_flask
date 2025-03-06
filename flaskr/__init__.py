import os

from flask import Flask

def create_app(test_config=None):
    # Crea y configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Carga la configuracion de la intancia, si existe, cuando no se este probando
        app.config.from_pyfile('config.py', silent=True)

    else:
        # Carga la configuración de pruebas, si pasa
        app.config.from_mapping(test_config)

    # Asegurese de que la carpeta de la instacia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Una página simple que dice Hola
    @app.route('/hello')
    def hello():
        return 'Hello World!'
    
    return app