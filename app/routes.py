from app import app
from flask import render_template, url_for, request, Flask, flash
from app.util import getFiles, displayOutput

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/lcs', methods=['GET', 'POST'])
def lcs():
    input_list = getFiles("lcs")

    if request.method == 'POST':
        dat = request.form['file']
        displayOutput(dat)
        return render_template('index.html')
    return render_template('lcs.html', title='Lowest Common Subsequence', inpt=input_list)


@app.route('/scs', methods=['GET', 'POST'])
def scs():
    input_list = getFiles("scs")
    
    if request.method == 'POST':
        dat = request.form['file']
        return dat
    else:
        flash("hello")
    return render_template('lcs.html', title='Shortest Common Supersequence', inpt=input_list)