from flask import Flask
import pymysql
import json
from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField, DateField, SelectField, IntegerField, FloatField, BooleanField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = pymysql.connect("localhost", "root", "", "SPbSU_log_analysis_system")

cursor = db.cursor(pymysql.cursors.DictCursor)

cursor.execute("SELECT VERSION()")

data = cursor.fetchall()


class UserForm(Form):
    name = StringField('Name:', validators=[validators.required()])
    surname = StringField('Surname:', validators=[validators.required()])
    email = StringField('Email:', validators=[validators.required()])


class CourseForm(Form):
    title = StringField('Title:', validators=[validators.required()])
    russian_title = StringField('Russian title:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    user_id = SelectField('User', validators=[validators.required()])


class LogForm(Form):
    load_date = DateField('Load date:', validators=[validators.required()])
    course_id = SelectField("Course", validators=[validators.required()])


class ModuleForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    log_id = SelectField("Log", validators=[validators.required()])


class LessonForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    link = StringField('Link:', validators=[validators.required()])
    module_id = SelectField("Module", validators=[validators.required()])


class TestForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    lesson_id = SelectField("Lesson", validators=[validators.required()])


class VideoForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    chart_link = StringField('Chart link:', validators=[validators.required()])
    materials_viewed = FloatField('Materials viewed:', validators=[validators.required()])
    users_watched = FloatField("Users watched:", validators=[validators.required()])
    is_most_viewed = BooleanField("Is most viewed:", validators=[validators.required()])
    link = StringField('Link:', validators=[validators.required()])
    lesson_id = SelectField("Lesson", validators=[validators.required()])


class AttemptForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    average_grade = FloatField('Average grade:', validators=[validators.required()])
    median_grade = FloatField('Median grade:', validators=[validators.required()])
    max_grade = FloatField('Max grade:', validators=[validators.required()])
    number_of_solutions = IntegerField('Number of solutions:', validators=[validators.required()])
    test_id = SelectField("Lesson", validators=[validators.required()])


class QuestionForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    right_answers_percent = FloatField("Right answers percent:", validators=[validators.required()])
    attempt_id = SelectField("Attempt", validators=[validators.required()])


@app.route('/users/get')
def get_users():
    cursor.execute("SELECT * from User")
    users = cursor.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)


@app.route('/courses/get')
def get_courses():
    cursor.execute("SELECT * from Course")
    courses = cursor.fetchall()
    return json.dumps(courses)


@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    form = CourseForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        title = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)


@app.route('/users/get')
def get_users():
    cursor.execute("SELECT * from User")
    users = cursor.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)


@app.route('/users/get')
def get_users():
    cursor.execute("SELECT * from User")
    users = cursor.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)


@app.route('/users/get')
def get_users():
    cursor.execute("SELECT * from User")
    users = cursor.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)


@app.route('/users/get')
def get_users():
    cursor.execute("SELECT * from User")
    users = cursor.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
    if form.validate():
        cursor.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
        return get_users()
    return render_template('add_user.html', form=form)

if __name__ == '__main__':
    app.run()
