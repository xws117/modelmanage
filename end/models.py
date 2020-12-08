# _*_ coding: utf-8 _*_
"""
@File    : models.py
@Time    : 2020/11/23 10:46 
@Author  : xia
"""

# 定义后端用户模型
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash         # 导入密码加密解密方法的库
from flask_login import UserMixin

class Account(UserMixin, db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(36), nullable=False)
    priority = db.Column(db.String(10))
    describe = db.Column(db.String(256))
    createdatetime = db.Column(db.DateTime)
    def __init__(self, username, password, priority, describe, createdatatime):
        self.username = username
        self.password = password
        self.priority = priority
        self.describe = describe
        self.createdatatime = createdatatime

        # # 密码加密操作
        # @property
        # def password(self):  # 密码取值
        #     return self._password
        #
        # @password.setter  # 密码加密
        # def password(self, raw_password):
        #     self._password = generate_password_hash(raw_password)

        # 用于验证后台登录密码是否和数据库一致，raw_password是后台登录输入的密码
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)  # 相当于用相同的hash加密算法加密raw_password，检测与数据库中是否一致
        return self.password == raw_password



class Model(db.Model):
    __tablename__ = "model"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    version = db.Column(db.String(100))
    md5 = db.Column(db.String(100))
    describe = db.Column(db.String(256))
    createdatetime = db.Column(db.DateTime)
    createuser = db.Column(db.Integer)
    updatedatetime = db.Column(db.DateTime)
    updateuser = db.Column(db.Integer)

    def __init__(self,name,version,md5,describe,createdatetime,createuser,updatedatetime,updateuser):
        self.name = name
        self.version = version
        self.md5 = md5
        self.describe = describe
        self.createdatetime = createdatetime
        self.createuser = createuser
        self.updatedatetime = updatedatetime
        self.updateuser = updateuser
