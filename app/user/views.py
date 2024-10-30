from flask import request, redirect, url_for,render_template, make_response
from . import user_bp
from datetime import timedelta, datetime

@user_bp.route('/<string:name>') 
def hi(name):
    age = request.args.get("age", None, type=int)
    return render_template("user/hi.html", name=name, age=age)

@user_bp.route('/admin')
def admin():
    to_url = url_for("user.hi",name="administrator", age=19, _external=True)
    print(to_url)
    return redirect(to_url)

@user_bp.route('/set_cookie')
def set_cookie():
    response = make_response('Кука')
    #response.set_cookie('user','student',expire=datetime.now()+timedelta(seconds=10))
    response.set_cookie('user','student',max_age=timedelta(seconds=10))
    return response
@user_bp.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('user')
    return f'Користувач: {username}'
@user_bp.route('/delete_cookie')
def delete_cookie():
    response =make_response('del')
    response.set_cookie('user','',max_age=0)
    return response