from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjinseong



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/infos', methods=['POST'])
def write_info():
    model = request.form['model']
    price = request.form['price']
    mail_address = request.form['mail_address']


    doc = {
        'model': model,
        'price': price,
        'mail_address': mail_address,
        'flag': 0


    }
    db.infos.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '이제 메일을 기다려볼까요?!'})


@app.route('/infos', methods=['GET'])
def show_order():
    infos = list(db.infos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'infos': infos})

@app.route('/delete', methods=['POST'])
def delete_order():
    db.infos.delete_many({})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)