from flask import render_template,  url_for, redirect,current_app,request
from flask import flash
from . import films_bp
from app import db
from .form import CreatFilmForm, SearchForm
from .models import Films,FilmTags
from app.user.models import User
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os


@films_bp.route("/", methods=['GET'])
def get_all_films():
    form = SearchForm(request.args)
    query = Films.query
    if form.serch.data:
        query = query.filter(Films.name.ilike(f"%{form.serch.data}%"))
    if form.sort.data == 'add_to_db':
        query = query.filter(Films.add_to_db.ilike(f"%{form.serch.data}%")).order_by(Films.id.desc())
    elif form.sort.data == 'user_id':
        stmt = db.select(User).where(User.username == form.serch.data)
        user = db.session.scalar(stmt)
        if user:
            query = query.filter(Films.user_id == user.id).order_by(Films.id.desc())
        else:
            flash('User not found, showing all films.', 'error')
            query = query.order_by(Films.id.desc())
    elif  form.sort.data == 'duration':
            print(f"Found user: {user.username}")
            query = query.filter(Films.add_to_db == form.serch.data).order_by(Films.id.desc())
    else:
        query = query.order_by(Films.name.asc())
    films = query.all()
    print(f"query={query}")
    print(f"films={films}")
    return render_template('all_films.html', films=films, form=form)

@films_bp.route("/<int:id>")
def get_film(id):
    stmt = db.select(Films).where(Films.id == id)
    film =db.session.scalar(stmt)
    return render_template("film_info.html",film=film)

@films_bp.route("/create-films", methods=["GET","POST"])
@login_required
def creat_films():
    form = CreatFilmForm()
    form.film_tegs.choices = [(tag.id, tag.name) for tag in FilmTags.query.all()]
    if form.validate_on_submit():
        user = current_user
        film_new = Films(
            name = form.film_name.data,
            user_id = user.id,
            duration = form.duration.data,
        )
        if form.film_img.data:
            print(f"{form.film_img.data}")
            picture_file = save_picture(form.film_img.data)
            film_new.img_file = picture_file

        for tag_id in form.film_tegs.data:
            tag = FilmTags.query.get(tag_id)
            film_new.film_tags.append(tag)
            db.session.add(film_new)
            db.session.commit()
        flash('Film created.', 'succes')
        return redirect(url_for(".get_all_films"))
    return render_template("creat_films.html",form=form)

@films_bp.route('/<int:id>/delet_film', methods=["POST"])
def delet_film(id):
    stmt = db.select(Films).where(Films.id == id)
    film = db.session.scalar(stmt)
    if film:
        film.film_tags.clear() 
        db.session.delete(film)
        db.session.commit()
        print(f"Film with id {id} deleted successfully.")
        flash('Film successful delaet.', 'success')
        return redirect(url_for(".get_all_films"))
    
@films_bp.route('/<int:id>/update_film', methods=["get","post"])
def update_film(id):
    film = db.get_or_404(Films, id)
    form = CreatFilmForm(obj=film)
    form.film_tegs.choices = [(tag.id, tag.name) for tag in FilmTags.query.all()]
    if form.validate_on_submit():
        film.name = form.film_name.data
        film.duration = form.duration.data
        if form.film_img.data:
            print(f"{form.film_img.data}")
            picture_file = save_picture(form.film_img.data)
            film.img_file = picture_file
        film.film_tags = []
        for tags_id in form.film_tegs.data:
            tag = FilmTags.query.get(tags_id)
            if tag:
                film.film_tags.append(tag)
        db.session.commit()
        flash('Film successful update.', 'success')
        return redirect(url_for(".get_film", id=film.id))
    return render_template("creat_films.html", form=form, film=film)

def save_picture(form_picture):
    filename = secure_filename(form_picture.filename)
    picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    os.makedirs(os.path.dirname(picture_path), exist_ok=True)
    form_picture.save(picture_path)
    return filename
