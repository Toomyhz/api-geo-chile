from flask import Flask, render_template
import json, os
from app.routes.api import api_bp
from app.extensions.limiter import limiter



base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir,"..","data","dpa.json")



def create_app(testing:bool = False):
    app = Flask(__name__)

    if testing:
        app.config.from_object("config.TestingConfig")

    else:
        app_config = os.getenv("FLASK_CONFIG","config.DevelopmentConfig")
        app.config.from_object(app_config)
        


    # Cargar datos en memoria
    with open(data_path,encoding="utf-8") as f:
        app.config["SECTORES"] = json.load(f)
    
    # Registrar blueprints
    app.register_blueprint(api_bp)

    limiter.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    app.config['JSON_AS_ASCII'] = False

    return app