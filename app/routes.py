from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user

from app import app, login_manager, db
from .Models.Acteur import Acteur
from .Models.Comment import Comment
from .Models.Film import Film
from .Models.Regisseur import Regisseur
from .Models.User import User
from .forms.CommentForm import CommentForm
from .forms.CreateActeur import CreateActeur
from .forms.CreateRegisseur import CreateRegisseur
from .forms.CreateFilm import CreateFilm
from .forms.FilmForm import FilmForm
from .forms.LoginForm import LoginForm
from .forms.ModifyActeur import ModifyActeur
from .forms.ModifyRegisseur import ModifyRegisseur
from .forms.RegisterForm import RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    films = Film.query.all()
    cards = [(film.id, film.titel, '06-05-2022', Regisseur.query.filter_by(id=film.regisseur).first(),
              Acteur.query.filter_by(id=film.acteur).first(), film.beschrijving) for film in films]
    return render_template(
        'base.html',
        title="Filmfan homepage",
        page="home.html",
        cards=cards
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is not None and user.verify_password(request.form.get('password')):
            login_user(user)
            return redirect(url_for('home'))

        return redirect(url_for('login'))

    return render_template(
        'base.html',
        title="Filmfan login pagina",
        page="login.html",
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
        page="register.html",
        form=registerform
    )


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return "Success"


@app.route('/film', methods=['GET', 'POST'])
@login_required
def create_film():
    create_film_form = CreateFilm()
    form = request.form

    if create_film_form.validate_on_submit():
        film = Film(form.get('titel'), form.get('regisseur'), form.get('acteur'), form.get('beschrijving'))
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        title="Filmfan film toevoegen",
        page="film_aanmaken.html",
        form=create_film_form
    )


@app.route('/film/<film_id>', methods=['GET', 'POST'])
def film(film_id):
    form = request.form
    film_form = FilmForm()
    film = Film.query.filter_by(id=film_id).first()
    comment_form = CommentForm()
    comments = Comment.query.filter_by(film=film_id).all()

    comment_list = [(comment.id, comment.comment, User.query.filter_by(id=comment.user).first().username,
                     int(User.query.filter_by(id=comment.user).first().id)) for comment in comments]

    if film_form.validate_on_submit() and current_user.is_authenticated:
        film.titel = form.get('titel')
        film.beschrijving = form.get('beschrijving')
        film.acteur = form.get('acteur')
        film.regisseur = form.get('regisseur')

        db.session.add(film)
        db.session.commit()
        return redirect(url_for('home'))

    if comment_form.validate_on_submit() and current_user.is_authenticated:
        comment = Comment(form.get('comment'), current_user.get_id(), film_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('film', film_id=film_id))

    film_form.titel.data = film.titel
    film_form.beschrijving.data = film.beschrijving
    film_form.regisseur.data = film.regisseur
    film_form.acteur.data = film.acteur

    return render_template(
        'base.html',
        title=film.titel,
        page="film.html",
        form=film_form,
        comment_form=comment_form,
        comment_list=comment_list
    )


@app.route('/film/<film_id>', methods=['DELETE'])
@login_required
def modify_film(film_id):
    film = Film.query.get(film_id)
    db.session.delete(film)
    db.session.commit()
    return "succes"


@app.route('/acteur', methods=['GET', 'POST'])
@login_required
def create_acteur():
    create_acteur_form = CreateActeur()
    form = request.form

    if create_acteur_form.validate_on_submit():
        voornaam = form.get('voornaam')
        achternaam = form.get('achternaam')

        acteur = Acteur(voornaam, achternaam)

        db.session.add(acteur)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        title="Filmfan acteur toevoegen",
        page="acteur_aanmaken.html",
        form=create_acteur_form
    )


@app.route('/regisseur', methods=['GET', 'POST'])
@login_required
def create_regisseur():
    create_regisseur_form = CreateRegisseur()
    form = request.form

    if create_regisseur_form.validate_on_submit():
        voornaam = form.get('voornaam')
        achternaam = form.get('achternaam')

        regisseur = Regisseur(voornaam, achternaam)

        db.session.add(regisseur)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        title="Filmfan regisseur toevoegen",
        page="regisseur_aanmaken.html",
        form=create_regisseur_form
    )


@app.route('/regisseur/<regisseur_id>', methods=['GET', 'POST'])
def regisseur(regisseur_id):
    form = request.form
    regisseur = Regisseur.query.filter_by(id=regisseur_id).first()
    modify_regisseur_form = ModifyRegisseur()

    if modify_regisseur_form.validate_on_submit():
        regisseur.voornaam = form.get('voornaam')
        regisseur.achternaam = form.get('achternaam')
        db.session.add(regisseur)
        db.session.commit()
        return redirect(url_for('regisseurs'))

    modify_regisseur_form.voornaam.data = regisseur.voornaam
    modify_regisseur_form.achternaam.data = regisseur.achternaam
    return render_template(
        'base.html',
        title="Filmfan regisseur bewerken",  # add film title
        page="regisseur_bewerken.html",
        form=modify_regisseur_form
    )


@app.route('/acteur/<acteur_id>', methods=['GET', 'POST'])
def acteur(acteur_id):
    form = request.form
    acteur = Acteur.query.filter_by(id=acteur_id).first()
    modify_acteur_form = ModifyActeur()

    if modify_acteur_form.validate_on_submit():
        acteur.voornaam = form.get('voornaam')
        acteur.achternaam = form.get('achternaam')
        db.session.add(acteur)
        db.session.commit()
        return redirect(url_for('acteurs'))

    modify_acteur_form.voornaam.data = acteur.voornaam
    modify_acteur_form.achternaam.data = acteur.achternaam
    return render_template(
        'base.html',
        title="Filmfan acteur bewerken",  # add film title
        page="acteur_bewerken.html",
        form=modify_acteur_form
    )


@app.route('/acteurs', methods=['GET'])
@login_required
def acteurs():
    acteurs = Acteur.query.all()
    return render_template(
        'base.html',
        title="Filmfan acteurs lijst",
        page="acteurs.html",
        acteurs=acteurs
    )


@app.route('/regisseurs', methods=['GET'])
@login_required
def regisseurs():
    regisseurs = Regisseur.query.all()
    return render_template(
        'base.html',
        title="Filmfan regisseurs lijst",
        page="regisseurs.html",
        regisseurs=regisseurs
    )


@app.route('/acteur/<acteur_id>', methods=['DELETE'])
@login_required
def delete_acteur(acteur_id):
    acteur = Acteur.query.get(acteur_id)
    db.session.delete(acteur)
    db.session.commit()
    return "succes"


@app.route('/regisseur/<regisseur_id>', methods=['DELETE'])
@login_required
def delete_regisseur(regisseur_id):
    regisseur = Regisseur.query.get(regisseur_id)
    db.session.delete(regisseur)
    db.session.commit()
    return "succes"


@app.route('/comment/<comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if current_user.id == comment.user:
        db.session.delete(comment)
        db.session.commit()
        return "succes"
    return "false"
