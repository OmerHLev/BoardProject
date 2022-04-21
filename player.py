from distutils.log import error
from unicodedata import name


class player:
    name =''
    pieces_on_board = []
    piece_types = []

    def __init__(self,name_input):
        self.name = name_input


class tic_tac_toe_player(player):
    def __init__(self,name_input):
        piece_types = []
        if name_input == 'X':
            self.name = name_input
            self.piece_types = ['x']
        elif name_input == 'O':
            self.name = name_input
            self.piece_types = ['o']
        else:
            print('Invalid tic tac toe player type')
            return False

class checkers_player(player):

    def __init__(self, name_input):
        if name_input == 'Black':
            self.name = name_input
            self.piece_type = 'b'
        elif name_input == 'White':
            self.name = name_input
            self.piece_type = 'w'
        else:
            print('Invalid checkers player type')
            return False
        