import numpy

class Board:
    def __init__(self):
        # init is a function that runs whenever a new "board" is created
        self.matrix=numpy.zeros([5, 5], dtype=int)
        #Creating a 5by 5 matrix of 0s
    def startingposition(self):
        #this function puts all the ducks in their proper places
        #adding self as a parameter makes it so that anything that happens in the method applies to a single board
        self.matrix[0, 0] = 1
        #1 represents green
        self.matrix[0, 1] = 2
        #2 represents orange
        self.matrix[0, 2] = 1
        self.matrix[0, 3] = 2
        self.matrix[0, 4] = 1
        self.matrix[1, 0] = 0
        #zero represents absence of ducks!
        self.matrix[1, 1] = 0
        self.matrix[1, 2] = 0
        self.matrix[1, 3] = 0
        self.matrix[1, 4] = 0
        self.matrix[2, 0] = 1
        self.matrix[2, 1] = 0
        self.matrix[2, 2] = 0
        self.matrix[2, 3] = 0
        self.matrix[2, 4] = 2
        self.matrix[3, 0] = 0
        self.matrix[3, 1] = 0
        self.matrix[3, 2] = 0
        self.matrix[3, 3] = 0
        self.matrix[3, 4] = 0
        self.matrix[4, 0] = 2
        self.matrix[4, 1] = 1
        self.matrix[4, 2] = 2
        self.matrix[4, 3] = 1
        self.matrix[4, 4] = 2
    def print(self):
        print(self.matrix)

    def isMoveValid(self, fromRow, fromCol, toRow, toCol, player):
        #TODO implement this
        return True

    def moveDuck(self, fromRow, fromCol, toRow, toCol, player):
        if not self.isMoveValid(fromRow, fromCol, toRow, toCol, player):
            return False
        self.matrix[fromRow, fromCol] = 0
        self.matrix[toRow, toCol] = player
        return True


class Game:
    def __init__(self):
        self.myBoard = Board()
        self.myBoard.startingposition()

    def getHumanMove(self, player):
        possible = False
        while not possible:
            fromRow = int(input("Row of duck you want to move:"))
            fromColumn = int(input("Column of duck you want to move:"))
            if self.myBoard.matrix[fromRow, fromColumn] == player:
                possible = True
            else:
                print("You don't have a duck in that square")
        possible = False
        while not possible:
            toRow = int(input("Desired row you want to move that duck to:"))
            toColumn = int(input("Desired column you want to move that duck to"))
            if self.myBoard.matrix[toRow, toColumn] == 0:
                possible = True
        return fromRow, fromColumn, toRow, toColumn

    def nextPlayer(self, player):
        if player == 1:
            return 2
        return 1

    def getRowbotMove(self, player):
        return 0,1,0,0

    def play(self):
        human_player = int(input("do you want to be player 1 or 2?"))
        self.myBoard.print()
        current_player = 1
        game_over = False
        while not game_over:
            if current_player == human_player:
                fromRow, fromColumn, toRow, toColumn = self.getHumanMove(current_player)
            else:
                fromRow, fromColumn, toRow, toColumn = self.getRowbotMove(current_player)
            if not self.myBoard.moveDuck(fromRow, fromColumn, toRow, toColumn, current_player):
                print("Move was not valid")
            else:
                current_player = self.nextPlayer(current_player)
                self.myBoard.print()


myGame = Game()
myGame.play()