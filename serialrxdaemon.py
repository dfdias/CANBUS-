import time,sqlite3

from SerialDriver import *
conn = sqlite3.connect('pind.db')
c = conn.cursor()
path = '/dev/ttyUSB1' #serial path

rxlist = [];
dev = SerialDriver(path,115200,8,'N',rxlist)   #sets serial Settings
dev.pic.close()
idx = 0;
while dev.pic.is_open is True: 
    if dev.pic.is_open is False : break;
while True:
    print("here2")
    dev.receiveLogic();
    ID = dev.rxlist[idx]
    ID = ID[2:]
    print(rxlist)
    times = time.strftime("%H:%M:%S")
    date = time.strftime("%I:%M:%S")
    timestamp = date + "@" + time
    c.execute("INSERT INTO RX VALUES ('"+ID+"','"+timestamp+"')") #writes log into db

