from comment.models import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(255), nullable=False, unique=True,doc = 'username')
    password = db.Column(db.VARCHAR(255), nullable=False,doc = 'password')
    email = db.Column(db.VARCHAR(255), nullable=False,doc = '邮箱')
    icon = db.Column(db.VARCHAR(255), nullable=False, doc= 'profile')
    nickname = db.Column(db.VARCHAR(255), nullable=False)
    note = db.Column(db.VARCHAR(255), nullable=False)
    phone = db.Column(db.VARCHAR(255), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.now(), doc = '登陆时间')
    create_time = db.Column(db.DateTime, default=datetime.now(), doc = '注册时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate = datetime.now())
    status = db. Column(db.Integer, doc = '用户状态')