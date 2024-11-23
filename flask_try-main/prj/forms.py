from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from wtforms.fields import StringField,PasswordField,EmailField,SubmitField,BooleanField
from prj.models import User
class regestrationfrom(FlaskForm):
    user_name=StringField('User Name',validators=[DataRequired(),Length(min=2,max=50)])
    Email=EmailField('Email',validators=[DataRequired(),Email()])
    pass_word=PasswordField('pass word',validators=[DataRequired()])
    confirm_pass=PasswordField('conifrm pass word',validators=[DataRequired(),EqualTo('pass_word')])
    submit=SubmitField('Sing Up')
    def validate_user_name(self,user_name):
        user=User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('this name already taken')


class loginfrom(FlaskForm):
    Email=EmailField('Email',validators=[DataRequired(),Email()])
    pass_word=PasswordField('pass word',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Log In')