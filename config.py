import os


class Config:

    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?{}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ARTICLES_BASE_URL= 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    parent class

    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
