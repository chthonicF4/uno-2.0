class card() :
    def __init__(self,ID,colour,type):
        self.ID = ID
        self.colour = colour
        self.type = type
        self.name = str(colour+"_"+type)

class player():
    def __init__(self,nickname,hand,addr,conn):
        self.nick = nickname
        self.hand = hand
        self.addr = addr
        self.conn = conn
        pass      

class game():
    def __init__(self):
        discard = []
        deck = []
        players = []
        pass
    def gendeck(self):
        colours = ["yelllow","blue","green","red"]
        types = range(0,9)
        special = ["wild","+4"]
        
        