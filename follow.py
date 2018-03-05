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
        # make sure the right player is in the from space
        if self.matrix[fromRow, fromCol] != player:
            return False
        # make sure the space you are going to is empty
        if self.matrix[toRow,toCol] != 0:
            return False
        #detect whether or not the duck is moving diagonally or straight
        if fromRow == toRow:
            # it's movin' straight to the side
            # make sure the spaces in between are empty
            for col in range(toCol,fromCol, numpy.sign(toCol-fromCol)):
                if self.matrix[fromRow, col] != 0:
                    return False
        elif fromCol == toCol:
            # it's movin' up
            # make sure the spaces in between are empty
            for row in range(toRow,fromRow, numpy.sign(toRow-fromRow)):
                if self.matrix[row, fromCol] != 0:
                    return False
        else:
            # it's movin' diagonally
            # is it moving with slope 1
            if abs((toRow-fromRow)/(toCol-fromCol)) != 1:
                return False
            # make sure the spaces in between are empty
            # up and to the right
            if toCol-fromCol > 0 and toRow-fromRow > 0:
                col = fromCol
                for n in range(fromRow+1,toRow):
                    col += 1
                    print(str(n) + ", " + str(col))
                    if self.matrix[n,col] != 0:
                        print("1")
                        return False
            #down and to the right
            if toCol-fromCol > 0 and toRow-fromRow < 0:
                col = fromCol
                for n in range(toRow, fromRow-1):
                    col += 1
                    if self.matrix[n, col] != 0:
                        print("2")
                        return False
            #moving up and left yo duh
            if fromCol-toCol > 0 and toRow-fromRow > 0:
                col = fromCol
                for n in range(fromRow+1, toRow):
                    col -= 1
                    if self.matrix[n, col] != 0:
                        print("3")
                        return False
            #movign down and left
            if fromCol-toCol > 0 and toRow-fromRow < 0:
                col = fromCol
                for n in range(toRow, fromRow-1):
                    col -= 1
                    if self.matrix[n, col] != 0:
                        print("4")
                        return False

        return True

    def moveDuck(self, fromRow, fromCol, toRow, toCol, player):
        if not self.isMoveValid(fromRow, fromCol, toRow, toCol, player):
            return False
        self.matrix[fromRow, fromCol] = 0
        self.matrix[toRow, toCol] = player
        return True

    # return 1 if player 1 wins, 2 if player 2 wins, 0 if no player wins
    def check_win(self):
        # on the row
        for row in range(0, 5):
            # first four
            for player in range(1, 3):
                allsame = True
                for col in range(0, 4):
                    if self.matrix[row, col] != player:
                        allsame = False
                        break
                if allsame:
                    return player
            # last four
            for player in range(1, 3):
                allsame = True
                for col in range(1, 5):
                    if self.matrix[row, col] != player:
                        allsame = False
                        break
                if allsame:
                    return player
        # columns
        for col in range(0, 5):
            # first four
            for player in range(1, 3):
                allsame = True
                for row in range(0, 4):
                    if self.matrix[row, col] != player:
                        allsame = False
                        break
                if allsame:
                    return player
            # second four
            for player in range(1, 3):
                allsame = True
                for row in range(1, 5):
                    if self.matrix[row, col] != player:
                        allsame = False
                        break
                if allsame:
                    return player

        for player in range(1,3):
            # diagonal left -> right
            # main diag first four
            if [self.matrix[0, 0], self.matrix[1, 1], self.matrix[2, 2], self.matrix[3, 3]] == [player, player, player, player]:
                return player
            # main diag second four
            if [self.matrix[1, 1], self.matrix[2, 2], self.matrix[3, 3], self.matrix[4, 4]] == [player, player, player, player]:
                return player
            # lower diag
            if [self.matrix[1, 0], self.matrix[2, 1], self.matrix[3, 2], self.matrix[4, 3]] == [player, player, player, player]:
                return player
            # upper diag
            if [self.matrix[0, 1], self.matrix[1, 2], self.matrix[2, 3], self.matrix[3, 4]] == [player, player, player, player]:
                return player
            # diagonal right to left ->
            # main diagonal first four
            if [self.matrix[0, 4], self.matrix[1, 3], self.matrix[2, 2], self.matrix[3, 1]] == [player, player, player, player]:
                return player
            # main diagonal second four
            if [self.matrix[1, 3], self.matrix[2, 2], self.matrix[3, 1], self.matrix[4, 0]] == [player, player, player, player]:
                return player
            # lower diag
            if [self.matrix[0, 3], self.matrix[1, 2], self.matrix[2, 1], self.matrix[3, 0]] == [player, player, player, player]:
                return player
            # upper diag
            if [self.matrix[1, 4], self.matrix[2, 3], self.matrix[3, 2], self.matrix[4, 1]] == [player, player, player, player]:
                return player
        return 0


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
            else:
                print("move was invalid")
        return fromRow, fromColumn, toRow, toColumn

    def nextPlayer(self, player):
        if player == 1:
            return 2
        return 1

    def getRowbotMove(self, player):
        return 0,1,1,1

    def play(self):
        human_player = int(input("do you want to be player 1 or 2?"))
        self.myBoard.print()
        current_player = 1
        game_over = False
        while not game_over:
            if current_player == human_player:
                fromRow, fromColumn, toRow, toColumn = self.getHumanMove(current_player)
            else:
                fromRow, fromColumn, toRow, toColumn = self.getHumanMove(current_player)
                #fromRow, fromColumn, toRow, toColumn = self.getRowbotMove(current_player)
            if not self.myBoard.moveDuck(fromRow, fromColumn, toRow, toColumn, current_player):
                print("Move was not valid")
            else:
                print("moved from (" + str(fromRow) + "," + str(fromColumn) + ") to (" + str(toRow) + "," + str(toColumn) + ")")
                current_player = self.nextPlayer(current_player)
                self.myBoard.print()
            winner = self.myBoard.check_win()
            if winner > 0:
                print("Yeet, Player " + str(winner) + " wins and gets 2 pokedollars")
                game_over = True



myGame = Game()
myGame.play()
