import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    PORT = int(os.getenv('PORT', 5000))

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = True