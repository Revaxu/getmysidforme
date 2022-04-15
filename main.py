import os
from flask import Flask, request
os.system("pip install -U amino.fix.py")
import aminofix as amino
app = Flask(__name__)


@app.route("/myname")
def revax():
        print="hello,app by revax ,don't try to change any thing,cuz all this in my host,and if u have any proplem pm amino"
        return print

@app.route("/sid", methods=['POST',"GET"])
def sidz():
       email = request.args.get("email")
       password = request.args.get("password")
       client = amino.Client(deviceId="420d1764f13a6b9ad3b04a96aec26e766bb61bd3fdbf00ccabd367e4eebff3bfc6f9b99940eb7d9a7e")
       client.login(email, password)
       sid=client.sid
       return sid
       print(sid)
       
if __name__ == '__main__':
    app.run("0.0.0.0", 9833)
