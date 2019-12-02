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


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
 return 'Hello to the World of Flask!'

@app.route('/check', methods=['POST'])
def check():
    # res = "check success " + request.data
    data = request.get_json()
    # print(data['input'])
    res = getResponse(data['input'])
    print(res)
    return jsonify(
        message=res
    )

def getResponse(sentence):
    topic = topics.getTopic(sentence)
    if(topic == "Error"):
        return "Sorry, I am unable to comprehend or I haven't learned yet, please rephrase."
    # Calculate things
    if("calculate" in sentence.lower() or "find" in sentence.lower()):
        print("Calculate")
        # "Circuits", "Heatflow", "Unit changes", "Heat conduction", "Waves"
        return calculateAnswer(topic, sentence)
    # Get definitions
    else:
        print("Def")
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
    elif(topic == "Heatflow"):
        ans += definitions.heatFlow
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
    elif(topic == "Chaos"):    
        ans += ""
    elif(topic == "Electricity and Magnetism"):
        ans += ""
    elif(topic == "Quantum Mechanics"):
        ans += ""
    elif(topic == "Cryptography"):    
        ans += ""            
    elif(topic == "Gravity"):    
        ans += definitions.gravity                       
    return ans

if __name__ == '__main__':
#  app.run()
 print(getResponse("calculate units for 20g to 10 kg"))
