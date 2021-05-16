from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def form_gen():
    """generates form to input words"""
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def result(): 
    """generates story"""
    result = story.generate(request.args)
    return render_template('story.html', result=result)



