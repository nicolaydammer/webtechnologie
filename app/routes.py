from flask import render_template, request, redirect, url_for
from app import app, login_manager
from .Models import User
from .forms.LoginForm import LoginForm


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
        # inloggen
        return redirect("https://google.nl")

    return render_template(
        'base.html',
        title="Filmfan login pagina",
        page="login",
        form=loginform
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template(
            'base.html',
            title="Filmfan register pagina",
            page="register"
        )
    if request.method == 'POST':
        return 'hi'
