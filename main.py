
from statistics import mean
from genetic_algorithms.BasePop import *
from genetic_algorithms.Matrix import *
from genetic_algorithms.TournamentSelection import *
from genetic_algorithms.Pairindividuals import *
from genetic_algorithms.PMX import *
from genetic_algorithms.Rate import *
from genetic_algorithms.MutationExchange import MutationExchange
from genetic_algorithms.RouletteSelection import *
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


########################### Parameters ########################### 
FILE_NAME='berlin52'
m1=Matrix(FILE_NAME).txt_to_matrix()
LEN_BASE_POP=5
NUM_GENERATIONS=10000
TURNAMENT_SELECTION_NUM_BRACKET=50
NUMBER_OF_PARTICIPANTS_IN_BRACKET=2
CHANCE_TO_PMX=0.65
chance_to_mutate=1/len(m1[0])+0.1

########################### Lists for Results ##############################
generations=[]
distatnces_max=[]
distatnces_min=[]
distatnces_avg=[]
distatnces_peak=[]
best_indiwiduals=[]

########################### mutbomb ##############################
def nuke(t,distatnces_min, pop,last_nuke):

    last_nuke+=1
    if t>200:
        if last_nuke>200:
            t_10_proc=t-int(t*0.1)
            roznica=distatnces_min[-1]-distatnces_min[t_10_proc]

            if roznica == 0:
                #print(f'NUKE !!,ostatni{distatnces_min[-1]}, -10 %{distatnces_min[t_10_proc]}  roznica:{roznica}, t, {t}, 10% {t_10_proc} ')
                for _ in range(15):
                    pop=MutationExchange(pop,1).mutation()
                last_nuke=0   
            else:
                pass

    return pop, last_nuke

###########################  Algorithm   #############################
def main():
    last_nuke=0
    t=0
    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,LEN_BASE_POP).n_pop()
    r1=Rate(b1,m1).rate()
    while not t==NUM_GENERATIONS:
        # if t > 5000:
        #     pop=RouletteSelection(100,r1).roll()
        # else:
        pop=TournamentSelection(NUMBER_OF_PARTICIPANTS_IN_BRACKET,TURNAMENT_SELECTION_NUM_BRACKET,r1).sellect_winners()
        pop=PMX(pop,CHANCE_TO_PMX).c1_c2_pmx()
        pop=MutationExchange(pop,chance_to_mutate).mutation()
        pop, last_nuke=nuke(t,distatnces_min, pop,last_nuke)
        r1=Rate(pop,m1).rate()
        rates=[y[1] for y in r1]


        ## Results 
        generations.append(t)
        distatnces_min.append(min(rates))
        distatnces_max.append(max(rates))
        distatnces_avg.append(mean(rates))
        distatnces_peak.append((min(distatnces_min)))

        if min(distatnces_min) >= min(rates):
            for index, x in enumerate(rates):
                if x==min(rates):
                    if r1[index] not in best_indiwiduals:
                        best_indiwiduals.append(r1[index])
                else:
                    continue
        ## Tracking  Progress per x generations        
        if t%1000==0:
            print('Gen: {}, with best score: {}'.format(t,min(rates)))
            t=t+1
        else:
            t=t+1


###########################  Best Result  ##############################

    rates=[y[1] for y in best_indiwiduals]
    for index, x in enumerate(rates):
        if x==min(rates):
            result=best_indiwiduals[index]
        else:
            continue

    print('Last generation {}'.format(t))
    print('\n Best rate \n')
    print("-".join(map(str,result[0])), result[1])

###########################   Plots   #################################
    plt.plot(generations, distatnces_max, color='r', alpha=0.1)
    plt.plot(generations, distatnces_avg, color='orange', alpha=0.8)
    plt.plot(generations, distatnces_min, color='b')
    plt.plot(generations, distatnces_peak, color='green', linewidth=2)

    plt.show()




if __name__ == "__main__":
    start=datetime.now()    
    main()
    print (f"Runtime of the program is {datetime.now()-start}")
    