from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'sopes-p1'
app.config['MONGO_URI'] = 'mongodb://admin:a12345@0.0.0.0:27017/sopes-p1'

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
    return jsonify({'res': doc, 'ok': True})

@app.route('/getCpu', methods=['GET'])
def cpuUsage():
    return jsonify({"res": '', 'ok': True})

@app.route('/getRam', methods=['GET'])
def ramUsage():
    return jsonify({"res": '', 'ok': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)