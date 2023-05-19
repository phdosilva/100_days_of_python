from flask import Flask

app = Flask(__name__)

def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"
    return wrapper

def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"
    return wrapper

@app.route("/")
def hello_world():
    # the whay to render html:
    # return render_template("index.html", num=random.randint(1,10))

    return f"<p>Hello, World!</p>"

@app.route("/<name>")
def greet(name):
    return f"Hello, {name}"

@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return f"Bye!"

if __name__ == "__main__":
    app.run(debug=True)