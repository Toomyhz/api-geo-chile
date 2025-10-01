import os
from app import create_app

def test_config_testing(monkeypatch):
    # Forzamos la variable de entorno
    monkeypatch.setenv("FLASK_CONFIG", "config.TestingConfig")
    
    app = create_app()
    assert app.config["TESTING"] is True
    assert app.config["DEBUG"] is False

def test_config_development(monkeypatch):
    monkeypatch.setenv("FLASK_CONFIG", "config.DevelopmentConfig")
    
    app = create_app()
    assert app.config["DEBUG"] is True
    assert app.config["TESTING"] is False
