from flaskapp.model.configdb import db


class Stu(db.Model):
    __tablename__ = 'stu'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    age = db.Column(db.Integer, nullable=False)

    def get_list():
        users = Stu.query.all()
        return users



