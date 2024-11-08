from flask import request, redirect, url_for,render_template,abort
from . import app

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/homepage') 
def home():
    agent = request.user_agent
    return render_template("home.html", agent=agent)

@app.route('/resume')
def resume():
    return render_template("resume.html")
@app.errorhandler(404)
def pege_not_found():
    return render_template("404.html"), 404
