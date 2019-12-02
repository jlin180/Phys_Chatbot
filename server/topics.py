# Contains all the topis necessary

# Circuits
# Heatflow
# Unit changes
# Heat conduction

topics = ["Circuits", "Heatflow", "Unit changes", "Heat conduction", "Waves", "Collisions",
    "Networks", "Fractal", "Chaos", "Electricity and Magnetism", "Quantum Mechanics", "Cryptography", "Gravity"]

keyWords = [["circuit","parallel","series","ohms","resistor","voltmeter","voltage","current","ammeter","amperes", "resistance", "amps", "volts"],
    ["heatflow","temperature","heat","heat capacity"], 
    ["convert units","units", "SI", "unit", "conversion"],
    ["heat conduction","thermodynamics law","heat convention"],
    ["waves","speed of light","frequency","period","wavelength","amplitude","wave properties","constructive interference","destructive interference","transverse wave","longitudinal wave", "polarization","diffraction","reflection","refraction"],
    ["elastic collision","inelastic collision"],
    ["networks", "networks structure", "connections", "erdos number", "nodes"],
    ["fractals", "fractal properties", "fractal dimension"],
    ["sensitivity to initial condition", "phase space", "invariants" ,"strange attractors"],
    ["gauss law for electric field", "guass law for magnetic field", "ampere's law", "faraday's law"],
    ["qubit","heisenberg uncertainty principle","copenhagen interpretation","entanglement"], 
    ["encryption","decryption","cryptanalysis","private key", "public key"],
    ["gravity", "force", "radius", "gravitational"]
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
    return topics[result]
