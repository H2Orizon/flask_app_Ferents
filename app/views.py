from flask import request, redirect, url_for,render_template,abort,current_app
# from . import app

@current_app.route('/')
def main():
    return render_template("main.html")

@current_app.route('/homepage') 
def home():
    agent = request.user_agent
    return render_template("home.html", agent=agent)

@current_app.route('/resume')
def resume():
    return render_template("resume.html")

@current_app.errorhandler(404)
def pege_not_found(error):
    return render_template("404.html"), 404
