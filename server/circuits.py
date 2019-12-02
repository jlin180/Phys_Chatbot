from decimal import *
import math

# V = IR


def seriesCurrent(resistors, voltage):
    s = seriesResistance(resistors)
    if(s == 0):
        return "Cannot divide by 0"
    return voltage/s

def seriesResistance(resistors):
    s = 0
    for i in resistors:
        s += i
    return s

def parallelCurrent(resistors, voltage):
    s,count = parallelResistance(resistors)
    if(s == 0):
        return "Cannot divide by 0"
    res = int(math.pow(10,count) / s)
    return voltage/res

def parallelResistance(resistors):
    s = 0
    for  i in resistors:
        s += 1/i
    # Convert back to 1/x
    d = Decimal(s)
    d = d.as_tuple().exponent
    count = 0
    while( d < 0 and count < 5):
        s *= 10
        d+=1
        count+=1
    return s,count

def get(sentence):
    resistors = []
    last = 0
    voltage = -1
    for word in sentence.split():
        if(word.isnumeric()):
            last = int (word)
            if not(voltage == -1):
                resistors.append(int (word))
        if("voltage" in word or "volts" in word or "V" in word):
            voltage = last
    if("series" in sentence):
        return "The current is "+ str('%.2E' % Decimal(seriesCurrent(resistors, voltage))) + "A"
    elif("parallel" in sentence):
        return "The current is "+ str('%.2E' % Decimal(parallelCurrent(resistors, voltage))) + "A"
    return "I didn't understand the question. Please list the voltages and each of the resistors"
        
        
