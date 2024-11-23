from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired, Length

CATEGORIES = [("tech","Tech"),("science","Science"),("lifestyle","Lifestyly")]

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(),Length(min=2,)])
    content = TextAreaField("Content", validators=[DataRequired()],render_kw={"rows":5, "cols":5})
    is_active = BooleanField('Active Post')
    publish_date = DateTimeLocalField('Publish Date',validators=[DataRequired()],format='%Y-%m-%dT%H:%M',default=datetime.now())
    category = SelectField("Category",validators=[DataRequired()],choices=CATEGORIES)
    submit = SubmitField("Add Post")