class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [player1_name, player2_name]
        self.scores = [0, 0]
       
    def won_point(self, player_name):
        if player_name == self.players[0]:
            self.scores[0] += 1
        elif player_name == self.players[1]:
            self.scores[1] += 1
            

    def get_score(self):
        point_names = ('Love', 'Fifteen', 'Thirty', 'Forty' )
        specials = {	(0,0): "Love-All",	(1,1): "Fifteen-All",
                        (2,2): "Thirty-All",	(3,3): "Deuce",
                        (4,4): "Deuce"	}
        
        if tuple(self.scores) in specials:
            text = specials[tuple(self.scores)]
            
        elif self.scores[0] > 3 or self.scores[1] > 3:
            if abs( self.scores[0] - self.scores[1] ) > 1:
                text = "Win for player"
            else:
                text = "Advantage player"
            text += "1" if ( self.scores[0] > self.scores[1] ) else "2"
            
        else:
            text=f"{point_names[self.scores[0]]}-{point_names[self.scores[1]]}"

        return text
