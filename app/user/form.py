from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from flask_wtf.file import FileAllowed
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), 
                                       Length(min=3, max=20),
                                       Regexp('^[a-zA-Z0-9_]+$', message="Username must contain only letters, numbers, or underscores.")])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered. Please choose a different one.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken. Please choose a different one.')
        

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    username = StringField('Username',
                            validators=[DataRequired(), 
                                       Length(min=3, max=20),
                                       Regexp('^[a-zA-Z0-9_]+$', message="Username must contain only letters, numbers, or underscores.")]
                            )
    img_file = FileField('Update Profile Picture', 
                         validators=[FileAllowed(['jpg', 'png'], 
                                                 'Images only!')])
    about_me = TextAreaField('About me',render_kw={"rows":5, "cols":5})
    submit = SubmitField('Update')
    
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', message="Passwords must match.")])
    submit = SubmitField('Update')