from wtforms import Form, StringField

class GridInputForm(Form):
    grid = StringField('Grid')
    n = StringField('N')
    submit = StringField('')

