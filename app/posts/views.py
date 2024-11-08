import json
import os
from flask import session, render_template, abort, flash, url_for, redirect
from . import post_bp
from .forms import PostForm

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
        posts = load_posts()
        new_post ={
            "id": len(posts)+1,
            "title": form.title.data,
            "content": form.content.data,
            "date": form.publish_date.data,
            "author": session.get("user","annonym")
        }
        posts.append(new_post)
        save_posts(posts)
        flash(f"Post {new_post['title']} added succsessfully!", "success")
        return redirect(url_for(".get_posts"))
    return render_template("add_post.html", form=form)

@post_bp.route('/')
def get_posts():
    posts = load_posts()
    return render_template("post.html", posts=posts)

@post_bp.route('/<int:id>') 
def get_detail_posts(id):
    posts = load_posts()
    post = posts[id-1]
    if id > len(posts):
        abort(404)
    return render_template("detail_post.html", post=post)