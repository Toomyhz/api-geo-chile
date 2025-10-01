from flask import Flask, render_template
import json
from app.routes.api import api_bp
import os

def create_app(testing:bool = False):
    app = Flask(__name__)

    if testing:
        app.config.from_object("config.TestingConfig")

    else:
        app_config = os.getenv("FLASK_CONFIG","config.DevelopmentConfig")
        app.config.from_object(app_config)
        


    # Cargar datos en memoria
    with open('data/dpa.json',encoding="utf-8") as f:
        app.config["SECTORES"] = json.load(f)
    
    # Registrar blueprints
    app.register_blueprint(api_bp)
    
    @app.route('/')
    def index():
        return render_template("index.html")

    app.config['JSON_AS_ASCII'] = False 
    return app