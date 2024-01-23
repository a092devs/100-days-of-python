from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'>Hello, World!</h1>"
        "<p>This is a paragraph.</p>"
        "<img src='https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif'>"
    )


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "<p>Bye</p>"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
