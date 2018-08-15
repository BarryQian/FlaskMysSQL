from flaskapp.model.configdb import db


class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    age = db.Column(db.String(16), nullable=False)

    def get_list(self):
        users = Stu.query.all()
        return users

    def add_user(self, username, userage):
        try:
            db.session.add(Stu(name=username, age=userage))
            db.session.commit()
            print('写入数据库测试点：成功')
            return True
        except Exception as e:
            print('写入数据库测试点：失败')
            return False



