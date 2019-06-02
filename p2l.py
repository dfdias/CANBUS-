import can

class p2l(object): 


    def __init__(self,cbus,id,gateid): #cbus defines the canbus that is being operated, id defines the id of the p2l itself and gateid is the can gateway ID
        self.cbus = cbus    #cbus => CANBUS
        self.id = id        #id => can arbitration ID
        self.bus = can.Bus(interface='socketcan',channel=cbus, bitrate=125000)
        self.gateid =  gateid
        print(self.bus)


    def init(self):
        states = ["sby","picking"]
        NS = states[0]
        while  True :
            PS = NS
            if (PS == states[0]):
                rx = self.bus.recv(timeout=None)
                if rx.data[0] == self.id:
                    if rx.data[1] == 0x01:
                        NS = "picking"
                else: NS = "sby"
            if (PS == states[1]):
                qty = rx.data[2]
                qty2 = rx.data[3]
                print("p2l" , self.id, "reports: qty1 = " ,qty, "\n", "qty2 = ",qty2)
                message = can.Message(arbitration_id=123, is_extended_id=False,
                      data=[self.gateid,self.id, 0xFF])                                            #gives feedback on task completion             
                self.bus.send(message,timeout=None)
                NS = states[0]