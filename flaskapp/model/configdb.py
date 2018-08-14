
from flask_sqlalchemy import SQLAlchemy
from flaskapp.__init__ import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

