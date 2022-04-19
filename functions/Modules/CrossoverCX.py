
from Modules.Pairindividuals import *
import random

class CX(Pairindividuals):
    def __init__(self, turnament_selection, chance_of_crossover):
        super().__init__(turnament_selection, chance_of_crossover)
        self.chance_of_crossover=chance_of_crossover

    def cx(self):
        pairs=self.pair_individuals_intercepts()
        new_pop=[]
        for pair in pairs:
            p1=pair[0]
            p2=pair[1]
            if random.random() <= self.chance_of_crossover:

                c1=[]
                c2=[]

                cykl1=[]

                # tutaj zamiast zera moge nawet dac random liczbe przez co 
                # zaczynam z innego miejsca
                # start_cykl=random.choice(range(0, len(p1)))
                # cykl1.append(p1[start_cykl])
                # cykl1.append(p2[start_cykl])

                cykl1.append(p1[0])
                cykl1.append(p2[0])


                while cykl1[0] != cykl1[-1]:
                    for  index, x in enumerate(zip(p1, p2)):
                        if x[0]==cykl1[-1]:    
                            cykl1.append(x[1])
                            break

                # zbinduj to zipem zeby jeden enumerate byl 


                for index, x in enumerate(p1):
                    if x in cykl1:
                        c1.append(x)
                    else:
                        c1.append(p2[index])

                for index, x in enumerate(p2):
                    if x in cykl1:
                        c2.append(x)
                    else:
                        c2.append(p1[index])
                new_pop.append(c1)
                new_pop.append(c2)

            else:
                new_pop.append(p1)
                new_pop.append(p2)

        return new_pop


