# _*_ coding: utf-8 _*_
"""
@File    : views.py
@Time    : 2020/11/23 09:22 
@Author  : xia
"""

# 前端的蓝图文件  类视图函数写在这里
from flask import Blueprint

front_bp = Blueprint("front_bp", __name__)          # 前端不用前缀，直接在首页显示


@front_bp.route("/")
def index():
    return "front index：前端的首页"