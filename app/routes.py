from flask import render_template, request
from app import app, login_manager
from .Models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
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
    if request.method == 'GET':
        return render_template(
            'base.html',
            title="Filmfan login pagina",
            page="login"
        )
    if request.method == 'POST':
        return 'hi'


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
