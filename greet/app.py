from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def show_welcome():
    return "welcome"

@app.route("/welcome/<word>")
def show_welcome_home(word):
    return f"welcome {word}"
