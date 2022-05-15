from Modules.Mutation import Mutation

class MutationBomb(Mutation):
    """
    Rapid, cyclicall mutliple mutation that helps algorithm to leave local optimum with hard reshuffle

    Atributes:
    t: int
        Current generation 
    distance_min: int
        Best fitness in t- generation 
    max_generations: int
        Max number of t- generations
    pop: list
        Table of population 
    last_nuke: int
        number of t-generations that last bomb emerged 
    nuke_count: int
        Number of bombs triggered

    """

    def __init__(self,t: int,distatnces_min: int,max_generation: int ,
     pop: list ,last_nuke: int, nuke_count: int):
        self.t=t
        self.distances_min=distatnces_min
        self.max_generation=max_generation
        self.pop=pop
        self.last_nuke=last_nuke
        self.nuke_count=nuke_count
    
    def bomb(self):
            self.last_nuke+=1
            if self.max_generation*0.05:
                if self.last_nuke> self.max_generation*0.01:
                    
                    if self.distances_min[-1]-self.distances_min[self.t-int(self.t*0.20)]== 0:
                        for _ in range(25):
                            self.pop=Mutation(self.pop,1).exchange()
                        self.last_nuke=0
                        self.nuke_count+=1
                        
            return self.pop, self.last_nuke, self.nuke_count