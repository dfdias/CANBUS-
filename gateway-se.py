from consolemenu import *

from consolemenu.items import *

from SerialDriver import *

from queue import Queue

import serial 

path = '/dev/ttyUSB0' #serial path
txlist = Queue()
rxlist = Queue()
dev = SerialDriver(path,115200,8,'N',txlist,rxlist)   #sets serial Settings

# while(1):

#     if dev.pic.in_waiting > 0 :

#         datain=dev.pic.readline()

#         print(datain)

#     dev.test()

def SendMessage() :

    msg = input("Input Message :")

    if msg :

        for x in range(0,len(msg)):

            print(msg[x])

        dev.sendFrame(msg)

def SendFromFile():##readsfrom files

    path = "hello.txt"#input('Enter full file PATH:')

    t = time.time()

    # do stuff

    if path :

        file = open(path, 'r')

        msg = file.readlines()

        idx = 0;

    while idx < len(msg):

        print(idx)

        time.sleep(0.05)

        dev.sendFrame(msg[idx])

        idx += 1

    elapsed = time.time() - t

    print("done in ",elapsed," seconds")

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

picking_sop = FunctionItem("Picking Single OP",PickingSOP)

menu.append_item(send_frame)

menu.append_item(send_from_file)

menu.append_item(picking_sop)

menu.show()

