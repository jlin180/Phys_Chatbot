import math
import re
from decimal import Decimal

siUnit = {
    "da" : math.pow(10,1),
    "h" : math.pow(10,2),
    "k" : math.pow(10,3),
    "M" : math.pow(10,6),
    "G" : math.pow(10,9),
    "T" : math.pow(10,12),
    "P" : math.pow(10,15),
    "E" : math.pow(10,18),
    "Z" : math.pow(10,21),
    "Y" : math.pow(10,24),
    "d" : math.pow(10,-1),
    "c" : math.pow(10,-2),
    "m" : math.pow(10,-3),
    "u" : math.pow(10,-6),
    "n" : math.pow(10,-9),
    "p" : math.pow(10,-12),
    "f" : math.pow(10,-15),
    "a" : math.pow(10,-18),
    "z" : math.pow(10,-21),
    "y" : math.pow(10,-24),
}

class num(object):
    def __init__(self, eq):
        i = 0
        while(eq[i].isdigit()):
            i+=1
        self.coef = eq[0:i]
        self.sym = eq[i:]
        unitConversion()

    def unitConversion(self):
        global siUnit
        unit = self.sym[-1]
        multi = self.sym[:-1]
        for key in siUnit:
            if(key == multi):
                multi = siUnit[key]
                break
        self.coef *= multi
        self.sym = multi
        # return str('%.2E' % Decimal(self.coef * multi)) + unit
    
    def toString(self):
        return str(self.coef)+self.sym

def calculate(equation):
    coef = []
    symbols = []
    operators = []
    nums = []
    calculateFirst = False
    items = equation.split()
    for i in items:
        if(bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)', i))):
            nums.append(num(i))
        elif(isOperator(i)):
            operators.append(i)
            if(i == "*" or i == "/"):
                calculateFirst = True
        elif(i[0].isalpha()):
            symbols.append(i)
        else:
            coef.append(i)
        
        if(len(coef) > 0 and len(symbols) > 0):
            nums.append(num(str(coef.pop())+symbols.pop()))
            if(calculateFirst):
                calculateFirst = False
                
    for i in nums:
        print(i.toString())
            


def isOperator(equation):
    if(equation == "+" or equation == "-"
     or equation == "*" or equation == "/"):
        return True
    return False


# print(unitConversion(1, "kg"))
calculate("5 kg + 29 lm+ 12kg")