from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template(
        'base.html',
        title="Filmfan homepage",
        page="home",
        cards=[
            {
                'id': '12',
                'date': '15-4-2022'
            },
            {
                'id': '15',
                'date': '16-4-2022'
            },
            {
                'id': '18',
                'date': '17-4-2022'
            },
            {
                'id': '21',
                'date': '18-4-2022'
            },
            {
                'id': '24',
                'date': '19-4-2022'
            },
        ]
    )


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
