from random import randint
from csv import writer
listValue = [ 0, 1, 2 ] # 0 is rock, 1 is paper, 2 is scissor
listDescription = [ "rock", "paper", "scissor" ]

def displayGameResult(player1, givenGamer1, player2, givenGamer2, givenWinner):
    if (givenGamer1 != -1) and (givenGamer2 != -1) and (givenWinner != -1):
        msg = "[" + player1.getId() + ":" + listDescription[givenGamer1] + "] vs [" + player2.getId() + ":" + listDescription[givenGamer2] + "]"
        if winner == 1:
            msg += " -> winner is " + player1.getId()
        elif winner == 2:
            msg += " -> winner is " + player2.getId()
        else:
            msg += " -> tie game"
        print(msg)
    else:
        print("Game session not ready")


# ANSWER : START
class Player:
    whatvalue = None

    def __init__(self, playerID="noname"):
        self.playerID = playerID

    def getId(self):
        return self.playerID

    def setValue(self, value):
        if value == None: self.whatvalue = randint(0,2)
        else: self.whatvalue = value # 멤버 데이터 저장이면 클래스 밖이나 생성자 안에 있어야 되지 않나...

    def getValue(self):
        return self.whatvalue # 이게 가능한지 모르겠음. 생성자 안에서 선언 안했으면 밖에서라도 선언해야하는게 아닌가 해서... 파썬에서 이해가 안되는 부분은 필드에 대한 것인듯...



class Game:
    winner = None
    gamelist = None

    def __init__(self, player1, player2, gamename):
        try:
            self.player1 = player1
            self.player2 = player2
            self.gamename = gamename
        except:
            # 게임 비정상 상태 정의. 근데 이거 어떻게 하지?!
            raise Exception("Session Error: Abnormal State")

    def runGame(self, value1 = randint(0,2), value2 = randint(0,2)):
        try:
            # decideWinner에서 실행해도 값이 당연히 변경되지 않고 잘 반환되는 구조라고 할 수 있.
            self.player1.setValue(value1)
            self.player2.setValue(value2)
            return value1, value2
        except: return (-1,-1)
            


    def decideWinner(self): # value1,2를 걍 이용
        value1, value2 = self.runGame()
        try:
            if (value1 == 0): # rock
                if(value2 == 0): # rock
                    self.winner = 0
                elif(value2 == 1): # paper
                    self.winner = 2
                else:
                    self.winner = 1
            elif (value1 == 1): # paper
                if(value2 == 0): # rock
                    self.winner = 1
                elif(value2 == 2): # scissor
                    self.winner = 2
                else:
                    self.winner = 0
            else: # scissor
                if(value2 == 0):
                    self.winner = 2
                elif(value2 == 1):
                    self.winner = 1
                else:
                    self.winner = 0
            return self.winner
        except: return -1


    def logGame(self):
        try:
            self.gamelist = [self.player1.playerID, self.player1.whatvalue, self.player2.playerID, self.player2.whatvalue, winner]
            return True
        except: return False


    def closeSession(self):
        try:
            with open("sample.csv",'w') as f:
                wr = csv.writer(f)
                wr.writerow(["sequence","player1","player1-turn","player2","player2-turn","winner"])
                wr.writerow(self.gamelist)
        except: return False
# ANSWER : END

player1 = Player("20190001")
player2 = Player("20190002")

game = Game(player1, player2, "myGame")

gamer1, gamer2 = game.runGame()
winner = game.decideWinner()
game.logGame()
displayGameResult(player1, gamer1, player2, gamer2, winner)

gamer1, gamer2 = game.runGame(listValue[0], listValue[1])
winner = game.decideWinner()
game.logGame()
displayGameResult(player1, gamer1, player2, gamer2, winner)

game.closeSession()