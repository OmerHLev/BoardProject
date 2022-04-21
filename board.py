import numpy as np

class board:
    grid_length = 0
    grid_width = 0
    board_array=[]
    
    def __init__(self,length,width):
        self.board_array = np.zeros(length * width,dtype=object).reshape((length,width))
        self.grid_length = length
        self.grid_width = width
        for i in range (self.grid_length):
            for j in range (self.grid_width):

                if self.board_array[(i,j)] ==0: #board array is initialized to be all zeros
                    self.board_array[(i,j)]='E' #E for Empty
        

    def check_in_board(self,x,y):
        
        if (x<=self.grid_length) and (y<=self.grid_width):
            return True
        else:
            return False

    def insert(self,x,y,content):
        self.board_array[x-1][y-1] = content # -1 to convert user input values to array compatable

    def print_board_state(self):
        print(self.board_array)