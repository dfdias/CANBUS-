#!/usr/bin/python3
import time
from consolemenu import *
from consolemenu.items import *
from threading import Thread
from SerialDriver import *

path = '/dev/ttyUSB1' #serial path
<<<<<<< HEAD
=======

>>>>>>> c4f9316cad8a9c4854034e12523516757ac18c90

rxlist = [];
dev = SerialDriver(path,115200,8,'N',rxlist)   #sets serial Settings

# while(1):
#     if dev.pic.in_waiting > 0 :
#         datain=dev.pic.readline()
#         print(datain)
#     dev.test()

def SendMessage() :
<<<<<<< HEAD
    id = input("ID :")
    data = input("Data0:") 
    data1 = input("Data1:")
    msg= "$03"+id+data+data1+"\n1"
    done = False
=======

    msg = input("Input Message :")
>>>>>>> c4f9316cad8a9c4854034e12523516757ac18c90
    if msg :
        for x in range(0,len(msg)):
            print(msg[x])
        dev.sendFrame(msg)

def SendFromFile():##readsfrom files
    
    path = "hello.txt"#input('Enter full file PATH:')

    # do stuff

    if path :
        file = open(path, 'r')
        msg = file.readlines()
        idx = 0;
    while idx < len(msg):
        print(idx)
        time.sleep(0.1)
        dev.sendFrame(msg[idx])
        idx += 1
    
    #t.start()

#def ReadRXLOG():
    #print(dev.rxlist)
   # time.sleep(3)
  
#t=Thread(target=dev.receiveLogic)


#time.sleep(100)

def PickingSOP() :
    done = False
    l = b'01';
    msg = "12345678" #input("Input Message :")

    if dev.pic.is_open is False:
        dev.pic.open()
    dev.pic.write(b'CP')

    while done != True :
        if  dev.pic.in_waiting > 0 :
            data = dev.pic.readline();
            data = data[:-1]
            print(data)
            if data == b'P' :
                dev.pic.write(l)




menu =  ConsoleMenu("P2L Gateway CLI Utility")
send_frame = FunctionItem("Send Message", SendMessage)
send_from_file = FunctionItem("Send From File",SendFromFile)
<<<<<<< HEAD
#readlog= FunctionItem("Read Received Message LOG",ReadRXLOG)
menu.append_item(send_frame)
menu.append_item(send_from_file)
#menu.append_item(readlog)
=======
picking_sop = FunctionItem("Picking Single OP",PickingSOP)

menu.append_item(send_frame)
menu.append_item(send_from_file)
menu.append_item(picking_sop)
>>>>>>> c4f9316cad8a9c4854034e12523516757ac18c90
menu.show()











