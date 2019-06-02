import can,threading,serial

from queue import Queue
#Runs as a separate thread
class GatewayCan(object):

    def __init__(self,cbus,canid,queueRX,queueTX):
        self.canid = canid
        print(self.canid)
        self.queueRX = queueRX
        self.queueTX = queueTX
        self.cbus = can.Bus(interface='socketcan',channel=cbus, bitrate=125000)

    def run(self):
        while True:
            if(self.queueTX.qsize() > 0):
                while (self.queueTX.qsize() > 0): 
                   #empty's buffer queue
                    msg = self.queueTX.get()
                    message = can.Message(arbitration_id=123, is_extended_id=False,
                      data=msg)
                    self.cbus.send(message)
            rx = self.cbus.recv(timeout=0.2)            #
            if rx != None :
#               print("Received Data  :",rx)   
                if(rx.data[0] == self.canid):
                    self.queueRX.put(rx.data)

