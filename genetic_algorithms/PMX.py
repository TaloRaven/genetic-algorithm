from genetic_algorithms.Pairindividuals import *
from random import random
class PMX(Pairindividuals):
    def __init__(self, turnament_selection, chance_of_crossover) -> None:
        super().__init__(turnament_selection, chance_of_crossover)
        self.pairs=self.intercepts_individuals()
        self.chance_of_crossover=chance_of_crossover
    def c1_pmx(self):
        p2=self.pairs
        c1_all=[]
        for x in p2:
            c1=[]
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
            c1_all.append(c1)
        return c1_all

    def c2_pmx(self):
        p2=self.pairs
        c2_all=[]
        for x in p2:
            c2=[]
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
            c2_all.append(c2)
        return c2_all

    def c1_c2_pmx(self):
        if random() < self.chance_of_crossover:
            result=self.c1_pmx()+self.c2_pmx()
        else:
            result=self.turnament_selection
        return result