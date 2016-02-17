from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, login_manager, db
from forms import LoginForm, SignupForm
from models import User


@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Check if user is not already logged in'''
    if g.user is not None and g.user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        '''Check if user already exists'''
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('User already exists')
            return render_template('signup.html',
                                   form=form)
        '''Create a new user'''
        newUser = User(form.username.data, form.password.data)
        db.session.add(newUser)
        db.session.commit()
        flash('User added. You can now login')
        return redirect(url_for('login'))
    return render_template('signup.html',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Check if user is not already logged in'''
    if g.user is not None and g.user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        '''Check if user exists'''
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('User does not exist')
            return render_template('login.html',
                                   form=form)
        login_user(user)
        flash('Logged in successfully.')
        return redirect('/')
    return render_template('login.html',
                           form=form)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login'))
