from flask import Flask,jsonify
app=Flask(__name__)
#store=shop
#stores=shops
stores=[{'name':'My Wonderful Store', 'items':[{'name':'My item','price':15.99}]}]

#POST /store data:{name:}
#client wants to create a store and we(the server)is retrieving that request as POST and would be passing it 
# through the method-->create_store
@app.route('/store',methods=['POST'])
def create_store():
    pass

#GET/store/<string:name>
#we(server)is sending data via GET
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET/store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
    #http://127.0.0.1:5000/store
    #{"stores":[{"items":[{"name":"My item","price":15.99}],"name":"My Wonderful Store"}]}

#POST /store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass

#GET/store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port=5000)