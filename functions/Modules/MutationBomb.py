from Modules.MutationExchange import MutationExchange

class MutationBomb(MutationExchange):
    def __init__(self,t,distatnces_min, pop,last_nuke, nuke_count):
        self.t=t
        self.distances_min=distatnces_min
        self.pop=pop
        self.last_nuke=last_nuke
        self.nuke_count=nuke_count
    
    def bomb(self):
            self.last_nuke+=1
            if self.t>200:
                if self.last_nuke>500:
                    t_10_proc=self.t-int(self.t*0.1)
                    roznica=self.distances_min[-1]-self.distances_min[t_10_proc]

                    if roznica == 0:
                        #print(f'NUKE !!,ostatni{distatnces_min[-1]}, -10 %{distatnces_min[t_10_proc]}  roznica:{roznica}, t, {t}, 10% {t_10_proc} ')
                        for _ in range(1):
                            self.pop=MutationExchange(self.pop,1).mutation()
                        self.last_nuke=0
                        self.nuke_count+=1
                           
                    else:
                        pass

            return self.pop, self.last_nuke, self.nuke_count