from flask import Blueprint, jsonify, current_app

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/regiones/', methods=['GET'])
def get_regiones():
    sectores = current_app.config["SECTORES"]
    regiones = [sector for sector in sectores if sector['tipo'] == "region"]
    return jsonify(regiones)


@api_bp.route('/regiones/<codigo>/', methods=['GET'])
def get_region(codigo):
    if len(codigo) != 2 or not codigo.isdigit():
        return jsonify({"error": "Código inválido"}), 400

    sectores = current_app.config["SECTORES"]
    region = next((sector for sector in sectores if sector['tipo'] == "region" and sector['codigo'] == codigo), None)
    if not region:
        return jsonify({"error": "Región no encontrada"}), 404

    return jsonify(region)

@api_bp.route('/regiones/<codigo>/provincias/', methods=['GET'])
def get_provincias_por_region(codigo):
    if len(codigo) != 2 or not codigo.isdigit():
        return jsonify({"error": "Código inválido"}), 400

    sectores = current_app.config["SECTORES"]
    provincias = [sector for sector in sectores if sector['tipo'] == "provincia" and sector['codigo'][:2] == codigo]
    return jsonify(provincias)


@api_bp.route('/provincias/', methods=['GET'])
def get_provincias():
    sectores = current_app.config["SECTORES"]
    provincias = [sector for sector in sectores if sector['tipo'] == "provincia"]
    return jsonify(provincias)

@api_bp.route('/provincias/<codigo>/', methods=['GET'])
def get_provincia(codigo):
    if len(codigo) <= 2 or not codigo.isdigit():
        return jsonify({"error": "Código inválido"}), 400

    sectores = current_app.config["SECTORES"]
    provincia = next((sector for sector in sectores if sector['tipo'] == "provincia" and sector['codigo'] == codigo), None)

    if not provincia:
        return jsonify({"error": "Provincia no encontrada"}), 404

    return jsonify(provincia)

@api_bp.route('/provincias/<codigo>/comunas/', methods=['GET'])
def get_comunas_por_provincia(codigo):
    if len(codigo) <= 2 or not codigo.isdigit():
        return jsonify({"error": "Código inválido"}), 400

    sectores = current_app.config["SECTORES"]
    comunas = [sector for sector in sectores if sector['tipo'] == "comuna" and sector['codigo'][:len(codigo)] == codigo]
    return jsonify(comunas)

@api_bp.route('/comunas/', methods=['GET'])
def get_comunas():
    sectores = current_app.config["SECTORES"]
    comunas = [sector for sector in sectores if sector['tipo'] == "comuna"]
    return jsonify(comunas)

@api_bp.route('/comunas/<codigo>/', methods=['GET'])
def get_comuna(codigo):
    if len(codigo) <= 4 or not codigo.isdigit():
        return jsonify({"error": "Código inválido"}), 400

    sectores = current_app.config["SECTORES"]
    comuna = next((sector for sector in sectores if sector['tipo'] == "comuna" and sector['codigo'] == codigo), None)

    if not comuna:
        return jsonify({"error": "Comuna no encontrada"}), 404

    return jsonify(comuna)

@api_bp.route('/docs/', methods=['GET'])
def get_docs():
    return jsonify({"message": "Documentación de la API Geo Chile"})