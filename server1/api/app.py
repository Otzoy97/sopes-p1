from flask import Flask
import requests
from flask import jsonify

app = Flask(__name__)

@app.route('/newMsg', methods=['GET'])
def newMessage():
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
    # determina el uso de cpu y ram
    infoA = infoA.json()["res"]
    infoB = infoB.json()["res"]
    # uso de cpu/ram A
    cpuA = infoA["cpu"]
    ramA = infoA["ram"]
    cpuAUsage = (cpuA["total"] - cpuA["idle"])* (100/cpuA["total"])
    ramAUsage = (ramA["total"] - ramA["free"] - ramA["buffer"] - ramA["cached"]) * (100/ramA["total"])
    # uso de cpu/ram B
    cpuB = infoA["cpu"]
    ramB = infoA["ram"]

    cpuBUsage = (cpuB["total"] - cpuB["idle"])* (100/cpuB["total"])
    ramBUsage = (ramB["total"] - ramB["free"] - ramB["buffer"] - ramB["cached"]) * (100/ramB["total"])
    
    output = {"A": {"cpuUsage" : cpuAUsage, "ramUsage": ramAUsage}, "B" : {"cpuUsage" : cpuBUsage, "ramUsage": ramBUsage}}
    return jsonify({"res": output, "ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)