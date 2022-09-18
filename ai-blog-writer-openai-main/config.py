##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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-"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
