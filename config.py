import os

class Config:
    DEBUG = os.getenv('DEBUG') == 'True'
    PORT = int(os.getenv('PORT', 5000))