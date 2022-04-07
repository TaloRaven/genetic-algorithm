from Modules.MutationExchange import MutationExchange

class MutationBomb(MutationExchange):
    def __init__(self,t,distatnces_min, pop,last_nuke):
        self.t=t
        self.distances_min=distatnces_min
        self.pop=pop
        self.last_nuke=last_nuke
    
    def bomb(self):
            last_nuke+=1
            if self.t>200:
                if last_nuke>200:
                    t_10_proc=self.t-int(self.t*0.1)
                    roznica=self.distatnces_min[-1]-self.distatnces_min[t_10_proc]

                    if roznica == 0:
                        #print(f'NUKE !!,ostatni{distatnces_min[-1]}, -10 %{distatnces_min[t_10_proc]}  roznica:{roznica}, t, {t}, 10% {t_10_proc} ')
                        for _ in range(15):
                            pop=MutationExchange(pop,1).mutation()
                        last_nuke=0   
                    else:
                        pass

            return pop, last_nuke