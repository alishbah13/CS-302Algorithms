from app import app
from flask import render_template, url_for, request, Flask, flash
from app.util import getFiles
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
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        lookup = {}
        in1 = "String 1 : " + obj[0]
        in2 = "String 2 : " + obj[1]
        out =  "Length of Shortest Common Supersequence = " + str ( SCSLength(obj[0], obj[1], len(obj[0]), len(obj[1]), lookup) )
        return render_template('lcs.html', title='Shortest Common Supersequence', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Shortest Common Supersequence', inpt=input_list , output=out)
    
@app.route('/lvd', methods=['GET', 'POST'])
def lvd():
    input_list = getFiles("lvd")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        in1 = "String 1 : " + obj[0]
        in2 = "String 2 : " + obj[1]
        out =  "Levenshtein Distance = " + str( dist( obj[0], obj[1]) )
        return render_template('lcs.html', title='Levenshtein Distance', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Levenshtein Distance', inpt=input_list , output=out)
    
@app.route('/lis', methods=['GET', 'POST'])
def lis():
    input_list = getFiles("lis")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        in1 = "Input : " + str( obj )
        out =  "Longest Increasing Subsequence = " + str( LIS( obj ) )
        return render_template('lcs.html', title='Longest Increasing Subsequence', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Longest Increasing Subsequence', inpt=input_list , output=out)

@app.route('/mcm', methods=['GET', 'POST'])
def mcm():
    input_list = getFiles("mcm")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        in1 = "Input : " + str( obj )
        out =  "Matrix Chain Multiplication, minimum cost = " + str( MCM( obj ) )
        return render_template('lcs.html', title='Matrix Chain Multiplication', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Matrix Chain Multiplication', inpt=input_list , output=out)

@app.route('/ks01', methods=['GET', 'POST'])
def ks01():
    input_list = getFiles("ks01")
    out = " "
    in1 = " "
    in2 = " "
    in3 = " "
    if request.method == 'POST':
        dat = request.form['file']
        v = input_list[int(dat)-1]['data']['v']
        w = input_list[int(dat)-1]['data']['w']
        W = input_list[int(dat)-1]['data']['W']
        in1 = "Weights : " + str( w )
        in2 = "Values : " + str( v )
        in3 = "Required weight : " + str( W )
        out =  "Knapsack, minimum cost = " + str( KS( v, w, W ) )
        return render_template('lcs.html', title='Knapsack 0/1', inpt=input_list , output=out, in1=in1, in2=in2, in3=in3)
    return render_template('lcs.html', title='Knapsack 0/1', inpt=input_list , output=out)


@app.route('/coin', methods=['GET', 'POST'])
def coin():
    input_list = getFiles("coin")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']  
        sett = input_list[int(dat)-1]['data']['coins']
        Change_Req = input_list[int(dat)-1]['data']['money']
        in1 = "Coin Values : " + str( sett )
        in2 = "Change Required : " + str( Change_Req )
        out =  "Minimun coins Required = " + str( Coins( sett , Change_Req ) )
        return render_template('lcs.html', title='Coin Change', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Coin Change', inpt=input_list , output=out)


@app.route('/rc', methods=['GET', 'POST'])
def rc():
    input_list = getFiles("rc")
    out = " "
    in1 = " "
    in2 = " "
    if request.method == 'POST':
        dat = request.form['file']  
        price = input_list[int(dat)-1]['data']['p']
        n = input_list[int(dat)-1]['data']['n']
        length = input_list[int(dat)-1]['data']['l']
        in1 = "Rod Lenghts : " + str( length )
        in2 = "Rod prices : " + str( price )
        out =  "Profit is = " + str( Rc( price, n ) )
        return render_template('lcs.html', title='Rod Cutting', inpt=input_list , output=out, in1=in1, in2=in2)
    return render_template('lcs.html', title='Rod Cutting', inpt=input_list , output=out)

    
@app.route('/partition', methods=['GET', 'POST'])
def partition():
    input_list = getFiles("partition")
    out = " "
    in1 = " "
    if request.method == 'POST':
        dat = request.form['file']
        obj = input_list[int(dat)-1]['data']
        in1 = "Input : " + str( obj )
        out =  "Partition with equal sum possible? := " + str( Partition( obj ) )
        return render_template('lcs.html', title='Partition Problem', inpt=input_list , output=out, in1=in1)
    return render_template('lcs.html', title='Partition Problem', inpt=input_list , output=out)

