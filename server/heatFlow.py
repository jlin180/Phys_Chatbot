from decimal import *
# Change in heat flow = MCaT

def fillEq(m, t1, t2, c, q):
    variables = { }
    variables["mass"] = m
    variables["temp1"] = t1
    variables["temp2"] = t2
    variables["heatCapacity"] = c
    variables["heatFlow"] = q
    print(variables)
    return calculate(variables)

def calculate(variables):
    if variables["mass"] == "":
        res = findMass(variables)
    elif variables["temp1"] == "":
        res = findMissingTemp(variables)
    elif variables["temp2"] == "":
        res = findMissingTemp(variables)
    elif variables["heatCapacity"] == "":
        res = findHeatCapacity(variables)
    elif variables["heatFlow"] == "":
        res = findHeatFlow(variables)
    else:
        return "Insufficient variables for calculation"
    if(res == "Cannot divide by 0"):
        return res
    return str('%.2E' % Decimal(res))

def findMass(variables):
    if(variables["temp1"] == variables["temp2"] or variables["heatCapacity"] == 0):
        return "Cannot divide by 0"
    return (variables["heatFlow"]/ (abs(variables["temp1"]-variables["temp2"])*variables["heatCapacity"]))

def findMissingTemp(variables):
    if(variables["mass"] or variables["heatCapacity"] == 0):
        return "Cannot divide by 0"
    x = (variables["heatFlow"]/ (variables["mass"] * variables["heatCapacity"]))
    if(variables["temp1"] == ""):
        return x + variables["temp2"]
    else:
        return variables["temp1"] - x

def findHeatCapacity(variables):
    if(variables["temp1"] == variables["temp2"] or variables["mass"] == 0):
        return "Cannot divide by 0"
    return (variables["heatFlow"]/ (abs(variables["temp1"]-variables["temp2"])*variables["mass"]))

def findHeatFlow(variables):
    return (variables["heatCapacity"] * abs(variables["temp1"]-variables["temp2"]) * variables["mass"])

def get(sentence):
    m = ""
    t1 = ""
    t2 = ""
    c = ""
    q = ""
    last = 0
    for word in sentence.split():
        if(word.isnumeric()):
            last = int (word)
            print(last)
        elif("kg" in word):
            m = last
        elif("K" == word):
            print("K")
            if(t1 == ""):
                t1 = last
                print(t1)
            elif (t2 == ""):
                t2 = last
                print(t2)
        elif("J/K" in word):
            c = last
        elif("J" in word and "J/K" not in word):
            q = last
    return fillEq(m, t1, t2, c, q)
