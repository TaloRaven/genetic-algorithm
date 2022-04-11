from Modules.MutationExchange import MutationExchange

class MutationBomb(MutationExchange):
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
            if self.max_generation*0.10 <= self.t:
                # if self.last_nuke> 750:   #self.max_generation*0.05:
                    t_5_proc=self.t-int(self.t*0.05)
                    t_10_proc=self.t-int(self.t*0.1)
                    t_20_proc=self.t-int(self.t*0.20)
                    t_30_proc=self.t-int(self.t*0.30)

                    roznica5=self.distances_min[-1]-self.distances_min[t_5_proc]
                    roznica10=self.distances_min[-1]-self.distances_min[t_10_proc]
                    roznica20=self.distances_min[-1]-self.distances_min[t_20_proc]
                    roznica30=self.distances_min[-1]-self.distances_min[t_30_proc]

                    if roznica20 == 0:
                        # self.saved_pop.append((self.pop,self.distances_min[-1]))
                        for _ in range(25):
                            self.pop=MutationExchange(self.pop,1).mutation()
                        self.last_nuke=0
                        self.nuke_count+=1
                        # print('lvl2')
                    # elif roznica10 == 0:
                    #     # self.saved_pop.append((self.pop,self.distances_min[-1]))
                    #     for _ in range(15):
                    #         self.pop=MutationExchange(self.pop,1).mutation()
                    #     self.last_nuke=0
                    #     self.nuke_count+=1
                    #     print('lvl1')
                    # elif roznica10 == 0:
                    #     #print(f'NUKE !!,ostatni{distatnces_min[-1]}, -10 %{distatnces_min[t_10_proc]}  roznica:{roznica}, t, {t}, 10% {t_10_proc} ')
                    #     for _ in range(10):
                    #         self.pop=MutationExchange(self.pop,0.5).mutation()

                    #     self.last_nuke=0
                    #     self.nuke_count+=1
                    #     print('Nuke lvl1')   
                    else:
                        pass

            return self.pop, self.last_nuke, self.nuke_count