from flask import Blueprint, jsonify, current_app

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/regiones', methods=['GET'])
def get_regiones():
    sectores = current_app.config["SECTORES"]
    regiones = [sector for sector in sectores if sector['tipo'] == "region"]
    return jsonify(regiones)