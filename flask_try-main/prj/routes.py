from flask import render_template ,url_for,redirect,flash
from prj.forms import regestrationfrom,loginfrom 
from prj import app,bcrypt,db
from prj.models import User


postes=[
{
    'name':'mohamed',
    'fname':'rebbouh',
    'age':'20'
},
]
@app.route('/')
def home():
    return render_template('home.html',posts=postes)

@app.route('/about')
def second():
    return render_template('2nd.html',title="about")

@app.route('/register',methods=['GET','POST'])
def register():
    form=regestrationfrom()
    if form.validate_on_submit():
        hash_pass=bcrypt.generate_password_hash(form.pass_word.data).decode("utf-8")
        user=User(user_name=form.user_name.data,email=form.Email.data,pass_word=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created Succefully  {form.user_name.data}!!','success')
        return redirect(url_for('login'))
      
    return render_template('regestration.html',title='registration',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=loginfrom()
    if form.validate_on_submit():
        return  
    return render_template('login.html',title='login',form=form)
@app.route('/try')
def try_test():
    return '<h1>mohamed<h1>'
