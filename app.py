from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

#make sure the varible name is the same for the next 3 lines "app"
app = Flask(__name__)

app.config['SECRET_KEY'] = "you can put something here"
debug = DebugToolbarExtension(app)


@app.route('/storyform')
def story_form():
    return render_template('form.html')

@app.route('/storytime')
def mystory():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("storytime.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)


# @app.route('/story')
# def get_greeting():
#     username = request.args["username"]
#     nice_thing = choice(COMPLIMENTS)
#     return render_template("storyform.html", user=username, compliment=nice_thing)
