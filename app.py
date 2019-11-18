import flask
import random
import model

app = flask.Flask(__name__)

@app.route("/")
def index():
        return "Hallo SmartNinja!"

@app.route("/temp")
def temp():
        return flask.render_template("index.html", myname="Daniel")

@app.route("/secret_number_game")
def secret_number_game():
    number = random.randint(0, 10)
    return flask.render_template("secret_number_game.html", secret_number=number)

@app.route("/blog")
def blog():

    receipe_1 = model.Receipe("Apfelstrudel", "Cut Apple Bake Sweet", "Sweet")
    receipe_2 = model.Receipe("Hamburger", "Fry Meat and Eat", "Sauer")
    receipe_3 = model.Receipe("Suppe", "temp", "fdfd")

    return flask.render_template("blog.html", receipes=[receipe_1, receipe_2, receipe_3])

if __name__ == '__main__':
    app.run()

