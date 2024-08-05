# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def calc_add():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a,b))

@app.route("/sub")
def calc_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a,b))

@app.route("/mult")
def calc_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a,b))

@app.route("/div")
def calc_div():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a,b))

OPERATIONS = {"add": add, "sub": sub, "mult": mult, "div": div}
@app.route("/math/<operation>")
def math_calc(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(OPERATIONS[operation](a,b))
