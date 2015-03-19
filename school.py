import os
from flask import Flask
from flask import Response
from flask import request
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from weasyprint import HTML
from jinja2 import Template


app = Flask(__name__, static_url_path='')
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['TEMPLATE_DIR'] = os.path.join(app.root_path, 'templates')


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


@app.route('/generatepdf')
def generate_pdf():
    templateurl = os.path.join(app.config['TEMPLATE_DIR'], 'pdftemplate.html')

    standard = request.args.get('student_standard')

    context = {
        'object_list': Student.query.filter_by(student_standard=standard).all() if standard else Student.query.all()
    }

    with open(templateurl, 'r') as file:
        template = Template(file.read())

    html_data = template.render(context)
    pdf_data = HTML(string=html_data.encode('utf-8'),
                    encoding='utf-8', base_url=os.path.join(app.root_path, 'static')).write_pdf()
    return Response(pdf_data,content_type="application/pdf")

app.debug = True

if __name__ == '__main__':
    app.run()
