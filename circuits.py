import decimal
import math

# V = IR
seriesDef = "A circuit where the current follows one paths"
parallelDef = "A circuit where current diverges into multiple paths"

def seriesCurrent(resistors, voltage):
    s = seriesResistance(resistors)
    return voltage/s

def seriesResistance(resistors):
    s = 0
    for i in resistors:
        s += i
    return s

def parallelCurrent(resistors, voltage):
    print(resistors)
    s,count = parallelResistance(resistors)
    res = int(math.pow(10,count) / s)
    return voltage/res

def parallelResistance(resistors):
    s = 0
    for  i in resistors:
        s += 1/i
    # Convert back to 1/x
    d = decimal.Decimal(s)
    d = d.as_tuple().exponent
    count = 0
    while( d < 0 and count < 5):
        s *= 10
        d+=1
        count+=1
    return s,count

print("Hello World")
print(seriesCurrent([30,30,30], 90))