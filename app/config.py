class Config:
    APP_KEY = 'Something secret'


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    DEBUG = False


configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
