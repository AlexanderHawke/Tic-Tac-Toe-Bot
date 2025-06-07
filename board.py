class board():
    def __init__(self):
        self.board = ["-" for i in range(9)]
        self.move = 0
        self.player = str(input("Do you want to play as X or O? ")).upper()
        while self.player != "X" and self.player != "O":
            self.player = str(input("Do you want to play as X or O? ")).upper()
        if self.player == "X":
            self.bot = "O"
        else: 
            self.bot = "X"

    def __str__(self):
        return self.board[0] + " " + self.board[1] + " " + self.board[2] + "\n" + \
               self.board[3] + " " + self.board[4] + " " + self.board[5] + "\n" + \
               self.board[6] + " " + self.board[7] + " " + self.board[8]
    
    def spaceEmpty(self, space):
        if self.board[space] == "-":
            return True
        return False

    def makeMove(self, player, space):
        if self.spaceEmpty(space):
            self.board[space] = player
            self.move += 1
            self.__str__()
            if self.isDraw():
                print("Draw")
                exit()
            winner = self.isWin()
            if winner != "-":
                print(winner + " won!")
                exit()
        else:
            self.makeMove(player, int(input("Please input a valid move:")))

    def isDraw(self):
        if self.move == 9 and self.isWin() == "-":
            return True
        return False
    
    def isWin(self): 
        # Returns the person who won as either "X" or "O" and if there is no winner, then it returns "-"
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != "-"):
            return self.board[1]
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != "-"):
            return self.board[4]
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != "-"):
            return self.board[7]
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != "-"):
            return self.board[1]
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != "-"):
            return self.board[2]
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != "-"):
            return self.board[3]
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != "-"):
            return self.board[1]
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != "-"):
            return self.board[7]
        else:
            return "-"
        
    def botMove(self, isMax):
        currentWinner = self.isWin()
        return currentWinner

        if isMax:
            bestScore = -int("inf")
            bestMove = 0
            self.minimax(self)

    def minimax(self, isMax):
        pass