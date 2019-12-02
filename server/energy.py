import math
from decimal import *
#  E wavelength = hc

c = 299792458
h = 6.62607004 * math.pow(10, -34)

def fillEq(e, w):
    variables = { }
    variables["energy"] = e
    variables["wavelength"] = w

    return calculate(variables)

def calculate(variables):
    if(variables["wavelength"] == ""):
        res = findWavelength(variables)
    else:
        res = findEnergy(variables)
    if(res == "Error"):
        return "Cannot divide by 0"
    return str('%.2E' % Decimal(res))

def findWavelength(variables):
    global c
    if(variables["energy"] == 0):
        return "Error"
    return (h*c)/variables["energy"]
def findEnergy(variables):
    global c
    global h
    if(variables["wavelength"] == 0):
        return "Error"
    return (h*c)/variables["wavelength"]