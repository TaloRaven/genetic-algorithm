
from statistics import mean
from unittest import result
from Modules import *

import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from utils import takesecond


def genetic_algorithm( file_name: str,
    base_pop,
    max_generation,
    tournament_pop,
    k_participants,
    chance_to_pmx,
    chance_to_mutate,
    tracking=None,
    plot_results=False):

    '''
    A genetic algorithm that tries to find the shortest path in a TSP problem, input is triangle matrix of 


    '''
    start=datetime.now()  
    
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
    nuke_count=0
    t=0
    # exploatation=0
    # saved_pop=[]
    m1=Matrix(file_name).txt_to_matrix()
    pop=BasePop(m1,base_pop).n_pop()
    r1=Rate(pop,m1).rate()

    while not t==max_generation:
        
        # if t > max_generation*0.75:
        #     pop=RouletteSelection(1000,r1).roll()
        #     pop=PMX(pop,0.95).c1_c2_pmx()
        #     pop=MutationExchange(pop,0.05).mutation()
        # else:
        pop=TournamentSelection(k_participants,tournament_pop,r1).sellect_winners()
        pop=PMX(pop,chance_to_pmx).c1_c2_pmx()
        pop=MutationExchange(pop,chance_to_mutate).mutation()
        # pop, last_nuke, nuke_count =MutationBomb(t,distatnces_min,max_generation,pop,last_nuke, nuke_count).bomb()
        r1=Rate(pop,m1).rate()
        rates=[y[1] for y in r1]

        ## Save Results
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

        ## Tracking algorithm progress              
        if tracking==None:
            t=t+1
            continue        
        
        elif t%tracking!=0:
            
            t=t+1
        else:
            print('Gen: {}, with best score: {}'.format(t,min(rates)))
            t=t+1

###########################  Best Result  ##############################

    rates=[y[1] for y in best_indiwiduals]

    for index, x in enumerate(rates):
        if x==min(rates):
            result=best_indiwiduals[index]
        else:
            continue


    print(f'''\n
----------------------------------------------------------------------------
----------------------------------------------------------------------------\n
Mutatuion: {chance_to_mutate}, Crossover: {chance_to_pmx},
k_participants: {k_participants}, Population: {tournament_pop},
Max_generation: {max_generation}, RunTime: {datetime.now()-start},
Nuke Count: {nuke_count}, Best rate {result[1]}   

''')

    print("-".join(map(str,result[0])), result[1])

 
    # result={
    #     'Raod': result[0],
    #     'Score': result[1],
    #     'chance_to_mutate': chance_to_mutate,
    #     'chance_to_pmx': chance_to_pmx,
    #     'k_participants': k_participants,
    #     'tournament_pop': tournament_pop,
    #     'max_generation':  max_generation,
    #     'nuke_count': nuke_count
    # }

    ## Save best result with parameters used 
    result=[result[0],result[1],
        ('chance_to_mutate',chance_to_mutate),
        ('chance_to_pmx',chance_to_pmx),
        ('k_participants',k_participants),
        ('tournament_pop',tournament_pop),
        ('max_generation', max_generation),
        ('nuke_count', nuke_count)]

###########################   Plot   #################################
    if plot_results==True:
        plt.title(f'''peak: {distatnces_peak[-1]}, chance_to_mutate, {chance_to_mutate},chance_to_pmx, {chance_to_pmx}, k_participants, {k_participants} \n
        tournament_pop,{tournament_pop}, max_generation {max_generation} ''')
        plt.plot(generations, distatnces_max, color='r', alpha=0.1)
        plt.plot(generations, distatnces_avg, color='orange', alpha=0.8)
        plt.plot(generations, distatnces_min, color='b')
        plt.plot(generations, distatnces_peak, color='green', linewidth=2)
        # plt.hlines(y = 8000, xmin = 0, xmax = max_generation, color ='r')
        # plt.vlines(x = (max_generation*0.7), ymin = -1000, ymax = 1000, color ='r')
        plt.ylabel('Distance')
        plt.xlabel('t-generations')
        plt.legend(['max', 'avg','min_for_t','peak_all_time'], loc='upper right')
        plt.show()

    return result

