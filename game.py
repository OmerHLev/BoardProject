from board import board
class game:
    player_number = 0
    players = []
    game_type = ''
    game_board = 0
    current_player = 0
    current_turn = 0
    
    def __init__(self):
        pass
            
    
    def turn(self,action):
        pass
    
    def check_winner(self):
        pass
    
    def run(self):
        ended,result = self.check_winner()
        while (ended!=True):
            self.turn(input())
            ended,result = self.check_winner()
        print(result)
        return result
