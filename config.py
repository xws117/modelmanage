# -*- encoding: utf-8 -*-
"""
@File    : config.py
@Time    : 2020/5/11 10:08
@Author  : xia

"""
import os

# 127.0.0.1
HOSTNAME = "localhost"
DATABASE = "modelmanage"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URL           # 数据库连接成功

SECRET_KEY = os.urandom(15)        # 产生随机15位字符串加密



# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.
# Set it to True or False to suppress this warning.'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
# 这里是为了解决上面的警告
SQLALCHEMY_TRACK_MODIFICATIONS = False