from statistics import mean
from Modules import *
from Modules import CX

from functions.utils import *
import os


def genetic_algorithm(file_name: str,
                      base_pop: int,
                      max_generation: int,
                      tournament_pop: int,
                      k_participants: int,
                      dhm_ilc: bool,
                      crossover_chance: float,
                      mutation_chance: float,
                      exploitation_start: float,
                      show_results: bool = False,
                      tracking: int or None = None,
                      plot_results: bool = False,
                      save_results: bool = False) -> dict:
    '''
    A genetic algorithm that tries to find the shortest path in a TSP problem.

    Parameters: 

        file_name: str
            Name of TSP problem in form of triangular matrix in txt format 
            
        base_pop: int
            base pop randomly selected from matrix 

        max_generation: int
            max number of generations, stop condition

        tournament_pop: int
            Population, (number of brackets in tournamnet or number of roulette spins) 

        k_participants: int
            number of praticipants in one bracket of a tournament

        dhm_ilc: bool:
            Dynamic Decreasing of high mutation ratio/dynamic increasing of low crossover ratio \n
            parameter crossover_chance act as max for  example crossover_chance= 0.95 is range(0,0.95) with growing t \n  
            parameter mutation_chance act as starting point example mutation_chance = 0.5 is range(0.5, 0) with growing t

        crossover_chance: float (0:1)
            Propability of crossover pair of parents into pair of children  

        mutation_chance: float(0:1)
            Propability of mutation invidual

        exploitation_start: float
            Tournament selection -> Roulette Selection
            Mutation exchange -> Mutation inversion

        tracing: int
            Shows results every number declared   

        plot_results: bool
            if True plot shows  progresion of finding optimal path by algorithm 

        save_results: bool
            if True saves algorithm output in json/csv file  

    Returns: dict
            stored progress with parameters 

    '''
    ## Runtime
    start = datetime.now()

    ## List of results 
    result = []
    distatnces_max = []
    distatnces_min = []
    distatnces_avg = []
    distatnces_peak = []
    best_indiwiduals = []

    ## Algorithm
    # ======================================================================================================#
    last_nuke = 0
    nuke_count = 0
    t = 0
    m1 = Matrix(os.getcwd(),file_name).txt_to_matrix()
    pop = BasePop(m1, base_pop).n_pop()
    r1 = Rate(pop, m1).rate()
    if dhm_ilc == True:
        init_mutation_chance = mutation_chance
        init_crossover_chance = crossover_chance

    while not t == max_generation:

        if dhm_ilc == True:
            mutation_chance = init_mutation_chance - t / max_generation * init_mutation_chance
            crossover_chance = t / (max_generation + (1 - init_crossover_chance) * max_generation)

        ## Exploration
        if t < max_generation * exploitation_start:
            pop = TournamentSelection(k_participants, tournament_pop, r1).sellect_winners()
            pop = CX(pop, crossover_chance).cx()
            pop = Mutation(pop, mutation_chance).exchange()

        ## Exploitation
        else:
            pop = RouletteSelection(tournament_pop, r1).roll()
            pop = CX(pop, crossover_chance).cx()
            pop = Mutation(pop, mutation_chance).inversion()

        ## Rate 
        r1 = Rate(pop, m1).rate()
        rates = [y[1] for y in r1]
        best_indiwiduals.append(min(r1, key=lambda x: x[1])[0])

        ## Save Results or plot result  
        if plot_results == True or save_results == True:
            distatnces_min.append(min(rates))
            distatnces_max.append(max(rates))
            distatnces_avg.append(mean(rates))
            distatnces_peak.append((min(distatnces_min)))

        ## Tracking algorithm progress           
        if tracking == None or t % tracking != 0 or t == 0:
            pass
        else:
            print('Gen: {}, with best score: {}'.format(t, min(rates)))
        t = t + 1

    # ======================================================================================================#

    ## Rate/Sort Results
    result = Rate(best_indiwiduals, m1).rate()
    result.sort(key=takeSecond)

    ## save result 

    result_dict = {
        "Name": file_name,
        'Fitness': result[0][1],
        "Global_optimum": get_optimum(file_name),
        "Delta": int(result[0][1]) - int(get_optimum(file_name)),
        'RunTime': str(datetime.now() - start),
        'dhm_ilc': dhm_ilc,
        'mutation_chance': mutation_chance,
        'crossover_chance': crossover_chance,
        'k_participants': k_participants,
        'tournament_pop': tournament_pop,
        'max_generation': max_generation,
        'nuke_count': nuke_count,
        'Result': result[0][0],
        'distances_max': distatnces_max,
        'distances_avg': distatnces_avg,
        'distances_min': distatnces_min,
        'distances_peak': distatnces_peak
    }

    ## Show Results
    if show_results == True:
        print('\nResults\n')
        for key, value in result_dict.items():
            if key not in ['distances_max', 'distances_avg', 'distances_min', 'distances_peak', 'Result']:
                print(key, ' : ', value)
        print('\n')
        # print("-".join(map(str,result[0][0])), result[0][1])

    ## Save result
    if save_results == True:
        save_result(result_dict, 'json')

    ## Plot result 
    if plot_results == True:
        plot_result(result_dict)

    return result_dict
