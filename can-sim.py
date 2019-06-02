import can,time,asyncio     #global 
from p2l import *        #local
import threading
from GatewayCan import *
import queue

bus = can.Bus(interface='socketcan',
              channel='vcan0', bitrate=125000,
              receive_own_messages=True)

module = []
num_modules = 10
threads = []
for i in range(0,num_modules):
    module.append(p2l("vcan0",i+1,0xFF))   #canid 0 é atribuido ao gateway
    print(module[i].id)
    ax = threading.Thread(target=module[i].init,daemon=True)
    threads.append(ax)
    ax.start()

print("all can threads started")
print("Starting Gateway")
qtx = queue.Queue()
qrx = queue.Queue()

gateway = GatewayCan("vcan0",0xFF,qrx,qtx)
thread = threading.Thread(target=gateway.run,daemon = True)

print("sending  can messages")

thread.start()
while True :
    
    for i in range(num_modules):
        msg =[module[i].id, 0x01, 0x03+module[i].id,0x03+module[i].id]
        qtx.put(msg)
        time.sleep(0.1)
    #print(qrx.get())
    while qrx.qsize() > 0 :
        msg = qrx.get()                                                 
        print("picking terminal no : ",msg[1], "reports finished")  

