from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class BasketAddItemForm(FlaskForm):
    class Meta:
        csrf = False

    itemid = IntegerField('itemid', validators=[DataRequired()])
    itemquantity = IntegerField('itemquantity', validators=[DataRequired()])
