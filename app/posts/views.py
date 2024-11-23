import json
import os
from flask import session, render_template, abort, flash, url_for, redirect
from . import post_bp
from .forms import PostForm
from .models import Post
from app import db

def load_posts():
    if os.path.exists('posts.json'):
        with open('posts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)

@post_bp.route('/add_post', methods=["GET","POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        is_active = form.is_active.data
        category = form.category.data
        date = form.publish_date.data
        author = session.get("user","annonym")

        post_new = Post(title=title, 
                        content=content, 
                        category=category,
                        is_active = is_active,
                        author=author,
                        date = date
                        )
        db.session.add(post_new)
        print("Post added to session")
        db.session.commit()
        print("Post committed")
        flash(f"Post {post_new.title} added succsessfully!", "success")
        return redirect(url_for(".get_posts"))
    return render_template("add_post.html", form=form)

@post_bp.route('/')
def get_posts():
    stmt= db.select(Post).order_by(Post.id)
    posts = db.session.scalars(stmt).all()
    return render_template("post.html", posts=posts)

@post_bp.route('/<int:id>') 
def get_detail_posts(id):
    stmt = db.select(Post).where(Post.id == id)
    post = db.session.scalar(stmt)
    if post is None:
        abort(404)
    return render_template("detail_post.html", post=post)
@post_bp.route('/<int:id>/delete_pos', methods=['POST'])
def deletPost(id):
    stmt = Post.query.get(id)
    db.session.delete(stmt)
    db.session.commit()
    flash(f"Post delet succsessfully!", "success")
    return redirect(url_for(".get_posts"))
@post_bp.route('/<int:id>/edit', methods=['GET','POST'])
def edit_post(id):
    post = db.get_or_404(Post, id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.is_active = form.is_active.data
        post.category = form.category.data
        post.date = form.publish_date.data
        db.session.commit()
        flash('Post updated succsessfully')
        return redirect(url_for(".get_posts"))
    return render_template("add_post.html", form=form, post=post)