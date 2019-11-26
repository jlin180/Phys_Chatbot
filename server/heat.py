
# Change in heat flow = MCaT


def fillEq(m, t1, t2, c, q):
    variables = { }
    variables["mass"] = m
    variables["temp1"] = t1
    variables["temp2"] = t2
    variables["heatCapacity"] = c
    variables["heatFlow"] = q
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
    return res

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

print(fillEq(1,1,12,"",5))