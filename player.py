from distutils.log import error
from unicodedata import name


class player:
    name =''
    pieces_on_board = []
    piece_type = ''

    def __init__(self,name_input):
        self.name = name_input


class tic_tac_toe_player(player):
    def __init__(self,name_input):
        if name_input == 'X':
            self.name = name_input
            self.piece_type = 'x'
        elif name_input == 'O':
            self.name = name_input
            self.piece_type = 'o'
        else:
            print('Invalid tic tac toe player type')
            return False