from flask import Flask, request, redirect, url_for, render_template,abort
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
def hi(name):
    age = request.args.get("age", None, type=int)
    return render_template("hi.html", name=name, age=age)

@app.route('/admin') 
def admin():
    to_url = url_for("hi",name = "administrator", _external=True)
    print(to_url)
    return redirect(to_url)

posts = [
    {"id": 1, 'title': 'My First Post', 'content': 'This is the content of my first post.', 'author': 'John Doe'},
    {"id": 2, 'title': 'Another Day', 'content': 'Today I learned about Flask macros.', 'author': 'Jane Smith'},
    {"id": 3, 'title': 'Flask and Jinja2', 'content': 'Jinja2 is powerful for templating.', 'author': 'Mike Lee'}
]

@app.route('/posts') 
def get_posts():
    return render_template("post.html", posts=posts)

@app.route('/post/<int:id>') 
def get_detail_posts(id):
    post = posts[id-1]
    if id > 3:
        abort(404)
    return render_template("detail_post.html", post=post)


if __name__ == '__main__':
    app.run(debug = True)