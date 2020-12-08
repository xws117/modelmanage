# _*_ coding: utf-8 _*_
"""
@File    : views.py
@Time    : 2020/11/23 09:23 
@Author  : xia
"""

# 蓝图文件：实现模块化应用，应用可以分解成一系列的蓝图   后端的类视图函数写在这个文件
from flask import Blueprint,render_template, views, session
from flask import request, redirect, url_for          # 页面跳转redirect   request请求收集
from .forms import LoginForm
from .models import Account


mm_backend = Blueprint("end", __name__, url_prefix='/end/')     # URL前缀url_prefix
from .hooks import before_request



@mm_backend.route("/")  # 后台界面
def index():
    # return "cms index：后端类视图文件"
    return render_template("index.html")

# 用户注销登录
@mm_backend.route("/logout/")                              # 需要关联到cms/cms_index.html中的注销属性
def logout():
    # session清除user_id
    del session['user_id']
    # 重定向到登录界面
    return redirect(url_for('end.login'))             # 重定向(redirec)为把url变为重定向的url

# 定义类视图，显示模板文件
class LoginView(views.MethodView):
    def get(self):
        return render_template("login.html")

    def post(self):
        # 收集表单信息
        login_form = LoginForm(request.form)
        if login_form.validate():
            # 数据库验证
            email = login_form.account.data
            password = login_form.password.data
            remember = login_form.remember.data

            # 查询数据库中的用户信息
            user = Account.query.filter_by(username=email).first()  # 邮箱唯一，用于查询验证用户
            # print("email==",email,"password==",password)
            # print(user)
            # print(user.check_password(password))
            if user and user.check_password(password):  # 验证用户和密码是否都正确
                session['user_id'] = user.id  # 查询到用户数据时，保存session的id到浏览器
                if remember:  # 如果用户点击了remember选择，在浏览器中进行数据持久化
                    session.permanent = True  # 数据持久化，默认31天，需要设置session_key在config.py中

                # 登录成功，跳转到后台首页
                return redirect(url_for('end.index'))  # 在蓝图中必须加cms   跳转到index方法
            else:
                return "账号或密码错误"  # 登录出错，返回结果
        else:
            print(login_form.errors)
            return "表单验证错误"
# 添加登录路由
mm_backend.add_url_rule("/login/", view_func=LoginView.as_view('login'))  # view_func 命名操作名字，"/login/"路由地址
# mm_backend.add_url_rule("/index/",)
