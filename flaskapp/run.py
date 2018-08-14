#本项目在__init__.py中实例化Flask和Bootstrap
#浏览器路由请求，执行相应路由(views.py)，如localhost:5000/get_list
#get_list()函数获取数据库数据
#configdb.py设置数据库连接，并实例化一个数据库对象：db
#models.py 实例化mysql数据库中test数据库的Stu表，并返回表内容：users到路由函数get_list()中
#通过render_templates()渲染user.html
#user.html是基于Bootstrap框架下的base.html模板


from flaskapp.__init__ import app


if __name__ == '__main__':
    app.run()
