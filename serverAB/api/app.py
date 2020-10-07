import codecs
from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
#app.config['MONGO_HOST'] = 'mongo'
#app.config['MONGO_PORT'] = '27017'
#app.config['MONGO_DBNAME'] = 'sopes-p1'
#app.config['MONGO_USERNAME'] = 'admin'
#app.config['MONGO_PASSWORD'] = 'a12345'
#app.config['MONGO_AUTH_SOURCE'] = 'admin'
app.config['MONGO_URI'] = 'mongodb://admin:a12345@mongo:27017/sopes-p1?authSource=admin'

mongo = PyMongo(app)


@app.route('/getMsgs', methods=['GET'])
def getMessage():
    msgs = mongo.db.msgs
    output = []
    for msg in msgs.find({}):
        output.append({'autor': msg['autor'], 'oracion': msg['oracion']})
    return jsonify({'res': output, 'ok': True})


@app.route('/newMsg', methods=['POST'])
def newMessage():
    msgs = mongo.db.msgs
    doc = request.get_json(force=True)
    msgId = msgs.insert(doc)
    newMsg = msgs.find_one({'_id': msgId})
    #autor = request.json['autor']
    #oracion = request.json['oracion']
    #msgId = msgs.insert({'autor': autor, 'oracion': oracion})
    #newMsg = msgs.find_one({'_id': msgId})
    output = {'autor': newMsg['autor'], 'oracion': newMsg['oracion']}
    return jsonify({'res': output, 'ok': True})


@app.route('/getInfo', methods=['GET'])
def cpuUsage():
    try:
        with codecs.open("cpumod") as fCpu, codecs.open("rammod") as fRam:
            # recupera la infor de ambos documentos
            infoRam = fRam.read()
            infoCpu = fCpu.read()
            infoRam = infoRam.split("\n")
            infoCpu = infoCpu.split("\n")
            count = mongo.db.msgs.count_documents({})
            output = {"count": int(count), "cpu": {"total": int(infoCpu[0]), "idle": int(infoCpu[1])}, "ram": {"total": int(infoRam[0]),
                                                                                                               "free": int(infoRam[1]), "buffer": int(infoRam[2]), "cached": int(infoRam[3])}}
            return jsonify({"res": output, "ok": True})
    except:
        return jsonify({"res": "error al abrir el archivo", "ok": False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
