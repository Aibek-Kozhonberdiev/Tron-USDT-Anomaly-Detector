from flask import render_template

from main import app
from .transactions import get_objects


@app.route("/", methods=['GET'])
def index():
    return render_template("transactions/index.html")

@app.route("/transactions/", methods=['GET'])
def transactions():
    transactions = get_objects()
    return render_template('transactions/transactions.html', transactions=transactions)
