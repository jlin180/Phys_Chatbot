# Contains all the topis necessary

# Circuits
# Heatflow
# Unit changes
# Heat conduction

topics = ["Circuits", "Heatflow", "Unit changes", "Heat conduction", "Waves", "Collisions",
    "Networks", "Fractal", "Chaos", "Electricity and Magnetism", "Quantum Mechanics", "Cryptography", "Gravity"]

keyWords = [["circuit", "circuits", "parallel","series","ohms","resistor","voltmeter","voltage","current","ammeter","amperes", "resistance", "amps", "volts"],
    ["heatflow", "heat flow", "temperature","heat","heat capacity", "temperature", "entropy", "hot to cold", "warm to cold", "transfer", "energy"], 
    ["convert units","units", "SI", "unit", "conversion", "change", "to", "from", "convert", "changes"],
    ["heat conduction","thermodynamics law","heat convention", "temperature", "high to low", "higher temperature to lower", "heat"],
    ["waves", "wave", "speed of light", "frequency", "period", "wavelength", "amplitude", "wave properties", "constructive interference", "destructive interference", "transverse wave", "longitudinal wave", "polarization", "diffraction", "reflection", "refraction", "constructive", "destructive", "interference"],
    ["collision", "collisions", "elastic", "collides", "inelastic", "crashes", "collide", "hit", "smash", "crash"],
    ["networks", "networks structure", "connections", "erdos number", "nodes", "node", "connect", "connection", "vertices", "degrees of seperation", "neighbor"],
    ["fractals", "fractcal", "fractal properties", "fractal dimension", "repeating", "loop", "copies", "copy", "statistics", "similarity", "self-similarity", "self similarity", "statistical"],
    ["chaos", "sensitivity to initial condition", "phase space", "invariants" ,"strange attractors", "deterministic", "not predictable", "time series", "invariant", "real", "same", "pulled", "pulling", "towards", "attract", "attracts", "attractor", "attractors", "trajectories", "pushed apart", "strange"],
    ["electricity and magnetism", "eletricity", "magnetism", "gauss law for electric field", "gauss law for magnetic field", "ampere's law", "faraday's law", "flux", "electric", "eletric law", "magnetic", "gauss", "law", "faraday", "faraday's", "field", "magnetic"],
    ["quantum", "qubit","heisenberg uncertainty principle","copenhagen interpretation","entanglement", "uncertainty", "copenhagen", "heisenberg", "zero or one", "0 or 1", "zero or 1", "0 or one", "quantum mechanic", "quantum mechanics"], 
    ["cryptography", "crypto", "encryption", "decryption", "cryptanalysis", "private key", "public key", "send", "safety", "private", "key", "public", "safe"],
    ["gravity", "force", "radius", "gravitational", "constant", "falling", "fall", "earth", "9.81", "m/s^2", "m/(s^2)","meters per second squared", "meter per second squared", "acceleration", "pull"]
]


def getTopic(sentence):
    global topics
    global keyWords
    result = 0
    maxCount = 0
    index = 0
    for words in keyWords:
        temp = 0
        for word in sentence.split():
            if(word.lower() in words):
                temp += 1
        if(temp > maxCount):
            result = index
            maxCount = temp
        index += 1
    if(maxCount == 0):
        return "Error"
    return topics[result]
