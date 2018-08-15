from flaskapp.__init__ import app
from flask import render_template, request
from flaskapp.model.models import Stu


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/get_list')
def get_list():

    #调用数据库获取数据（表格对象）
    userObj = Stu()
    #处理数据，获得表格内容
    users = userObj.get_list()
    print(users)

    return render_template('user.html', users=users)


@app.route('/add_user', methods=['POST', 'GET']) #此处的POST GET 必须大写
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        userage = request.form['userage']
        print("用户名测试点:" + username + userage)
        #调用数据库数据
        userObj = Stu()
        res = userObj.add_user(username, userage)

        if res:
            return render_template('ok.html')
        else:
            return render_template('error.html')
