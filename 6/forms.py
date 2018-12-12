from wtforms import Form, validators, StringField, DateField, SelectField, IntegerField, FloatField, BooleanField


class UserForm(Form):
    name = StringField('Name:', validators=[validators.required()])
    surname = StringField('Surname:', validators=[validators.required()])
    email = StringField('Email:', validators=[validators.required()])


class CourseForm(Form):
    title = StringField('Title:', validators=[validators.required()])
    russian_title = StringField('Russian title:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    user_id = SelectField('User', coerce=int, validators=[validators.required()])


class LogForm(Form):
    load_date = DateField('Load date:', validators=[validators.required()])
    course_id = SelectField("Course", coerce=int, validators=[validators.required()])


class ModuleForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    log_id = SelectField("Log", coerce=int, validators=[validators.required()])


class LessonForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    link = StringField('Link:', validators=[validators.required()])
    module_id = SelectField("Module", coerce=int, validators=[validators.required()])


class TestForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    hash = StringField('Hash:', validators=[validators.required()])
    lesson_id = SelectField("Lesson", coerce=int, validators=[validators.required()])


class VideoForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    chart_link = StringField('Chart link:', validators=[validators.required()])
    materials_viewed = FloatField('Materials viewed:', validators=[validators.required()])
    users_watched = FloatField("Users watched:", validators=[validators.required()])
    is_most_viewed = BooleanField("Is most viewed:", validators=[validators.required()])
    link = StringField('Link:', validators=[validators.required()])
    lesson_id = SelectField("Lesson", coerce=int, validators=[validators.required()])


class AttemptForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    average_grade = FloatField('Average grade:', validators=[validators.required()])
    median_grade = FloatField('Median grade:', validators=[validators.required()])
    max_grade = FloatField('Max grade:', validators=[validators.required()])
    number_of_solutions = IntegerField('Number of solutions:', validators=[validators.required()])
    test_id = SelectField("Test", coerce=int, validators=[validators.required()])


class QuestionForm(Form):
    number = IntegerField('Number:', validators=[validators.required()])
    right_answers_percent = FloatField("Right answers percent:", validators=[validators.required()])
    attempt_id = SelectField("Attempt", coerce=int, validators=[validators.required()])
