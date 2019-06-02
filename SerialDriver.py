from serial import Serial 
import time
class SerialDriver:

    def __init__(self,path,baud,bytes,paritys,rxlist,txlist):
        self.rxlist = rxlist
        self.txlist = txlist
        self.path = path
        self.baud = baud
        self.bytes = bytes
        self.paritys = paritys
        self.pic = serial.Serial(path,xonxoff=False, baudrate=baud, bytesize=bytes, parity=paritys,timeout=1, stopbits=1)
        print("Serial Driver initialized")


    def sendFrame(self,msg):
        if self.pic.is_open is False:
            self.pic.open()
        print(msg)
        self.pic.write(msg.encode())
        #for i in range(0,len(msg)):
         #   self.pic.write(msg[i].encode())
          #  print(msg[i].encode())
           # time.sleep(0.01)
        self.pic.close()

    def transmission(self):
        while(self.txqueue.qsize > 0):
            sendFrame(self.txqueue.get())

    def receiveLogic(self,rxqueue):
        print("here")
        if self.pic.is_open is False:
            self.pic.open()
        buff = b''
        while True:
            buff += self.pic.read(1000)
            while True :
                idx = buff.find(b'\n')
                if idx == -1 : break
                rx_msg = buff[:idx]
                buff = buff[idx+1:]
                print("buff")
                self.rxlist.append(rx_msg)
             
            