from flask import Flask, render_template
import json
from app.routes.api import api_bp

def create_app():
    app = Flask(__name__)
    
    # Cargar datos en memoria
    with open('data/dpa.json',encoding="utf-8") as f:
        app.config["SECTORES"] = json.load(f)
    
    # Registrar blueprints
    app.register_blueprint(api_bp)
    
    @app.route('/')
    def index():
        return render_template("index.html")

    return app