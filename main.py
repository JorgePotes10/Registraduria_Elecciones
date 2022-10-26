from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorPartido import ControladorPartido

app=Flask(__name__)
cors = CORS(app)

miControladorCandidato=ControladorCandidato()
miControladorMesa=ControladorMesa()
miControladorResultado=ControladorResultado()
miControladorPartido=ControladorPartido()

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://japotes7:0710Alex199110@cluster0.9hgajnz.mongodb.net/db_registraduria?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["db_registraduria"]
print(baseDatos.list_collection_names())

###########################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###########################################################
@app.route("/candidato",methods=['GET'])
def getCandidato():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato1(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)
###########################################################
@app.route("/partido",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido1(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
@app.route("/partido/<string:id>/mesa/<string:id_mesa>",methods=['PUT'])
def asignarMesaPartido(id,id_mesa):
    json=miControladorPartido.asignarMesa(id,id_mesa)
    return jsonify(json)
####################################################################################
@app.route("/mesa",methods=['GET'])
def getMesa():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa1(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa1(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
@app.route("/mesa/candidato/<string:id_candidato>/partido/<string:id_partido>",methods=['POST'])
def crearMesa1(id_candidato,id_partido):
    data = request.get_json()
    json=miControladorMesa.create(data,id_candidato,id_partido)
    return jsonify(json)
@app.route("/mesa/<string:id_rol>/candidato/<string:id_candidato>/partido/<string:id_partido>",methods=['PUT'])
def modificarMesa(id_rol,id_candidato,id_partido):
    data = request.get_json()
    json=miControladorMesa.update(id_rol,data,id_candidato,id_partido)
    return jsonify(json)
#######################################################################################################################
@app.route("/resultado",methods=['GET'])
def getResultado():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado1(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultado/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.create(data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultado/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.update(id_resultado,data,id_candidato,id_mesa)
    return jsonify(json)
@app.route("/resultado/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)
#######################################################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
