from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user

from app import app, login_manager, db
from .Models.User import User
from .forms.LoginForm import LoginForm
from .forms.RegisterForm import RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template(
        'base.html',
        title="Filmfan homepage",
        page="home",
        cards=[
            {
                'id': '1',
                'date': '15-4-2022',
                'title': 'film1'
            },
            {
                'id': '2',
                'date': '16-4-2022',
                'title': 'film2'
            },
            {
                'id': '3',
                'date': '17-4-2022',
                'title': 'film3'
            },
            {
                'id': '4',
                'date': '18-4-2022',
                'title': 'film4'
            },
            {
                'id': '5',
                'date': '19-4-2022',
                'title': 'film5'
            },
        ]
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is not None and user.verify_password(request.form.get('password')):
            login_user(user)
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        title="Filmfan login pagina",
        page="login",
        form=loginform
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(email, username, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        title="Filmfan register pagina",
        page="register",
        form=registerform
    )


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
