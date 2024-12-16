from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField,SelectMultipleField,TimeField,SelectField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, Regexp, ValidationError, Optional
from .models import Films

class CreatFilmForm(FlaskForm):
    film_name = StringField('FilmName',
                            validators=[DataRequired(),
                                        Length(min=3, max=20),
                                        Regexp('^[a-zA-Z0-9_\s]+$',message="")])
    duration = TimeField('Duration')
    film_tegs = SelectMultipleField("Tags", coerce=int)
    film_img = FileField('Film images', 
                         validators=[FileAllowed(['jpg', 'png'], 
                                                 'Images only!')])
    submit = SubmitField("Add Film")
    def validate_username(self, film_name):
        film = Films.query.filter_by(film_name=film_name.data).first()
        if film:
            raise ValidationError('This film name is already taken. Please choose a different one.')
class SearchForm(FlaskForm):
    serch = StringField("", validators=[Optional()])
    sort = SelectField(
        "Sort by",
        choices=[('name','Name'),('user_id', 'Post film by user'),('add_to_db','Date add'),('duration','duration')],
        default='name'
    )
    submit = SubmitField('submit')
