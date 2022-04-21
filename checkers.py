from calendar import c
from game import game
from board import board
from player import checkers_player
import constants

class checkers(game):
    
    def __init__(self):
        self.player_number = constants.CHECKERS_PLAYER_NUM
        self.players = [checkers_player('White'),
                        checkers_player('Black')]
        self.possible_pieces = [self.players[0].piece_type,[self.players[1].piece_type]]
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
                    ,player.piece_type)
                else:
                    self.game_board.insert(j,i,player.piece_type)

                

    