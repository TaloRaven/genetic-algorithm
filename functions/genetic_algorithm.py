
from statistics import mean
from Modules import *
from Modules.CrossoverPMX import PMX
from Modules.CrossoverOX import OX
from Modules.CrossoverCX import CX

import json
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from utils import *

import os




def genetic_algorithm(  file_name: str,
                        base_pop=100,
                        max_generation=100,
                        tournament_pop=20,
                        k_participants=2,
                        chance_to_pmx=0.96,
                        chance_to_mutate=0.001,
                        start_roulete=0.9,
                        tracking=None,
                        plot_results=False,
                        save_results=False
                    ):

    '''
    A genetic algorithm that tries to find the shortest path in a TSP problem.

    Parameters: 
    file_name: str
        Name of TSP problem in form of triangular matrix in txt format 
    base_pop: int
        base pop randomly selected from matrix 
    max_generation: int
        max number of generations, stop condidtion
    tournament_pop: int
        Population, (number of brackets in tournamnet) 
    k_participants: int
        number of praticipants in one bracket of a tournament
    chance_to_pmx: float (0:1)
        Propability of crossover pair of parents into pair of children  
    chance_to_mutate: float(0:1)
        Propability of mutation invidual
    tracing: int
        Shows results every   
    plot_results: bool
        if True plot shows  progresion of finding optimal path by algorithm 
    save_results: bool
        if True saves algorithm output in json file  

    returns: dict
        stored progress with parameters 
        result_dict={}

    '''
    start=datetime.now()  

    ## List of results 
    result=[]
    distatnces_max=[]
    distatnces_min=[]
    distatnces_avg=[]
    distatnces_peak=[]
    best_indiwiduals=[]


    ############################################# Algorithm 
    last_nuke=0
    nuke_count=0
    t=0
    m1=Matrix(file_name).txt_to_matrix()
    pop=BasePop(m1,base_pop).n_pop()
    r1=Rate(pop,m1).rate()

    while not t==max_generation :
        # cROSS OVER START 
        # chance_to_mutate=t/max_generation
        # chance_to_pmx=1-t/max_generation
        
        #MUTATION START 
        chance_to_mutate=1-t/max_generation
        chance_to_pmx=t/max_generation
        
        #MUTATION START 
        # chance_to_mutate=0.8-t/max_generation*0.85
        # chance_to_pmx=t/max_generation+0.05*max_generation


        if t < max_generation*start_roulete:
            pop=TournamentSelection(k_participants,tournament_pop,r1).sellect_winners()
            # pop=RouletteSelection(tournament_pop,r1).roll()
            # pop=PMX(pop,chance_to_pmx).c1_c2_pmx()
            pop=CX(pop,chance_to_pmx).cx()
            # pop=OX(pop,chance_to_pmx).ox()
            pop=Mutation(pop,chance_to_mutate).exchange()
            # pop, last_nuke, nuke_count =MutationBomb(t,distatnces_min,max_generation,pop,last_nuke, nuke_count).bomb()

        else:
            # pop=TournamentSelection(k_participants,tournament_pop,r1).sellect_winners() 
            pop=RouletteSelection(tournament_pop,r1).roll()
            # pop=PMX(pop,chance_to_pmx).c1_c2_pmx()
            pop=CX(pop,chance_to_pmx).cx()
            # pop=OX(pop,chance_to_pmx).ox()
            pop=Mutation(pop,chance_to_mutate).inversion()
            # pop, last_nuke, nuke_count =MutationBomb(t,distatnces_min,max_generation,pop,last_nuke, nuke_count).bomb()




        ## Rate 
        r1=Rate(pop,m1).rate()
        rates=[y[1] for y in r1]
        best_indiwiduals.append(min(r1, key=lambda x:x[1])[0])

        ## Save Results
        distatnces_min.append(min(rates))
        distatnces_max.append(max(rates))
        distatnces_avg.append(mean(rates))
        distatnces_peak.append((min(distatnces_min)))


        ## Tracking algorithm progress              
        if tracking==None:
            t=t+1    
        elif t%tracking!=0:    
            t=t+1
        else:
            print('Gen: {}, with best score: {}'.format(t,min(rates)))
            t=t+1

    #############################################


    
    ## Best Results 
    result=Rate(best_indiwiduals, m1).rate()
    result.sort(key=takeSecond)
    print(f'''\n
            ----------------------------------------------------------------------------\n

            Mutatuion: {chance_to_mutate}, Crossover: {chance_to_pmx},
            k_participants: {k_participants}, Population: {tournament_pop},
            Max_generation: {max_generation}, RunTime: {datetime.now()-start},
            Nuke Count: {nuke_count}, Best rate {result[0][1]}

            ----------------------------------------------------------------------------
            ''')

    print("-".join(map(str,result[0][0])), result[0][1])

    ## save result 
    result_dict={
        "Name": file_name,
        'Fitness': result[0][1],
        'RunTime': str(datetime.now()-start),
        'chance_to_mutate': chance_to_mutate,
        'chance_to_pmx': chance_to_pmx,
        'k_participants': k_participants,
        'tournament_pop': tournament_pop,
        'max_generation':  max_generation,
        'nuke_count': nuke_count,
        'Result': result[0][0],
        'distances_max': distatnces_max,
        'distances_avg': distatnces_avg,
        'distances_min': distatnces_min,
        'distances_peak': distatnces_peak
    }
    

    ## Save result
    if save_results==True:
        save_result(result_dict,'json')
    ## Plot result 
    if plot_results == True:
        plot_result(result_dict)

        

    return result_dict


# resuls=genetic_algorithm( file_name='berlin52',
#     base_pop=200,
#     max_generation=500,
#     tournament_pop=150,
#     k_participants=2,
#     chance_to_pmx=0.8,
#     chance_to_mutate=0.1,
#     tracking=10,
#     start_roulete=0.8,
#     save_results=True,
#     plot_results=True)
    



