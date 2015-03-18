from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__, static_url_path='')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'


class Student(db.Model):
    id = Column(Integer, primary_key=True)
    student_id = Column(Text, unique=True)
    student_name = Column(Text)
    student_standard = Column(Text)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Student, methods=['GET', 'POST'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

app.debug = True

if __name__ == '__main__':
    app.run()
