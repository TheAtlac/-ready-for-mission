# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index1.html', title='снова марс')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
