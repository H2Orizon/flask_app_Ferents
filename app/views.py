from flask import request, redirect, url_for,render_template,abort
from . import app

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/homepage') 
def home():
    agent = request.user_agent
    return render_template("home.html", agent=agent)

@app.route('/hi/<string:name>') 
def hi(name):
    age = request.args.get("age", None, type=int)
    return render_template("hi.html", name=name, age=age)

@app.route('/admin') 
def admin():
    to_url = url_for("hi",name = "administrator", _external=True)
    print(to_url)
    return redirect(to_url)

@app.route('/resume')
def resume():
    return render_template("resume.html")
