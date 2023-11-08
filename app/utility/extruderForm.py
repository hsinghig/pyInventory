from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired, DataRequired

class ItemForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired("Input is required!")])
    price = DecimalField("Price")
    description = TextAreaField("Description")
    category= SelectField("Category", coerce=int)
    subcategory = SelectField("Subcategory", coerce=int)
    submit = SubmitField("Submit")