from flask import *
import requests

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.likelion

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET'])
def listing():
    orders = list(db.likelion.find({},{'_id':0}))

    return jsonify({'result':'success', 'orders':orders})


@app.route('/submit', methods=['POST'])
def submit_info():
    name = request.form['form_name']
    quantity = request.form['form_quantity']
    address = request.form['form_address']
    phone = request.form['form_phone']
    
    db.likelion.insert_one({'name': name, 'quantity': quantity, 'address': address, 'phone': phone})

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)