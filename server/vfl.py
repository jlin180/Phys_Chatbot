# c = wave * freq
c = 299792458

def fillEq(w, f):
    variables = { }
    variables["wavelength"] = w
    variables["freq"] = f

    return calculate(variables)

def calculate(variables):
    if(variables["wavelength"] == ""):
        res = findWavelength(variables)
    else:
        res = findFreq(variables)
    if(res == "Error"):
        return "Cannot divide by 0"
    return res

def findWavelength(variables):
    global c
    if(variables["freq"] == 0):
        return "Error"
    return c/variables["freq"]

def findFreq(variables):
    global c
    if(variables["wavelength"] == 0):
        return "Error"
    return c/variables["wavelength"]

def get(sentence):
    w = ""
    f= ""
    last = 0
    for word in sentence.split():
        if(word.isnumeric()):
            last = int (word)
        elif("Hz" == word):
            f = last
        elif("m" == word ):
            w = last
    return fillEq(w,f)