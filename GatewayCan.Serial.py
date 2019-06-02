import can,threading,serial
from SerialDriver import *
from queue import Queue
#Runs as a separate thread
class GatewayCanSerial(object):

    def __init__(self,cbus,canid,queueRX,queueTX):
        self.canid = canid
        print(self.canid)
        self.queueRX = queueRX
        self.queueTX = queueTX
        self.cbus = can.Bus(interface='socketcan',channel=cbus, bitrate=125000)
        path = "/dev/ttyUSB0"
        dev = SerialDriver(path,115200,8,'N',self.queueRX,self.queueTX) 
        
        thread = []
        thread.append(target=dev.transmission,daemon=True)  #serial Starter
        thread.append(target=dev.receiveLogic,daemon=True)
        for t in thread:
            thread[t].start()
        

    def run(self):
        while True:
            if(self.queueRX.qsize() > 0):
                while (self.queueRX.qsize() > 0): 
                   #empty's buffer queue
                    msg = self.queueTX.get()
                    message = can.Message(arbitration_id=123, is_extended_id=False,
                      data=msg)
                    self.cbus.send(message)
            rx = self.cbus.recv(timeout=0.2)            #
            if rx != None :
#                print("Received Data  :",rx)   
                if(rx.data[0] == self.canid):
                    self.queueTX.put(rx.data)

