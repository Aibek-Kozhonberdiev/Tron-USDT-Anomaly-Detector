from flask import render_template

from main import app


@app.route("/", methods=['GET'])
def index():
    return render_template("transactions/index.html")
