from app import app
from flask import render_template, url_for, request, Flask, flash
from app.util import getFiles, displayOutput

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/lcs', methods=['GET', 'POST'])
def lcs():
    # input_list = getFiles("lcs")
    # return input_list[0]
    input_list = [1,2,3,4,5,6,7,8,9,10]
    out = " "
    if request.method == 'POST':
        dat = request.form['file']
        out = displayOutput(dat)
        return render_template('lcs.html', title='Lowest Common Subsequence', inpt=input_list , output=out)
    return render_template('lcs.html', title='Lowest Common Subsequence', inpt=input_list , output=out)


@app.route('/scs', methods=['GET', 'POST'])
def scs():
    input_list = getFiles("scs")
    out = " "
    if request.method == 'POST':
        dat = request.form['file']
        return dat
    else:
        flash("hello")
    return render_template('lcs.html', title='Shortest Common Supersequence', inpt=input_list, output=out)