#这是单独的实验
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    age = db.Column(db.Integer, nullable=False)


if __name__ == '__main__':
    users = Stu.query.all()
    for user in users:
        print(str(user.id) + user.name + str(user.age))

