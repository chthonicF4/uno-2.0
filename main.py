import threading
import socket
import random
from classes import *
import pickle
global sndr
sndr = sender()

def setup(players) :
    gameState = game()
    gameState.players = players
    gameState.gendeck()
    gameState.handOutCards()
    gameState.discard.append(gameState.deck.pop(0))
    return gameState

def sendMsg(conn,msg) :
    sndr.sendMsg(conn,msg)
    return

def recvMsg(conn) :
    msg = conn.recv(1024)
    if msg != None :
        try :
            return pickle.loads(msg) 
        except :
            print("load error")
    else :
        return

def server(HOST,PORT,numPlayer):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        players = []
        while len(players) != numPlayer :
            s.listen()
            conn , addr = s.accept()
            msg = recvMsg(conn)
            newPlayer = player(msg,[],addr,conn)
            players.append(newPlayer)
            clientThread = threading.Thread(target=clientHandle,args=(newPlayer,))
            clientThread.start()
            newPlayer = None
            print("connected by",addr)
        print("max players reached")
        #----- start ------
        global gameVar
        gameVar = setup(players)
        gameVar.show()
        print("updating")
        update(gameVar)


def update(gameVar) :
    for index,player in enumerate(gameVar.players) :
        # 1 : turn ,2 : hand ,3 : list of hand sizes ,4: discard pile top card ,5 : player index
        msg = [gameVar.turn,player.hand,gameVar.playerHands(),gameVar.discard[0],index]
        sendMsg(player.conn,msg)
        pass
        


        

def clientHandle(player) :
    global gameVar
    print("handle started for",player.nick)
    while True :
        r = True
        try:
            coppy = gameVar
        except:
            r = False
        if r == True :
            break
    while True :
        while coppy == gameVar :
            pass
        print("updating")

    pass

def client(HOST="127.0.0.1",PORT=None):
    nickname  = str(input("nickname >>"))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        sendMsg(s,nickname)
    # ------ main loop ------
        while True :
            msg = recvMsg(s)
            if msg != None :
                print(msg)
            pass

    pass

def host() :
    numofplayers = int(input("number of players(2-4) >>"))
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = random.randint(49152,65535)
    print("room :",HOST,PORT)
    host = threading.Thread(target=server,args=(HOST,PORT,numofplayers,))
    host.start()
    client(HOST,PORT)

def join() :
    HOST = str(input("host >>"))
    if HOST == "l" :
        HOST == "127.0.0.1"
    PORT = int(input("host's port>>"))
    client(PORT=PORT,HOST=HOST)
    pass

def connType():
    try:
        choice = str(input("host(h) or join(j) >>"))
    except:
        print("invalid input")
        connType()
        return
    if choice == "h" :
        host()
    elif choice == "j" :
        join()
    else :
        print("invalid choice")
        connType()
        return

connType()