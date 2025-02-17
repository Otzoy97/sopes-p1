from flask import Flask
from flask import jsonify
from flask import request
from info import Info
import requests
import codecs


app = Flask(__name__)

@app.route('/newMsg', methods=['POST'])
def newMessage():
    doc = request.get_json(force=True)
    infoA = requests.get('http://35.208.79.63/getInfo')
    infoB = requests.get('http://35.206.84.205/getInfo')
    # verifica errores
    if infoA.status_code != 200:
        return jsonify({"res": format(infoA.status_code), "ok": False})
    if infoB.status_code != 200:
        return jsonify({"res": format(infoA.status_code), "ok": False})
    if not infoA.json()["ok"]:
        return infoA.json()
    if not infoB.json()["ok"]:
        return infoB.json()
    # inicializa info
    stat = Info(infoA, infoB).toServer()
    if stat == 'A':
        res = requests.post('http://35.208.79.63/newMsg', json=doc)
        return res.json()
    res = requests.post('http://35.206.84.205/newMsg', json=doc)
    return res.json()
    
@app.route('/')
def info():
    try:
        with codecs.open("txt") as f:
            txt = f.read()
            return jsonify({"res":  {'carné': 201602782, "nombre": "Sergio Fernando Otzoy Gonzalez", "server": txt}, "ok": True})
    except:
        return jsonify({"res": "", "ok": False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)