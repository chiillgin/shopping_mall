# all configure
class Config:
    #DB he SQLachelmy
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'test2'
    USERNAME = 'root'
    PASSWORD = '123123'
    DB_URI = 'mysql+pymysql://root:123123@127.0.0.1:3306/test2'

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False #不跟踪db修改

#开发环境下配置信息
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True #打印sql

#生产环境中配置
class ProductConfig(Config):
    pass
#把两个环境配置和字符串映射
