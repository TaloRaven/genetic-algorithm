from email.mime import base
from random import sample, choice
class TournamentSelection():
    '''
    Atributes:
    
    n: int 
        number of participants in bracket 
    k: int 
        number of tournament brackets
    basepop: list 
        1st base population chosen randomly from matrix  
    
    '''
    def __init__(self, k_participants: int, n_brackets: int,basepop: list) -> None:
        self.basepop=basepop
        self.k_participants=k_participants
        self.n_brackets=n_brackets
        
    def turnament(self):
        
        if (self.n_brackets) % 2 != 0:
            raise ValueError("Number of k- turnament bracket  must be an even number")

        turnament=[]
        for _ in range(self.n_brackets):
                bracket = sample(self.basepop, self.k_participants)
                turnament.append(bracket)
        return turnament
    
    def sellect_winners(self):
        winners=[]
        for bracket in self.turnament():
            score=[]
            for x in bracket:
                score.append(x[1])
            winner=[]
            for index, x in enumerate(score):
                if x == min(score):
                    winner.append(bracket[index])
                else:
                    continue
            if len(winner) != 1:
                winner=[choice(winner)]
            winners.append(winner)
        turnament_selection=[item for sublist in winners for item in sublist]
        return [x[0] for x in turnament_selection]