class board:
    grid_length = 0
    grid_width = 0
    board_array=[]
    
    def __init__(self,length,width):
        self.board_array=[]
        self.grid_length = length
        self.grid_width = width
        
        
        for i in range(self.grid_width):
            self.board_array.append([])
            for j in range (self.grid_length):
                self.board_array[i].append('')

    def check_in_board(self,x,y):
        
        if (x<=self.grid_length) and (y<=self.grid_width):
            return True
        else:
            return False
    def insert(self,x,y,content):
        self.board_array[x-1][y-1] = content