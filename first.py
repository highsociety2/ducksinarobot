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

myBoard = Board()
myBoard.startingposition()
myBoard.print()

