from app import app
from flask import render_template, url_for, request, Flask, flash
from app.util import getFiles

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/lcs', methods=['GET', 'POST'])
def lcs():
    input_list = getFiles("lcs")

    if request.method == 'POST':
        qty = request.form['file']
        return qty
    return render_template('lcs.html', title='Lowest Common Subsequence', inpt=input_list)


@app.route('/scs', methods=['GET', 'POST'])
def scs():
    input_list = getFiles("scs")
    flash("hello")
    if request.method == 'POST':
        qty = request.form['file']
        return qty
    return render_template('lcs.html', title='Shortest Common Supersequence', inpt=input_list)