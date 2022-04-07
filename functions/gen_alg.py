
from statistics import mean
from unittest import result
from Modules.BasePop import *
from Modules.Matrix import *
from Modules.TournamentSelection import *
from Modules.Pairindividuals import *
from Modules.PMX import *
from Modules.Rate import *
from Modules.MutationExchange import MutationExchange
from Modules.RouletteSelection import *
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime




def gen_alg( file_name: str,base_pop, max_generation,
    tournament_pop,
    k_participants,
    chance_to_pmx,
    chance_to_mutate,
    # tracking=10000,
    plot_results=False):

    '''
    A genetic algorithm that tries to find the shortest path in a TSP problem

    '''
    ########################### Lists for Results ##############################
    result=[]
    generations=[]
    distatnces_max=[]
    distatnces_min=[]
    distatnces_avg=[]
    distatnces_peak=[]
    best_indiwiduals=[]

    ########################### Algorithm ##############################
    last_nuke=0
    t=0
    m1=Matrix(file_name).txt_to_matrix()
    b1=BasePop(m1,base_pop).n_pop()
    r1=Rate(b1,m1).rate()

    while not t==max_generation:
        # if t > 5000:
        #     pop=RouletteSelection(100,r1).roll()
        # else:
        pop=TournamentSelection(k_participants,tournament_pop,r1).sellect_winners()
        pop=PMX(pop,chance_to_pmx).c1_c2_pmx()
        pop=MutationExchange(pop,chance_to_mutate).mutation()
        # pop, last_nuke=nuke(t,distatnces_min, pop,last_nuke)
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
        t=t+1
         
        ## Tracking  Progress per x generations        
        # if t%tracking!=0:
        #     t=t+1
        # else:
        #     print('Gen: {}, with best score: {}'.format(t,min(rates)))
        #     t=t+1

###########################  Best Result  ##############################

    rates=[y[1] for y in best_indiwiduals]
    for index, x in enumerate(rates):
        if x==min(rates):
            result=best_indiwiduals[index]
        else:
            continue

    # print('\n Last generation {}'.format(t))
    print(f'''\n
Mutatuion: {chance_to_mutate},Crossover: {chance_to_pmx},k_participants: {k_participants},Population: {tournament_pop},Max_generation: {max_generation},
Best rate {result[1]}''')


    print("-".join(map(str,result[0])), result[1])

    result=[result[0],result[1],chance_to_mutate,chance_to_pmx,k_participants,tournament_pop,max_generation]
###########################   Plots   #################################
    if plot_results==True:
        plt.plot(generations, distatnces_max, color='r', alpha=0.1)
        plt.plot(generations, distatnces_avg, color='orange', alpha=0.8)
        plt.plot(generations, distatnces_min, color='b')
        plt.plot(generations, distatnces_peak, color='green', linewidth=2)

        plt.show()

    return result

def takeSecond(elem):
    return elem[1]


def testing():
    results12=[]
    # for _ in range(30):
    #     results.append(gen_alg('berlin52'))
    chance_to_pmx_range=[x/100 for x in range(65,96,5)]
    chance_to_mutate_range=[x/100 for x in range(4,19,2)]
    k_participants_range=[2,3]
    tournament_pop_range=[x for x in range(100,1501,100)]
    max_generation_range=[x for x in range(1000,15000,1000)]

    for chance_to_mutate in chance_to_mutate_range:
        for chance_to_pmx in chance_to_pmx_range:
            for k_participants in k_participants_range:
                for tournament_pop in tournament_pop_range:
                    for max_generation in max_generation_range:
                        result11=gen_alg('berlin52', base_pop=200,
                                                    max_generation=max_generation,
                                                    tournament_pop=tournament_pop,
                                                    k_participants=k_participants,
                                                    chance_to_pmx=chance_to_pmx,
                                                    chance_to_mutate=chance_to_mutate)                           
                        results12.append(result11)

                    
    results12.sort(key=takeSecond)

    print(f'\n############## Final Results ############\n')
    for x in results12:
        print("-".join(map(str,x[0])), x[1])

    print(f'\n############## Top Result   ############\n')
    print([print(x) for x in results12[0]])
    print("-".join(map(str,results12[0][0])), results12[0][1])

testing()