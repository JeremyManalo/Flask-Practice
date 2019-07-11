#  Prashant Marathay
#  Flask Tutorial Video 3  https://www.youtube.com/watch?v=UIJKdCIEXUQ
#  Most everything is available in wt forms
#  Could go into main application file but better to break out
#  Write python class that will automatically be converted into html form in the template (1:55)

from flask_wtf import FlaskForm # imports to application
from wtforms import StringField, PasswordField, SubmitField, BooleanField # imports these classes
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm): # create a Registration Form class.  Below are the form fields
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])  # StringField must identify Username as the label so form.username.label takes you to the username.label in the form
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up') # SubmitField must allow Signup as its button Label.  Not sure yet where the action goes

    def validate_field(self, field):
        if True:
            raise ValidationError('Validation Message')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login In')
