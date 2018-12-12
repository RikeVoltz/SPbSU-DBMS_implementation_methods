import json

import pymysql
from flask import Flask, render_template, request

import forms

app = Flask(__name__)
app.config.FROM_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = pymysql.connect("localhost", "root", "admin", "SPbSU_log_analysis_system")

cursor_dict = db.cursor(pymysql.cursors.DictCursor)
cursor_list = db.cursor()


@app.route('/users/get')
def get_users():
    cursor_dict.execute("SELECT * FROM User")
    users = cursor_dict.fetchall()
    return json.dumps(users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    request_data = request.get_json()
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        name = request.form['name']  or request_data['name']
        surname = request.form['surname'] or request_data['surname']
        email = request.form['email'] or request_data['email']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`User` (email, surname, name) VALUES "
            "('{0}', '{1}', '{2}')".format(email, surname, name))
    return render_template('add_user.html', form=form)


@app.route('/courses/get')
def get_courses():
    cursor_dict.execute("SELECT * FROM Course")
    courses = cursor_dict.fetchall()
    return json.dumps(courses)


@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    request_data = request.get_json()
    form = forms.CourseForm(request.form)
    cursor_list.execute("SELECT id, name, surname FROM `SPbSU_log_analysis_system`.`User`")
    users = list(cursor_list.fetchall())
    for i in range(len(users)):
        full_name = '{0} {1}'.format(users[i][1], users[i][2])
        users[i] = (users[i][0], full_name)
    form.user_id.choices = users
    if request.method == 'POST':
        title = request.form['name'] or request_data['name']
        russian_title = request.form['russian_title'] or request_data['russian_title']
        hash = request.form['hash'] or request_data['hash']
        user_id = request.form['user_id'] or request_data['user_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Course` (title, russian_title, hash, user_id) VALUES "
            "('{0}', '{1}', '{2}', {3})".format(title, russian_title, hash, user_id))
    return render_template('add_course.html', form=form)


@app.route('/logs/get')
def get_logs():
    cursor_dict.execute("SELECT * FROM Log")
    logs = cursor_dict.fetchall()
    return json.dumps(logs)


@app.route('/logs/add', methods=['GET', 'POST'])
def add_logs():
    request_data = request.get_json()
    form = forms.LogForm(request.form)
    cursor_list.execute("SELECT id, russian_title FROM `SPbSU_log_analysis_system`.`Course`")
    courses = cursor_list.fetchall()
    form.course_id.choices = courses
    if request.method == 'POST':
        load_date = request.form['load_date'] or request_data['load_date']
        course_id = request.form['course_id'] or request_data['course_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Log` (load_date, course_id) VALUES "
            "('{0}', '{1}')".format(load_date, course_id))
    return render_template('add_log.html', form=form)


@app.route('/modules/get')
def get_modules():
    cursor_dict.execute("SELECT * FROM Module")
    modules = cursor_dict.fetchall()
    return json.dumps(modules)


@app.route('/modules/add', methods=['GET', 'POST'])
def add_modules():
    request_data = request.get_json()
    form = forms.ModuleForm(request.form)
    cursor_list.execute("SELECT id, load_date FROM `SPbSU_log_analysis_system`.`Log`")
    logs = cursor_list.fetchall()
    form.log_id.choices = logs
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        hash = request.form['hash'] or request_data['hash']
        log_id = request.form['log_id'] or request_data['log_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Module` (number, hash, log_id) VALUES "
            "('{0}', '{1}', '{2}')".format(number, hash, log_id))
    return render_template('add_module.html', form=form)


@app.route('/lessons/get')
def get_lessons():
    cursor_dict.execute("SELECT * FROM Lesson")
    lessons = cursor_dict.fetchall()
    return json.dumps(lessons)


@app.route('/lessons/add', methods=['GET', 'POST'])
def add_lessons():
    request_data = request.get_json()
    form = forms.LessonForm(request.form)
    cursor_list.execute("SELECT id, number FROM `SPbSU_log_analysis_system`.`Module`")
    modules = cursor_list.fetchall()
    form.module_id.choices = modules
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        hash = request.form['hash'] or request_data['hash']
        link = request.form['link'] or request_data['link']
        module_id = request.form['module_id'] or request_data['module_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Lesson` (number, hash, link, module_id) VALUES "
            "('{0}', '{1}', '{2}', '{3}')".format(number, hash, link, module_id))
    return render_template('add_lesson.html', form=form)


@app.route('/tests/get')
def get_tests():
    cursor_dict.execute("SELECT * FROM Test")
    tests = cursor_dict.fetchall()
    return json.dumps(tests)


@app.route('/tests/add', methods=['GET', 'POST'])
def add_tests():
    request_data = request.get_json()
    form = forms.TestForm(request.form)
    cursor_list.execute("SELECT id, number FROM `SPbSU_log_analysis_system`.`Lesson`")
    lessons = cursor_list.fetchall()
    form.lesson_id.choices = lessons
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        hash = request.form['hash'] or request_data['hash']
        lesson_id = request.form['lesson_id'] or request_data['lesson_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Test` (number, hash, lesson_id) VALUES "
            "('{0}', '{1}', '{2}')".format(number, hash, lesson_id))
    return render_template('add_test.html', form=form)


@app.route('/videos/get')
def get_videos():
    cursor_dict.execute("SELECT * FROM Video")
    videos = cursor_dict.fetchall()
    return json.dumps(videos)


@app.route('/videos/add', methods=['GET', 'POST'])
def add_videos():
    request_data = request.get_json()
    form = forms.VideoForm(request.form)
    cursor_list.execute("SELECT id, number FROM `SPbSU_log_analysis_system`.`Lesson`")
    lessons = cursor_list.fetchall()
    form.lesson_id.choices = lessons
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        link = request.form['link'] or request_data['link']
        chart_link = request.form['chart_link'] or request_data['chart_link']
        materials_viewed = request.form['materials_viewed'] or request_data['materials_viewed']
        users_watched = request.form['users_watched'] or request_data['users_watched']
        is_most_viewed = request.form['is_most_viewed'] or request_data['is_most_viewed']
        lesson_id = request.form['lesson_id'] or request_data['lesson_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Video` (number, link, chart_link, materials_viewed,"
            " users_watched, is_most_viewed, lesson_id) VALUES "
            "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(number, link, chart_link, materials_viewed,
                                                                       users_watched, is_most_viewed, lesson_id))
    return render_template('add_video.html', form=form)


@app.route('/attempts/get')
def get_attempts():
    cursor_dict.execute("SELECT * FROM Attempt")
    attempts = cursor_dict.fetchall()
    return json.dumps(attempts)


@app.route('/attempts/add', methods=['GET', 'POST'])
def add_attempts():
    request_data = request.get_json()
    form = forms.AttemptForm(request.form)
    cursor_list.execute("SELECT id, number FROM `SPbSU_log_analysis_system`.`Test`")
    tests = cursor_list.fetchall()
    form.test_id.choices = tests
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        average_grade = request.form['average_grade'] or request_data['average_grade']
        median_grade = request.form['median_grade'] or request_data['median_grade']
        max_grade = request.form['max_grade'] or request_data['max_grade']
        number_of_solutions = request.form['number_of_solutions'] or request_data['number_of_solutions']
        test_id = request.form['test_id'] or request_data['test_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Attempt` (number, average_grade, median_grade, max_grade,"
            " number_of_solutions, test_id) VALUES "
            "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(number, average_grade, median_grade,
                                                                max_grade, number_of_solutions, test_id))
    return render_template('add_attempt.html', form=form)


@app.route('/questions/get')
def get_questions():
    cursor_dict.execute("SELECT * FROM Question")
    questions = cursor_dict.fetchall()
    return json.dumps(questions)


@app.route('/questions/add', methods=['GET', 'POST'])
def add_questions():
    request_data = request.get_json()
    form = forms.QuestionForm(request.form)
    cursor_list.execute("SELECT id, number, test_id FROM `SPbSU_log_analysis_system`.`Attempt`")
    attempts = list(cursor_list.fetchall())
    for i in range(len(attempts)):
        full_title = 'Attempt №{0}, Test id {1}'.format(attempts[i][1], attempts[i][2])
        attempts[i] = (attempts[i][0], full_title)
    form.attempt_id.choices = attempts
    if request.method == 'POST':
        number = request.form['number'] or request_data['number']
        right_answers_percent = request.form['right_answers_percent'] or request_data['right_answers_percent']
        attempt_id = request.form['attempt_id'] or request_data['attempt_id']
    if form.validate():
        cursor_dict.execute(
            "INSERT INTO `SPbSU_log_analysis_system`.`Question` (number, right_answers_percent, attempt_id) VALUES "
            "('{0}', '{1}', '{2}')".format(number, right_answers_percent, attempt_id))
    return render_template('add_question.html', form=form)


if __name__ == '__main__':
    app.run()
