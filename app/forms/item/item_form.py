from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length


class ItemForm(FlaskForm):
    class Meta:
        csrf = False

    itemname = StringField('itemname', validators=[DataRequired(), Length(min=2, max=255)])
    itemdescription = StringField('itemdescription', validators=[DataRequired()])
    itemstock = IntegerField('itemstock', validators=[DataRequired(), NumberRange(min=0)])
    itemprice = FloatField('itemprice', validators=[DataRequired(), NumberRange(min=0)])
