from flaskapp.model.configdb import db


class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    age = db.Column(db.String(16), nullable=False)

    def get_list(self):
        users = Stu.query.all()  #查询的所有用户，返回元组类型，元素为类
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

    def del_user(self, id):
        try:
            user = Stu.query.filter_by(id=id).first()
            print('测试获得user：')
            print(user)
            db.session.delete(user)
            db.session.commit()
            print('数据库测试点：成功')
            return True
        except Exception as e:
            return False
#修改部分错误
    def updata(self,newname, newage):
        try:
            user = Stu.query.filter_by(name=newname).r.update({'age': newage})
            print(user.name)

            db.session.commit()
            db.session.colose()
            print('修改成功')
            return True

        except Exception as e:
            return False