from flask import Flask, render_template,url_for,flash,redirect
from forms import Inscription, Connexion
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SECRET_KEY']='8c05717605352b7265844efd591701ea'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' 
db=SQLAlchemy(app) 

class User(db.Model): 
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(30) ,nullable=False, default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='auteur',lazy=True) 

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')" 

class Post(db.Model): #creer premier model(table) User
    id=db.Column(db.Integer, primary_key=True)
    titre=db.Column(db.String(100),nullable=False)
    date_poste=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    contenu=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) 

    def __repr__(self):
        return f"Post('{self.titre}','{self.date_poste}')"

@app.route('/')
@app.route('/home') 
def home():  
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/inscription',methods=['GET','POST']) 
def inscription():
    form=Inscription() 
    if form.validate_on_submit(): 
        flash(f'le Compte {form.username.data} creer avec Succees','success')                                                                              
        return redirect(url_for('connexion'))

    return render_template('inscription.html',title='inscription',form=form) 

@app.route('/connexion',methods=['GET','POST'])
def connexion():
    form=Connexion()
    if form.validate_on_submit(): 
        if form.email.data=="yassinetaiki01@gmail.com" and form.password.data=="1234":
            flash(f'vous etes connectee {form.email.data}',"success") 
            return redirect(url_for('home')) 
        else:
            flash("nom d'utilisateur ou mot de passe incorrecte",'danger')  
    return render_template('connexion.html',title='connexion',form=form)


if __name__=='__main__':
    app.run(debug=True) 