from flask import Flask, request, redirect, url_for
app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route('/')
def main():
    return 'Hello, world'

@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return f"This is your homepage :) - {agent} "

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

if __name__ == '__main__':
    app.run(debug = True)