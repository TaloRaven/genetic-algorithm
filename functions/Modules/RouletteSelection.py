from random import sample, choice,random

class RouletteSelection():
    '''
    Atributes:
    
    n: int 
        number of spins/number of new population
    basepop: list 
        1st base population chosen randomly from matrix  
    
    '''
    def __init__(self, n_spin: int, basepop: list):
        self.n_spin=n_spin
        self.basepop=basepop
    
    def reverse_rating(self):
        max1=max([x[1] for x in self.basepop])
        for x in self.basepop:
            x[1]=max1+1-x[1]
        return self.basepop

    def chance_range(self):
        rev1=self.reverse_rating()
        element=0
        for index, x in enumerate(rev1):
            if index == 0:
                element=element+x[1]
                x.append((0, element-1))
            elif index==len(rev1)-1:
                x.append((element,element+x[1]+1))
                element=element+x[1]
            else:
                x.append((element,element+x[1]))
                element=element+x[1]

        return rev1

    def roll(self):
    
        new_pop=[]
        rev1=self.chance_range()
        suma=rev1[-1][-1][-1]

        for _ in range(self.n_spin):
            num_roll = choice(range(0,suma))
            for index, x in enumerate(rev1):
                if x[-1][0] <= num_roll <= x[-1][1]:
                    new_pop.append(rev1[index][0])
                    break
                else:
                    continue
                    
        return  new_pop