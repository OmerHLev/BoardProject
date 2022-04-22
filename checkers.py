
from game import game
from board import board
from player import checkers_player
import constants
from piece import piece

class checkers(game):
    
    def __init__(self):
        self.player_number = constants.CHECKERS_PLAYER_NUM
        self.players = [checkers_player('White'),
                        checkers_player('Black')]
        self.possible_pieces = self.players[0].piece_types+self.players[1].piece_types
        self.game_board = board(
                constants.CHECKERS_BOARD_LENGTH,
                constants.CHECKERS_BOARD_WIDTH)
        self.current_player_index = 0
        self.add_starting_pieces(self.players[0])
        self.add_starting_pieces(self.players[1])
        self.game_board.print_board_state()

    
    def add_starting_pieces(self,player):
        for i in range(constants.CHECKERS_STARTING_ROWS_NUM):
            for j in range((i%2),constants.CHECKERS_BOARD_WIDTH,2):
                if player.name == 'Black':
                    self.game_board.insert(abs(j-(constants.CHECKERS_BOARD_WIDTH-1)),
                    abs(i-(constants.CHECKERS_BOARD_LENGTH-1))
                    ,'b')
                else:
                    self.game_board.insert(j,i,'w')

    def valid_action_input(self,action):
        valid = False

        while not valid:
            if ((len(action)==4 or len(action)==5) and 
            action[0] in constants.CHECKERS_VALID_COORDS and 
            action[2] in constants.CHECKERS_VALID_COORDS and 
            action[1]==',' and
            action[3] in constants.CHECKERS_VALID_DIRECTION):
                if len(action)==5: 
                    if action[5] in constants.CHECKERS_VALID_DIRECTION:
                        valid = True
                    else:
                        print("Not a move")
                        action = input()
                else:
                    valid = True
                
            else:
                print("Not a move")
                action = input()
        return action

    def turn(self,action):
        action = self.valid_action_input(action)
        initial_x=int(action[0]) #grabbing the x value of the input
        initial_y= int(action[2]) #grabbing the y value of the input
        direction = action[3]
        backwards = False
        if len(action)==5:
            if action[5]=='B':
                backwards = True
        next_x,next_y = self.find_next_cell(initial_x,initial_y,direction,backwards)
        
        if self.check_owned_piece(self.players[self.current_player_index],initial_x,initial_y):
            if self.check_occupied(next_x,next_y) == False:
                self.game_board.insert(next_x,next_y,self.game_board.board_array[(initial_x,initial_y)])
                self.game_board.insert(initial_x,initial_y,'E')
                self.current_player_index = (self.current_player_index +1)%2
                self.current_turn +=1
            else:
                if not self.check_owned_piece(self.players[self.current_player_index],next_x,next_y):
                    jump_x,jump_y = self.find_next_cell(next_x,next_y,direction,backwards)
                    if self.check_occupied(jump_x,jump_y) == False:
                        self.game_board.insert(jump_x,jump_y,self.game_board.board_array[(initial_x,initial_y)])
                        self.game_board.insert(initial_x,initial_y,'E')
                        self.game_board.insert(next_x,next_y,'E')
                        self.current_player_index = (self.current_player_index +1)%2
                        self.current_turn +=1
                

        
    def find_next_cell(x,y,direction,backwards):
        checked_x = x
        checked_y = y
        if direction == 'L':
            if backwards== False:
                checked_y+=1
                checked_x-=1
            else:
                checked_y-=1
                checked_x-=1
        if direction == 'R':
            if backwards== False:
                checked_y+=1
                checked_x+=1
            else:
                checked_y-=1
                checked_x+=1
        return checked_x,checked_y

    def check_occupied(self,x,y):
        occupied_flag = False
        checked_x = x
        checked_y = y
        if self.check_in_bounds(checked_x,checked_y) == True:
            if self.game_board[(checked_x-1,checked_y-1)] != 'E':
                occupied_flag = True

        return occupied_flag
        

    def check_in_bounds(self,x,y):
        flag = False
        if (x in constants.CHECKERS_VALID_COORDS and
            y in constants.CHECKERS_VALID_COORDS):
            flag = True
        else:
            print("Can't move outside of board!")
        return flag
    
    def check_owned_piece(self,player,x,y):
        owned = False
        if self.game_board.board_array[(x-1,y-1)] in player.piece_types:
            owned = True
        return owned
    
    def check_winner(self):
        no_white = True
        no_black = True
        for i in range(self.game_board.grid_length):
            for j in range(self.game_board.grid_width):
                if self.game_board.board_array[(i,j)] in self.players[0].piece_types:
                    no_white = False
                if self.game_board.board_array[(i,j)] in self.players[1].piece_types:
                    no_black = False
    
