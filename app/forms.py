from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired , Length, Email, EqualTo

class Inscription(FlaskForm): #creer formulaire inscription
    username=StringField('Nom utilisateur',
                         validators=[DataRequired(),Length(min=2,max=50)])

    email=StringField('email',
                      validators=[DataRequired(),Email()])

    password=PasswordField('Mot de passe',
                           validators=[DataRequired()])

    confirm_password=PasswordField('Confirmer_Mot de passe',
                           validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField("S'inscrire")


class Connexion(FlaskForm): #formulaire connexion

    email=StringField('Email',
                      validators=[DataRequired(),Email()])

    password=PasswordField('Mot de passe',
                           validators=[DataRequired()])

    remember=BooleanField("S'enregister")

    submit=SubmitField('Se conneter')
