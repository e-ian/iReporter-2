"""
module config to configure database
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