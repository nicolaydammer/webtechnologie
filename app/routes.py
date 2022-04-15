from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template


@app.route('/login')
def login():
    return render_template(
        'base.html',
        title="Filmfan login pagina",
        page="login"
    )

@app.route('/register')
def register():
    return render_template(
        'base.html',
        title="Filmfan register pagina",
        page="register"
    )