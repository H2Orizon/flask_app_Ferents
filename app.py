from flask import Flask, request
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)