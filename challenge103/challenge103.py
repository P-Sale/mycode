#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start():
    return render_template("trivia.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        answer = request.form.get("answer")
        if answer == "the office":
            return redirect(url_for("correct", name = user))
        else:
            return redirect(url_for("start", name = user))

@app.route("/correct")
def correct(name):
    return f"You are correct {name}\n"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
