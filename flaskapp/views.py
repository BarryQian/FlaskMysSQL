from flaskapp.__init__ import app
from flask import render_template
from flaskapp.model.models import Stu


@app.route('/')
def hello_world():
    return 'Hello aa '


@app.route('/get_list')
def get_list():

    #获取数据
    users = Stu.get_list( )
    print(users)

    return render_template('user.html', users=users)

