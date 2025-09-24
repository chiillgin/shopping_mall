from flask import Flask
from setting import map_config

#负责创建app
def create_app(config_type):
    app = Flask(__name__)
    #加载项目配置
    app.config.from_object(map_config.get(config_type))
    #加载工具（日志处理。。）

    # 初始化SQLALCHEMY
from comment.models import db

    #blueprint
    return app

