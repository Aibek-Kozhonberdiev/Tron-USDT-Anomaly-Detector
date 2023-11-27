from flask import render_template
from flask import request

from main import app
from .transactions import Transactions


@app.route("/", methods=['GET'])
def index():
    return render_template("transactions/index.html")

@app.route("/transactions/", methods=['GET'])
def transactions():
    page = request.args.get('limit', default=20)
    transactions = Transactions()
    return render_template('transactions/transactions.html', transactions=transactions.get_objects(limit=page))

@app.route("/coefficient/", methods=['GET'])
def coefficient():
    coefficient = Transactions()
    return render_template('transactions/coefficient.html', coefficient=coefficient.assess_risk())

@app.route('/analysis/', methods=['GET'])
def analysis():
    analysis = Transactions()
    return render_template('transactions/analysis.html', analysis=analysis.start_checking())
