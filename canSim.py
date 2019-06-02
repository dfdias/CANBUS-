import can,time,asyncio     #global 
from p2l import *        #local
import threading
from GatewayCan import *
import queue

class canSim(object):

    def __init__(self,num_modules,txqueue,rxqueue):
        self.bus = can.Bus(interface='socketcan',
              channel='vcan0', bitrate=125000,
              receive_own_messages=True)
        self.num_modules = num_modules
        self.module = []
        threads = []
        self.qtx = txqueue
        self.qrx = rxqueue
      
        for i in range(0,num_modules):
            self.module.append(p2l("vcan0",i+1,0xFF))   #canid 0 é atribuido ao gateway
            print(self.module[i].id)
            ax = threading.Thread(target=self.module[i].init,daemon=True)
            threads.append(ax)



        self.gateway = GatewayCan("vcan0",0xFF,self.qrx,self.qtx)
        threads.append(threading.Thread(target=self.gateway.run,daemon = True))

        #starting 

        for f in range(0,len(threads)):
            threads[f].start()
        print("all can threads started")
        print("Starting Gateway")


    