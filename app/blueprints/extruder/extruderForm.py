from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ExtruderForm(FlaskForm):
    locationID = SelectField("Location", validators=[DataRequired()])
    colorID = SelectField("Color", validators=[DataRequired()])
    widthID = SelectField("Width", validators=[DataRequired()])
    length = StringField("Length", validators=[DataRequired(), Length(min=1, max=10)])
    weight = StringField("Weight")
    comment = TextAreaField("Comment")
    users = SelectField("Submitted By", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def __repr__(self) -> str:
        return '<ExtruderForm {}>'.format(self.locationID)
    
class ExtruderFilterForm(FlaskForm):
    colorFilterForm = SelectMultipleField("Color")
    widthFilterForm = SelectMultipleField("Width")
    submit = SubmitField("Submit")