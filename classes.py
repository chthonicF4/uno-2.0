class card() :
    def __init__(self,ID,colour,type):
        self.ID = ID
        self.colour = colour
        self.type = type
        self.name = str(colour+"_"+str(type))

class player():
    def __init__(self,nickname,hand,addr,conn):
        self.nick = nickname
        self.hand = hand
        self.addr = addr
        self.conn = conn

    def pickUp(self,deck) :
        self.hand.append(deck.pop(0))



class game():
    def __init__(self):
        self.discard = []
        self.deck = []
        self.players = []
        pass
    
    def gendeck(self):
        colours = ["yellow","blue","green","red"]
        types = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
        special = ["wild","wild","+4","+4"]
        IDCount = 0
        for colour in colours :
            for num in types :
                cad = card(IDCount,colour,num)
                self.deck.append(cad)
                IDCount +=1
        for type in special :
            crd = card(IDCount,"black",type)
            self.deck.append(crd)
            IDCount += 1
     
    def handOutCards(self) :
        for player in self.players :
            for x in range(7) :
                player.pickUp(self.deck)




        