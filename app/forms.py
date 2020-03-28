from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    ingredients = FieldList(StringField('Ingredient:', validators=[DataRequired()]), min_entries=2)
    add_entry = SubmitField('Add Entry')
    remove_entry = SubmitField('Remove Entry')
    submit = SubmitField('Search')