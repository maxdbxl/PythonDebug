from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, EqualTo


class UserRegisterForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('username', validators=[DataRequired()])
    userpassword = StringField('userpassword', validators=[DataRequired(), EqualTo('confirm', message='passwords must match!')])
    confirm = StringField('confirm', validators=[DataRequired()])
    useremail = StringField('useremail', validators=[DataRequired()])
    userdescription = StringField('userdescription', validators=[DataRequired()])
