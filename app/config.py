import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DB_CONNECTION_STRING = 'postgres://vntugecoaypdwx:f6f2e2061bd82e591f8ff63892499b0b8fb1ea0c0c9afa89b7a51ed7685e49f0@ec2-3-217-87-84.compute-1.amazonaws.com:5432/d1a958r4jes78'
    FRONT_END_URL = 'https://dev-inscholaris-web-student.herokuapp.com/#/'
    EMPLOYER_FRONT_END_URL = 'https://dev-inscholaris-co-op-employer.herokuapp.com/#/verify'
    BACK_END_URL = 'https://dev-inscholaris-api.herokuapp.com/'
    DEBUG = True


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-test.db".format(basedir)
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DB_CONNECTION_STRING = 'postgres://xyprrcsjrxrkdg:73c9a26fba53de293f10f965a9443f270c23c29c1c390b8c49b208ef3bc19712@ec2-54-144-177-189.compute-1.amazonaws.com:5432/d464ivfc7vnh1g'
    FRONT_END_URL = 'https://qa-inscholaris-web-student.herokuapp.com/#/'
    EMPLOYER_FRONT_END_URL = 'https://qa-inscholaris-co-op-employer.herokuapp.com/#/verify'
    BACK_END_URL = 'https://qa-inscholaris-api.herokuapp.com/'
    DEBUG = True


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

