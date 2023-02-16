#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------


class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |     
        print("   "+"0   "+"1   "+"2   ") 
        for each_row in range(0,len(self.board)):
            print("",each_row, end=" ")
            for each_column in range(0,len(self.board)):
                if each_column < len(self.board) - 1:
                    if self.board[each_row][each_column] == 0:
                        print("   "+"|",end = "") 
                    else:
                        print("",self.board[each_row][each_column],""+"|",end = "")
                else:
                    if self.board[each_row][each_column] == 0:
                        print("   ",)
                    else:
                        print("",self.board[each_row][each_column],"")
            if each_row < len(self.board) - 1:
                print("   "+"-"*11)      


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        get_status = self.squareIsEmpty(row,col)
        if get_status == True:
            self.board[row][col] = num
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        for each_row  in range(len(self.board)):
            for each_column in range(len(self.board)):
                if self.board[each_row][each_column] == 0:
                    return False
        return True        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # each horizontal row.
        for each_row  in range(len(self.board)):
            sum = 0
            for each_column in range(len(self.board)):
                sum = sum + self.board[each_row][each_column]
                if sum == 15:
                    return True

        # each vertical row.
        for each_row  in range(len(self.board)):
            sum = 0
            for each_column in range(len(self.board)):
                sum = sum + self.board[each_column][each_row]
                if sum == 15:
                    return True

            
        
        # right diagonal
        sum = 0
        for each_element  in range(len(self.board)):
            sum = sum + self.board[each_element][each_element]
            if sum == 15:
                return True
        
        # left diagonal
        sum = 0
        for each_element in range(len(self.board)):
            sum = sum + self.board[each_element][len(self.board)-1-each_element]
            if sum == 15:
                return True
        
        return False
    
    def check_number(self):
        '''
        Checks whether the number entered is an integer number or not
        Inputs:none
        Returns:integer number
        '''
        continue_looping = False
        while not continue_looping:
            try:
                get_input = int(input())
            except:
                print("Please enter an integer number: ",end="")
            else:
                continue_looping = True
        return get_input

     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    board = myBoard.board
    print(board[2][2])
    print(board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    # try to assign a number to a non-empty square. What happens?
    # check if the board has a winner. Should there be a winner after only 1 entry?
    # check if the board is full. Should it be full after only 1 entry?
    # add values to the board so that any line adds up to 15. Display
    # check if the board has a winner
    # check if the board is full
    # write additional tests, as needed
    game_over = False
    append_item = 0
    while not game_over:
        continue_looping = False
        while not continue_looping:
            print("Please enter a row: ",end="")
            get_row_input = myBoard.check_number()
            print("Please enter a column: ",end="")
            get_column_input = myBoard.check_number()
            print("Please enter a number(1-9): ",end="")
            get_number = myBoard.check_number()
            if (get_row_input >= 0 and get_row_input < 3) and (get_column_input >= 0 and get_column_input < 3) and (get_number > 0 and get_number < 10):
                continue_looping = True
        myBoard.update(get_row_input,get_column_input,get_number)
        if myBoard.isWinner():
            print("There is a winner")
            game_over = True
        if myBoard.boardFull():
            print("The game is a tie.")
            game_over = True
        myBoard.drawBoard()

    




    