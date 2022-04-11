from Modules.Pairindividuals import *
from random import random
class PMX(Pairindividuals):
    """
    PMX crossocer of population
    Atributes: 
    pairs: list
        with Pairinvidualst.intercepts_inviuals prepeared population to corssover 
    chance_of_crossover: int
        chance to crossover paired inviduals

    Methods:
        c1_pmx(), c2_pmx()
    cross over for first/secound paired  invidual
        c1_cw_pmx()
    chance to crossover population 


    """
    def __init__(self, turnament_selection, chance_of_crossover) -> None:
        super().__init__(turnament_selection, chance_of_crossover)
        self.pairs=self.intercepts_individuals()
        self.chance_of_crossover=chance_of_crossover
        self.turnament_selection=turnament_selection

    # def c1_pmx(self):
    #     p2=self.pairs
    #     print('c1')
    #     print(p2)
    #     c1_all=[]
    #     c2_all=[]
    #     for x in p2:
    #         if random() >= self.chance_of_crossover:
    #             c1=[]
    #             for przylegajacy in [0,2]:
    #                 for element in x[1][przylegajacy]:
    #                     if element in x[0][1]:
    #                         zamiennik=element
    #                         while zamiennik in x[0][1]:
    #                             zamiennik = x[1][1][x[0][1].index(zamiennik)]

    #                         c1.append(zamiennik)
    #                     else:   
    #                         c1.append(element)
    #                 if przylegajacy == 0:
    #                     [c1.append(y) for y in x[0][1]]
    #             c1_all.append(c1)
    #             c2=[]
    #             for przylegajacy in [0,2]:
    #                 for element in x[0][przylegajacy]:
    #                     if element in x[1][1]:
    #                         zamiennik=element
    #                         while zamiennik in x[1][1]:
    #                             zamiennik = x[0][1][x[1][1].index(zamiennik)]
    #                         c2.append(zamiennik)
    #                     else:
    #                         c2.append(element)
    #                 if przylegajacy == 0:
    #                     [c2.append(y) for y in x[1][1]]
    #             c2_all.append(c2)
    #         else:
    #             print('ni ma ')

    #     return c1_all+c2_all

    # def c2_pmx(self):
    #     p2=self.pairs
    #     print('c2')
    #     print(p2)
    #     c2_all=[]
    #     for x in p2:
    #         c2=[]
    #         for przylegajacy in [0,2]:
    #             for element in x[0][przylegajacy]:
    #                 if element in x[1][1]:
    #                     zamiennik=element
    #                     while zamiennik in x[1][1]:
    #                         zamiennik = x[0][1][x[1][1].index(zamiennik)]
    #                     c2.append(zamiennik)
    #                 else:
    #                     c2.append(element)
    #             if przylegajacy == 0:
    #                 [c2.append(y) for y in x[1][1]]
    #         c2_all.append(c2)
    #     return c2_all

    # def c1_c2_pmx(self):
    #     result=self.c1_pmx()+self.c2_pmx()
    #     result=self.c1_pmx()+self.c2_pmx()


    #     if random() < self.chance_of_crossover:
    #         result=self.c1_pmx()+self.c2_pmx()
    #     else:
    #         result=self.turnament_selection
    #     return result

    def c1_c2_pmx(self):
        p2=self.pairs
        no_pmx=[]
        c1_all=[]
        c2_all=[]
        for x in p2:
            
            if random() >= self.chance_of_crossover:
                #perform PMX for 2 parents - > 2 childrens 
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
            else:
                # remove interceps and append both elements from pair without change to new pop ()
                no_pmx.append([item for sublist in x[0] for item in sublist])
                no_pmx.append([item for sublist in x[1] for item in sublist])


        return c1_all+c2_all+no_pmx