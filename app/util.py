def getFiles(alg_name):
    f = open("app/static/assets/text/" + alg_name + "/input1.txt", "r") 
    i1 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input2.txt", "r") 
    i2 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input3.txt", "r") 
    i3 = f.read()
    f.close()
    
    f = open("app/static/assets/text/" + alg_name + "/input4.txt", "r") 
    i4 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input5.txt", "r") 
    i5 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input6.txt", "r") 
    i6 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input7.txt", "r") 
    i7 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input8.txt", "r") 
    i8 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input9.txt", "r") 
    i9 = f.read()
    f.close()

    f = open("app/static/assets/text/" + alg_name + "/input10.txt", "r") 
    i10 = f.read()
    f.close()

    files = [ i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    return files