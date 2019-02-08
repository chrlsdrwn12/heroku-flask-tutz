from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    <p>Why is it so hard to find a step-by-step tutorial on how to do this?</p>

    <img src="http://loremflickr.com/600/400">
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)