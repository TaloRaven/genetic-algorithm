from random import randrange, choice
class Pairindividuals():
    """
    Population preperation to crossover 

    Atributes:
    touranment_selection:
        post selection population
    crossove_chance:
        chance to croosover character in popualtion

    Methods:
    intecepts():
        declare interception points for character in population  
    pair_individuals():
        pair unique characters in population
    pair_individuals_intercepts():
        combine paired individuals with declared interceptions
    intercepts_individuals():
        intercepts combined paired inviduals
    """

    def __init__(self, turnament_selection,chance_of_crossover) -> None:
        self.turnament_selection=turnament_selection
        self.crossover=chance_of_crossover
    def intercepts(self):
        roll1=choice(range(1, len(self.turnament_selection[0])))
        roll2=choice(range(roll1, len(self.turnament_selection[0])))
        return [roll1,roll2]
        
    def createlist(self):
        return [item for item in range(0, len(self.turnament_selection))]

    def pair_individuals(self):
        indexes=self.createlist()
        pairs_pn = {}
        for p in range(len(indexes) // 2):
            pairs_pn[p+1] = (indexes.pop(randrange(len(indexes))),
                        indexes.pop(randrange(len(indexes))))
        return pairs_pn

    def pair_individuals_intercepts(self):
        pairs_pn=self.pair_individuals()
        t = self.turnament_selection

        pairs=[]
        for x in pairs_pn:
            pairs.append((t[pairs_pn[x][0]],t[pairs_pn[x][1]],self.intercepts()))
        return pairs

    def intercepts_individuals(self):
        pairs=self.pair_individuals_intercepts()
        p2=[]
        for x in range(len(pairs)):
            #P1
            p2.append([(pairs[x][0][:pairs[x][2][0]],
            pairs[x][0][pairs[x][2][0]:pairs[x][2][1]], #P1 środek
            pairs[x][0][pairs[x][2][1]:]),
            #P2
            (pairs[x][1][:pairs[x][2][0]],
            pairs[x][1][pairs[x][2][0]:pairs[x][2][1]], #P2 środek
            pairs[x][1][pairs[x][2][1]:])])      
        return p2