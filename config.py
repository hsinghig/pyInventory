import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY='IMPACTGUARD'
    ALLOWED_IMAGE_EXTENSIONS= ["jpeg", "jpg", "png"]
    MAX_CONTENT_LENGTH= 16 * 1024 * 1024
    IMAGE_UPLOADS= os.path.join(basedir, "uploads")
    RECAPTCHA_PUBLIC_KEY= "6Lfty"
    RECAPTCHA_PRIVATE_KEY="6LFSDFFDY"
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'DEVELOPMENT_IMPACT_GUARD'

class TestingConfig(Config):
    DEBUG = True
    Testing = True
    SECRET_KEY = 'TESTING_IMPACT_GUARD'

class ProductionConfig(Config):
    DEBUG=False
    Testing = False
    SECRET_KEY='PRODUCTION_IMPACT_GUARD'