"""
module config
"""
class Config:
    """
    parent config class
    """
    DEBUG = False
    dbname = "iReporterdb"

class DevelopmentConfig(Config):
    """
    class for development configuration
    """
    DEBUG = True

class TestingConfig(Config):
    """
    class for testing configuration
    """
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    """
    class for Production configuration
    """
    DEBUG = True
    DATABASE_URI = "postgres://bmwdqpkfurzqev:b4ee0a501e7c5132bc0b157a36436af9696f2cb1e4470d53503c2aefd953ee8f@ec2-54-83-50-174.compute-1.amazonaws.com:5432/da51826nqt75f"

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}