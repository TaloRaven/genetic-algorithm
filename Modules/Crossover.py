    
from Modules.Pairindividuals import *
import random
from random import randint, random

class Crossover(Pairindividuals):
    def __init__(self, turnament_selection, chance_of_crossover):
        super().__init__(turnament_selection, chance_of_crossover)
        self.chance_of_crossover=chance_of_crossover
    
    
    
    
    def cx(self)->list:
        pairs=self.pair_individuals_intercepts()
        new_pop=[]
        for pair in pairs:
            p1=pair[0]
            p2=pair[1]
            if random.random() <= self.chance_of_crossover:
                c1=[]
                c2=[]
                cykl1=[]

                # chose random start for cicle 
                start_cykl=random.choice(range(0, len(p1)))
                cykl1.append(p1[start_cykl])
                cykl1.append(p2[start_cykl])

                while cykl1[0] != cykl1[-1]:
                    for  index, x in enumerate(zip(p1, p2)):
                        if x[0]==cykl1[-1]:    
                            cykl1.append(x[1])
                            break

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

    def ox(self) -> list:
        # This is an OX crossover

        pairs=self.pair()
        new_pop = []
        no_cross = []
        for x in pairs:
            if random() >= self.chance_of_crossover:
                parent1 = x[0]
                parent2 = x[1]

                first_cross_point = randint(0, len(parent1) - 2)
                second_cross_point = randint(first_cross_point + 1, len(parent1) - 1)

                parent1_middle_cross = parent1[first_cross_point:second_cross_point]
                parent2_middle_cross = parent2[first_cross_point:second_cross_point]

                substitution_elements_1 = parent1[second_cross_point:] + parent1[:first_cross_point] + parent1_middle_cross
                substitutions_elements_2 = parent2[second_cross_point:] + parent2[:first_cross_point] + parent2_middle_cross

                temp_substitution1 = []
                temp_substitution2 = []

                for i in substitution_elements_1:
                    if i not in parent2_middle_cross:
                        temp_substitution1.append(i)
                    else:
                        pass

                for i in substitutions_elements_2:
                    if i not in parent1_middle_cross:
                        temp_substitution2.append(i)
                    else:
                        pass

                crosspoint1_len = len(parent1[:first_cross_point])

                crosspoint1 = temp_substitution1[:crosspoint1_len]
                [temp_substitution1.pop(0) for _ in range(crosspoint1_len)]
                crosspoint2 = temp_substitution1

                child1 = crosspoint1 + parent2_middle_cross + crosspoint2

                crosspoint1_len = len(parent1[second_cross_point:])

                crosspoint1 = temp_substitution2[:crosspoint1_len]
                [temp_substitution2.pop(0) for _ in range(crosspoint1_len)]
                crosspoint2 = temp_substitution2

                child2 = crosspoint1 + parent1_middle_cross + crosspoint2

                new_pop.append(child1)
                new_pop.append(child2)
            else:

                no_cross.append(x[0])
                no_cross.append(x[1])

        return new_pop + no_cross

    def pmx(self)-> list:
        p2=self.pairs
        no_pmx=[]
        c1_all=[]
        c2_all=[]
        for x in p2:
            if random() <= self.chance_of_crossover:
                #perform PMX for 2 parents - > 2 childrens 
                c1=[]
                c2=[]

                for przylegajacy in [0,2]:
                    for element in x[1][przylegajacy]:
                        if element in x[0][1]:
                            zamiennik=element
                            while zamiennik in x[0][1]:
                                zamiennik = x[1][1][x[0][1].index(zamiennik)]

                            c1.append(zamiennik)
                        else:   
                            c1.append(element)
                    if przylegajacy == 0:
                        [c1.append(y) for y in x[0][1]]
                
                
                for przylegajacy in [0,2]:
                    for element in x[0][przylegajacy]:
                        if element in x[1][1]:
                            zamiennik=element
                            while zamiennik in x[1][1]:
                                zamiennik = x[0][1][x[1][1].index(zamiennik)]
                            c2.append(zamiennik)
                        else:
                            c2.append(element)
                    if przylegajacy == 0:
                        [c2.append(y) for y in x[1][1]]
                        
                c1_all.append(c1)
                c2_all.append(c2)
            else:
                # remove interceps and append both elements from pair without change to new pop ()
                no_pmx.append([item for sublist in x[0] for item in sublist])
                no_pmx.append([item for sublist in x[1] for item in sublist])


        return c1_all+c2_all+no_pmx