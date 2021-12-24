from flask import *
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.likelion

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_info():
   # receive values from the form
   form_name = request.form['input_name']
   form_quantity = request.form['input_quantity']
   form_address = request.form['input_address']
   form_phone = request.form['input_phone']

   # make them as dictionary for MongoDB
   order = {'name': form_name,
   'quantity': form_quantity,
   'address': form_address,
   'phone': form_phone}
   
   # insert review
   db.memo_review.insert_one(order)

   # jsonify object
   json_object = jsonify({'result':'success', 'msg':'주문이 완료되었습니다'})

   return json_object

@app.route('/submit', methods=['GET'])
def receive_info():
   # get order information from the db
   order_list = list(db.memo_review.find({},{'_id':0}))
   
   return jsonify({'result':'success', 'msg': 'successfully loaded', 'reviews': order_list})
   
   
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)