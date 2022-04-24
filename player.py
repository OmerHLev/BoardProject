

class player:
    name =''
    pieces_on_board = []
    piece_types = []

    def __init__(self,player_name):  #player_name
        self.name = player_name


class tic_tac_toe_player(player):
    def __init__(self,name_input):
        self.name = name_input
        if name_input == 'X':       #dict
            self.piece_types = ['x']
        elif name_input == 'O':
            self.piece_types = ['o']
        else:
            print('Invalid tic tac toe player type')
        return

class checkers_player(player):

    def __init__(self, name_input):
        if name_input == 'Black': #dict
            self.name = name_input
            self.piece_types = ['b','kb']
        elif name_input == 'White':
            self.name = name_input
            self.piece_types = ['w','kw']
        else:
            print('Invalid checkers player type')
            return False

