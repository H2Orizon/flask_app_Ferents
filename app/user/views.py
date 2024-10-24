from flask import request, redirect, url_for,render_template
from . import user_bp

@user_bp.route('/<string:name>') 
def hi(name):
    age = request.args.get("age", None, type=int)
    return render_template("user/hi.html", name=name, age=age)

@user_bp.route('/admin')
def admin():
    to_url = url_for("user.hi",name="administrator", age=19, _external=True)
    print(to_url)
    return redirect(to_url)