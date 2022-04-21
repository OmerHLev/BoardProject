from board import board
from game import game
from player import tic_tac_toe_player
import constants
class tic_tac_toe(game):
    pieces = []
    
    
    def __init__(self):
            self.player_number = constants.TIC_TAC_TOE_PLAYER_NUM
            self.players = [tic_tac_toe_player('X'),
                            tic_tac_toe_player('O')]
            self.pieces = [self.players[0].piece_type,[self.players[1].piece_type]]
            self.game_board = board(
                constants.TIC_TAC_TOE_BOARD_LENGTH,
                constants.TIC_TAC_TOE_BOARD_WIDTH)
            self.current_player_index = 0
    
    def turn (self,action):
        action = self.valid_action_input(action)
        x=int(action[0]) #grabbing the x value of the input
        y= int(action[2]) #grabbing the y value of the input
        
        if self.legal_move(x,y) == True:
            self.game_board.insert(x,y,
                                self.players[
                                self.current_player_index].piece_type)
            self.current_player_index = (self.current_player_index +1)%2
            self.current_turn +=1

    def valid_action_input(self,action):
        valid = False

        while not valid:
            if (len(action)==3 and 
            action[0] in constants.TIC_TAC_TOE_VALID_ACTIONS_INPUT and 
            action[2] in constants.TIC_TAC_TOE_VALID_ACTIONS_INPUT and 
            action[1]==','):
                valid = True
            else:
                print("Not a move")
                action = input()
        return action

            
    def legal_move(self,x,y):
        if self.game_board.check_in_board(x,y) == True:
            if self.game_board.board_array[x-1][y-1] =='E':
                return True
            else:
                print('Space already taken!')
                return False
        else:
            print('out of board bounds!')
            return False
            
    def check_winner(self):
        h = self.check_horizontal()
        d1 = self.check_diagonal_1()
        d2 = self.check_diagonal_2()
        v = self.check_vertical()
        for i in self.pieces:
            if i in [h,d1,d2,v]:
                return True,i
        if self.current_turn == 9:
            return True,'Tie'
        
        else:
            return False,'none'
                
    
    def check_horizontal(self):
        for i in range (self.game_board.grid_length):
            y=i
            x=0
            base = self.game_board.board_array[x][y]
            cell = self.game_board.board_array[x][y]
            for j in range(self.game_board.grid_width):
                if (cell in self.pieces) and (cell == base):
                    if j == self.game_board.grid_width-1:
                        return base
                    else:
                        x=j+1
                        cell = self.game_board.board_array[x][y]
                        
                else:
                    break

        return False
        
        
    def check_vertical(self):
        for i in range (self.game_board.grid_width):
            y=0
            x=i
            base = self.game_board.board_array[x][y]
            cell = self.game_board.board_array[x][y]
            for j in range(self.game_board.grid_length):
                if (cell in self.pieces) and (cell == base):
                    if j == self.game_board.grid_width-1:
                        return base
                    else:
                        y=j+1
                        cell = self.game_board.board_array[x][y]
                    
                else:
                    break
               
        return False
    
    def check_diagonal_1(self):
        x=0
        y=0
        base = self.game_board.board_array[x][y]
        cell = self.game_board.board_array[x][y]
        for i in range(self.game_board.grid_length):
            if (cell in self.pieces) and (cell == base):
                if i == self.game_board.grid_width-1:
                        return base
                else:
                    x=i+1
                    y=i+1
                    cell = self.game_board.board_array[x][y]
            else:
                return False
        return base
    def check_diagonal_2(self):
        x=0
        y=2
        base = self.game_board.board_array[x][y]
        cell = self.game_board.board_array[x][y]
        for i in range(self.game_board.grid_length):
            if (cell in self.pieces) and (cell == base):
                if i == self.game_board.grid_width-1:
                        return base
                else:
                    x=i+1
                    y=abs(i-1)
                    cell = self.game_board.board_array[x][y]
            else:
                return False
        return base