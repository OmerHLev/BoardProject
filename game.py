from board import board
class game:
    player_number = 0
    players = []
    game_board = 0
    current_player_index = 0
    current_turn = 0
    possible_pieces = []  # pieces_types
    
    def __init__(self):
        pass
            
    
    def turn(self,action):
        pass
    
    def check_winner(self):
        pass
    
    def run(self):
        ended,result = self.check_winner()
        while (ended!=True):
            self.game_board.print_board_state()
            self.turn(input())
            ended,result = self.check_winner()
        print(result)
        return
