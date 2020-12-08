# -*- encoding: utf-8 -*-
"""
@File    : app.py
@Time    : 2020/11/19 
@Author  : xia

"""
# 项目主文件，启动入口

# 前台  front    管理前端界面的逻辑
# 后台  end      管理后端的操作
# 公有的文件 common

from flask import Flask
import config      # 配置文件库
from exts import db    # 第三方库导入db
from end.views import mm_backend          # 导入后端蓝图文件
from front.views import front_bp      # 导入前端蓝图文件


app = Flask(__name__)
app.config.from_object(config)        # 添加配置

db.init_app(app)                      # 绑定app

app.register_blueprint(mm_backend)        # 后端蓝图文件注册
app.register_blueprint(front_bp)        # 前端蓝图文件注册


if __name__ == '__main__':
    app.run(debug=True, port=9999)