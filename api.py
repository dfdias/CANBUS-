from flask import Flask, request
from flask_restful import Resource,Api
from sqlalchemy import create_engine
import json
from flask_jsonpify import jsonify
from queue import Queue

from canSim import *
from Porder import *


app = Flask(__name__)
api = Api(app)
txqueue = Queue()
rxqueue = Queue()
num_modules = 10
sim = canSim(num_modules,txqueue,rxqueue)
num = 0;



print (a["qty"])

def parse(self):
    #still an idea
    pass

class PickingOrder(Resource):
    qty = []
    pos = []
    p = Porder(num,qty,pos) 
    def post(self,data):
        pass
    def get(self):    
        return(jsonify(a))

api.add_resource(PickingOrder,"/picking")

if __name__ == '__main__':
     app.run(port='5002')