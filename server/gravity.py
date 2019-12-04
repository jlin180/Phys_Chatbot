#  F = G (m1m2)/r^2
import math
from decimal import *

def fillEq(f, g, m1, m2, r):
    variables = { }
    variables["force"] = f
    variables["gravity"] = 6.67 * math.pow(10,-11)
    variables["mass1"] = m1
    variables["mass2"] = m2
    variables["rad"] = r

    return calculate(variables)

def calculate(variables):
    if variables["force"] == "":
        res = findForce(variables)
    elif variables["gravity"] == "":
        res = findGravity(variables)
    elif variables["mass1"] == "":
        res = findMissingMass(variables)
    elif variables["mass2"] == "":
        res = findMissingMass(variables)
    elif variables["rad"] == "":
        res = findRad(variables)
    if(res == "Error"):
        return "Cannot divide by 0"
    return str('%.2E' % Decimal(res))

def findForce(variables):
    if(variables["rad"] == 0):
        return "Error"
    return (variables["gravity"] * (variables["mass1"] * variables["mass2"])) / math.pow(variables["rad"], 2)

def findGravity(variables):
    num = variables["force"] * math.pow(variables["rad"], 2)
    den = (variables["mass1"] * variables["mass2"])
    if(den == 0):
        return "Error"
    return num/den

def findMissingMass(variables):
    num = variables["force"] * math.pow(variables["rad"], 2)
    if(variables["mass1"] == ""):
        den = variables["mass2"] * variables["gravity"]
    else:
        den = variables["mass1"] * variables["gravity"]
    if(den == 0):
        return "Error"
    return num/den

def findRad(variables):
    if(variables["force"] == 0):
        return "Error"
    return math.sqrt(variables["gravity"] * (variables["mass1"] * variables["mass2"] * variables["force"]))

def get(sentence):
    f = ""
    g = ""
    m1 = ""
    m2 = ""
    r = ""
    last = 0
    for word in sentence.split():
        if(word.isnumeric()):
            last = int (word)
        elif("m" == word):
            r = last
        elif("kg" == word ):
            if(m1 == ""):
                m1 = last
            else:
                m2 = last
        elif("N" == word):
            f = last
    return fillEq(f,g,m1,m2,r)