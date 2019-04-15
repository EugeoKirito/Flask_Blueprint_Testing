#coding='utf-8'

from flask import Flask, request, jsonify
from flask_sqlalchemy   import SQLAlchemy

app=Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/FlaskTest'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY='asdasdasdasdasfafa'


app.config.from_object(Config)

db = SQLAlchemy(app)  # 先设置app的config 再传app


class Author(db.Model):
    __tablename__ = 'tbl_anthors'

    id = db.Column(db.Integer, primary_key=True, unique=True)

    name = db.Column(db.String(64), unique=True)



db.create_all()
# author=Author(name='wiki')
# db.session.add(author)
# db.session.commit()

@app.route('/login',methods=['POST'])
def login():


    user_name=request.form.get('user_name')
    password=request.form.get('password')

    if not all([user_name,password]):
        resp={
            'code':1,
            'message':'invail params'
        }
        return jsonify(resp)
    if  user_name=='admin' and password=='yeye':
        resp={
            'code':'OK',
            'message':'login success'


        }
        return jsonify(resp)
    else:
        resp={
            'code':2,
            'message':'Error Password Or UserName'
        }
        return jsonify(resp)









