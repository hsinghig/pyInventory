from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError
class extruderForm(FlaskForm):
    location = StringField("Location")
    color = StringField("Color")
    user = StringField("User")
    width = StringField("Width")
    submit = SubmitField("Submit")