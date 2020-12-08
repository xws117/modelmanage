# _*_ coding: utf-8 _*_
"""
@File    : hooks.py
@Time    : 2020/12/7 16:11 
@Author  : xia
"""
from flask import request, session, url_for, redirect, g   # g对象全局变量gloabl，方便调用
from .views import mm_backend
from .models import Account


# 钩子函数 ,所有操作前执行该方法，判断当前界面是否是登录界面,不是就将url重定向到登录界面
@mm_backend.before_request
def before_request():
    print(request.path)                                         # 输出的是网页url的后缀，即/cms/login/
    if not request.path.endswith(url_for('end.login')):         # 判断当前所在url是否是/cms/login/，不是代表不在后台登录界面
        user_id = session.get('user_id')                        # 登陆之后，获取登录时候记录的session中的user_id
        if not user_id:                                         # 若没有user_id，说明登录不成功
            return redirect(url_for('end.login'))               # 重定向到后台登录界面

    # 判断user_id是否登陆过，登录之后就返回用户名到CMS后台管理系统
    if 'user_id' in session:
        user_id = session.get('user_id')                        # 调用session中user_id
        user = Account.query.get(user_id)                      # 通过user_id查询到用户对象，方便前端界面调用对象中的字段属性
        if user:
            g.user = user                                   # 赋值给g对象，全局变量g.cms_user用于渲染到后台管理界面cms_index.html

