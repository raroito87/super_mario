from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired

class GridInputForm(Form):
    grid = StringField('Grid')
    n = StringField('N')
    submit = StringField('')

