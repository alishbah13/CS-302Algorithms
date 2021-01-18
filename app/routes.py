from app import app
from flask import render_template, url_for, request, Flask, flash
from app.util import getFiles, displayOutput
from app.dp import *

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/lcs', methods=['GET', 'POST'])
def lcs():
    input_list = getFiles("lcs")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        lookup = {}
        in1 = "String 1 : " + obj[0]
        in2 = "String 2 : " + obj[1]
        out =  "Length of Longest Common Subsequence = " + str ( LCS(obj[0], obj[1], len(obj[0]), len(obj[1]), lookup) )
        return render_template('lcs.html', title='Lowest Common Subsequence', inpt=input_list , output=out, in1=in1, in2=in2)
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