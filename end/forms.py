# _*_ coding: utf-8 _*_
"""
@File    : forms.py
@Time    : 2020/12/7 09:25 
@Author  : xia
"""

# forms表单信息
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    account = StringField()
    password = StringField()
    remember = IntegerField()                # 记住cookie操作  赋值为0或1