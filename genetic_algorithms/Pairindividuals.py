from random import randrange, choice
class Pairindividuals():

    def __init__(self, turnament_selection) -> None:
        self.turnament_selection=[x[0] for x in turnament_selection]

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

    