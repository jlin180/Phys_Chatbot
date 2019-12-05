from flask import Flask, request, jsonify
from flask_cors import CORS

# Imports
import circuits
import definitions
import energy
import gravity
import heatFlow
import topics
import units
import vfl

startup = False
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    res = getResponse(data['input'])
    print(res)
    return jsonify(
        message=res
    )

def getResponse(sentence):
    global startup
    print(startup)
    if (startup == False):
        startup = True
        return SayHello()
    topic = topics.getTopic(sentence)
    if(topic == "Error"):
        return "Sorry, I am unable to comprehend or I haven't learned yet, please rephrase."
    # Calculate things
    if("calculate" in sentence.lower() or "find" in sentence.lower()):
        return calculateAnswer(topic, sentence)
    # Get definitions
    else:
        return getDefinition(topic, sentence)

def calculateAnswer(topic, sentence):
    if(topic == "Circuits"):
        ans = circuits.get(sentence)
    elif(topic == "Heatflow"):
        ans = heatFlow.get(sentence)
    elif(topic == "Unit changes"):
        ans = units.get(sentence)
    elif(topic == "Gravity"):
        ans = gravity.get(sentence)
    elif(topic == "Waves"):
        ans = vfl.get(sentence)
    elif(topic == "Planks"):
        ans = energy.get(sentence)
    return ans

def getDefinition(topic, sentence):
    ans = ""
    if(topic == "Circuits"):
        if("series" in sentence):
            ans += definitions.seriesCircuit
        if("parallel" in sentence): 
            ans += definitions.parallelCircuit
        else:
            ans += definitions.circuit
    elif(topic == "Heatflow"):
        if("flow" in sentence):
            ans += definitions.heatFlow
        if("capacity" in sentence):
            ans += definitions.heatCapacity
        if("conduction" in sentence):
            ans += definitions.heatConduction
        if("convention" in sentence):
            ans += definitions.heatConvention
        if("temperature" in sentence):
            ans += definitions.temperature
    elif(topic == "Unit changes"):    
        ans += definitions.SI
    elif(topic == "Heat conduction"):    
        ans += definitions.heatConduction
    elif(topic == "Waves"):
        ans += definitions.Wave
    elif(topic == "Collisions"):    
        if("elastic" in sentence):
            ans += definitions.elasticCollision
        if("inelastic" in sentence):
            ans += definitions.inelasticCollision    
    elif(topic == "Networks"):    
        if("networks" in sentence):
            ans += definitions.networks
        if("nodes" in sentence):
            ans += definitions.nodes
        if("connections" in sentence):
            ans += definitions.connections
    elif(topic == "Fractal"):    
        ans += definitions.fractals
        if("properties" in sentence):
            ans += "Properties that it contains are: \n"
            for prop in definitions.fractalProperties:
                ans += prop + " is " + definitions.fractalProperties[prop]
    elif(topic == "Chaos"):    
        ans += "Chaos contains the following properties: \n"
        for prop in definitions.Chaos:
            ans += prop + " is " + definitions.Chaos[prop]
    elif(topic == "Electricity and Magnetism"):
        ans += "Electricity and magnetism contains the following properties: \n"
        for prop in definitions.electricMagnetism:
            ans += prop + " is " + definitions.electricMagnetism[prop]
    elif(topic == "Quantum Mechanics"):
        ans += ""
        if("entanglement" in sentence):
            ans += definitions.entanglement
        if("uncertainty" in sentence):
            ans += definitions.uncertaintyPrinciple
        if("copenhagen" in sentence):
            ans += definitions.copenhagenInterpretation
        if("qubit" in sentence):
            ans += definitions.qubit
    elif(topic == "Cryptography"):    
        if("encryption" in sentence):
            ans += definitions.encryption
        if("decryption" in sentence):
            ans += definitions.decryption
        if("cryptanalysis" in sentence):
            ans += definitions.cryptanalysis
        if("private" in sentence):
            ans += definitions.privateKey
        if("public" in sentence):
            ans += definitions.publicKey  
        else:
            ans += definitions.cryptography          
    elif(topic == "Gravity"):    
        ans += definitions.gravity                       
    return ans

def SayHello():
    return "Hello, I am a basic bot that can give definitions and minor calculations. I will try my best to help!!!"

if __name__ == '__main__':
 app.run()
