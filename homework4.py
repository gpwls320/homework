from flask import Flask,render_template, jsonify, request
from pymongo import MongoClient

app=Flask(__name__)

client = MongoClient('localhost', 27017)
db=client.dbsparta

@app.route('/')
def home():
    return render_template('homework4.html')

@app.route('/order', method=["POST"])
def post_order():
    orderName = request.form['orderName']
    quantity= request.form['quantity']
    totalPrice = request.form['totalPrice']
    email = request.form['email']
    address = request.form['address']
    orderMessage=request.form['orderMessage']

    # order
    new_rorder = {
        "orderName": orderName,
        "quantity": quantity,
        "totalPrice": totalPrice,
        "email": email,
        "address": address,
        "orderMessage": orderMessage
    }

    # db insert
    db.orders.insert_one(new_order)
    return jsonify({'result': 'success', 'msg': '주문 완료!'})


@app.route('/orderlist', methods=["GET"])
def get_order():

    orderlist=list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orderlist': orderlist})

if __name__ == "__main__":
    app.run('localhost', 5000)