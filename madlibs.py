"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Show user madlibs form if they want to play a game."""

    game = request.args.get("play-game")

    if game == "True":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib', methods=['POST'])
def show_madlib():
    """Show madlib."""

    person = request.form.get("person")

    color = request.form.get("color")

    noun = request.form.get("noun")

    adjective = request.form.get("adjective")

    verb = request.form.get("verb")

    return render_template("madlib.html", person=person, color=color,
                           noun=noun, adjective=adjective, verb=verb)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
