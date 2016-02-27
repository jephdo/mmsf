from flask.ext.wtf import Form

from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required


class KidsUploadForm(Form):
    csvstring = TextAreaField("Comma delimited string of students. "
                         "Fields  required =first, last, year, schoolname, phone, email", 
                         validators=[Required()])
    submit = SubmitField('Submit')