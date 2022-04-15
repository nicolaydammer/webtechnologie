from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template(
        'base.html',
        title="Filmfan login pagina",
        page="home",
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
