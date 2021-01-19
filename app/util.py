import json
def getFiles(alg_name):
    f = open("app/static/assets/text/" + alg_name + "/0.json", "r") 
    # i1 = f.read()
    i1 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/1.json", "r") 
    i2 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/2.json", "r") 
    i3 = json.load(f) 
    f.close()
    
    f = open("app/static/assets/text/" + alg_name + "/3.json", "r") 
    i4 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/4.json", "r") 
    i5 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/5.json", "r") 
    i6 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/6.json", "r") 
    i7 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/7.json", "r") 
    i8 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/8.json", "r") 
    i9 = json.load(f) 
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/9.json", "r") 
    i10 = json.load(f) 
    f.close()

    files = [ i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    return files
