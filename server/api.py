from flask import Flask,jsonify
import flask 
from flask_cors import CORS
# import index
import dbconnection

exit
app = Flask(__name__)
CORS(app)

key = open('keys/public_1.pem').read() # importing server public key 1


@app.route("/")
def index():
  return "Hello, World!"


@app.route("/serverkey",methods=['GET']) #send server public key (key 1)
def get():
   return jsonify({'Key':key})
   

@app.route("/clientkey",methods=['POST']) # get client public key
def starting_url():
    json_data = flask.request.get_json(force=True)
    a_value = json_data["client_public_key"]
    f = open("keys/clientPublicKey.pem", "w")
    clientKey =str(a_value) 
    sql = "UPDATE server SET clientPublicKey = '"+clientKey+"'"
    val = ("private_key")
    dbconnection.cursor.execute(sql,val) #save client public key in DB
    dbconnection.connection.commit()
    f.write(clientKey)

    print(a_value)
    return a_value




if __name__=="__main__":
   app.run(debug=True)

