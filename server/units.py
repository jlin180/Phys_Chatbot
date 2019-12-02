import math
import re
import sys
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
        self.flag = False
        i = 0
        while(eq[i].isdigit()):
            i+=1
        self.coef = float(eq[0:i])
        self.sym = str(eq[i:])
        self.unitConversion()

    def unitConversion(self):
        global siUnit
        used = False
        unit = self.sym[-1]
        if(len(self.sym) == 1):
            multi = 1
            used = True
        else:
            multi = self.sym[:-1]
            for key in siUnit:
                if(key == multi):
                    multi = siUnit[key]
                    used = True
                    break
        if(not used):
            self.flag = True
        self.coef = self.coef * multi
        self.sym = unit
        return 1
        # return str('%.2E' % Decimal(self.coef * multi)) + unit
    
    def toString(self):
        return str(self.coef)+str(self.sym)

def generateObjects(equation):
    coef = []
    symbols = []
    operators = []
    nums = []
    calculateFirst = False
    items = equation.split()
    for i in items:
        if(bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)', i))):
            n = num(i)
            if(n.flag):
                return "Unit not found"
            nums.append(n)
        elif(isOperator(i)):
            operators.append(i)
            # if(i == "*" or i == "/"):
            #     calculateFirst = True
        elif(i[0].isalpha()):
            symbols.append(i)
        else:
            coef.append(i)
        
        if(len(coef) > 0 and len(symbols) > 0):
            n = num(str(coef.pop())+symbols.pop())
            if(n.flag):
                return "Unit not found"
            nums.append(n)
            # if(calculateFirst):
            #     calculateFirst = False

    return calculateEquation(nums, operators)
            
def calculateEquation(nums, operators):
    time = sys.maxsize 
    distance = sys.maxsize
    mass = sys.maxsize
    for i in range(len(nums)):
        n = nums[i]
        if(i > 0):
            op = operators[i-1]
        if(n.sym == "s"):
            if(time == sys.maxsize):
                time = n.coef
            else:
                time = update(time, n.coef, op)
        elif(n.sym == "g"):
            if(mass == sys.maxsize):
                mass = n.coef
            else:
                mass = update(mass, n.coef, op)
        elif(n.sym == "m"):
            if(distance == sys.maxsize):
                distance = n.coef
            else:
                distance = update(distance, n.coef, op)
    return getResult(time,mass,distance)
    
def getResult(time, mass, distance):
    result = ""
    if(distance == "Error"):
        return "Error, cannot divide by 0"
    if not(time == 0 or time == sys.maxsize):
        result += str(time)+ "s "
    if not(mass == 0 or mass == sys.maxsize):
        if not(result == ""):
            result += "+ "
        result += str(mass)+ "g "  
    if not(distance == 0 or distance == sys.maxsize):
        if not(result == ""):
            result += "+ "
        result += str(distance)+ "m "
    return result  

def update(val1, val2, op):
    if(op == "+"):
        return (val1 + val2)
    elif(op == "-"):
        return (val1 - val2)
    elif(op == "/"):
        if(val2 == 0):
            return "Error"
        return (val1 / val2)
    return (val1 * val2)

def isOperator(equation):
    if(equation == "+" or equation == "-"
     or equation == "*" or equation == "/"):
        return True
    return False
