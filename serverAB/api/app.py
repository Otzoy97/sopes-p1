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
    return jsonify({'res': '', 'ok': True})


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


@app.route('/getCpu', methods=['GET'])
def cpuUsage():
    try:
        with codecs.open("cpumod") as f:
            info = f.read()
            info = info.split("\n")
            return jsonify({"res": {"total": info[0], "idle": info[1]}, "ok": True})
    except:
        return jsonify({"res": "error al abrir el archivo", "ok": False})


@app.route('/getRam', methods=['GET'])
def ramUsage():
    try:
        with codecs.open("rammod") as f:
            info = f.read()
            info = info.split("\n")
            return jsonify({"res": {"total": info[0],
                                    "free": info[1], "buffer": info[2], "cached": info[3]}, "ok": True})
    except:
        return jsonify({"res": 'error al abrir el archivo', 'ok': False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
