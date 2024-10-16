from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/homepage') 
def home():
    agent = request.user_agent
    return render_template("home.html", agent=agent)

@app.route('/hi/<string:name>') 
def hi_someone(name):
    age = request.args.get("age", None, type=int)
    name = name.upper()
    return f"Welcome {name=} {age=}"

@app.route('/admin') 
def admin():
    to_url = url_for("hi_someone",name = "administrator", _external=True)
    print(to_url)
    return redirect(to_url)

@app.route('/about') 
def about():
    return render_template('about.html', company_name='Test')

if __name__ == '__main__':
    app.run(debug = True)