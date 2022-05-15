from genetic_algorithm import genetic_algorithm
from datetime import datetime
import json
from Modules import *
from utils import  takeSecond
from statistics import mean
def ga_parameters_testing(file_name, dt_string):
    """Function to test multiple parameters for genetic_algorithm
    Parameters:
    file_name: str
        Name of triangular matrix matrix in txt format placed in data folder
    test_name: str 
        name a test, test is saved in /data/results

    returns:
    list : test results [raod, best score, parameters chosed,rundtime] saved  in /data/results/{test_name}.json
    """
    test_start=datetime.now() 


    # datetime object containing current date and time
    now = datetime.now()
    

    results12=[]
    chance_to_pmx_range=[x/100 for x in range(70,81,5)]
    chance_to_mutate_range=[x/100 for x in range(10,17,2)]
    k_participants_range=[2]
    tournament_pop_range=[x for x in range(750,951,50)]
    max_generation_range=[x for x in range(10000,10001,1000)]


    # chance_to_pmx_range=[x/100 for x in range(65,86,2)]
    # chance_to_mutate_range=[x/100 for x in range(10,21,2)]
    # k_participants_range=[2]
    # tournament_pop_range=[x for x in range(750,751,50)]
    # max_generation_range=[x for x in range(10000,10001,1000)]

    for chance_to_mutate in chance_to_mutate_range:
        for chance_to_pmx in chance_to_pmx_range:
            for k_participants in k_participants_range:
                for tournament_pop in tournament_pop_range:
                    for max_generation in max_generation_range:

                        result11=genetic_algorithm(file_name, base_pop=500,
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
    # print([print(x) for x in results12[0][0]])
    print("-".join(map(str,results12[0][0])), results12[0][1])

    print(f"\nTest Time: {datetime.now()-test_start}")



    with open(f"data/results/parameters{dt_string}.json", 'w') as f:
            json.dump(results12, f) 


def ga_mutliple_attempts(n,file_name: str,
                        base_pop: int,
                        max_generation: int,
                        tournament_pop: int,
                        k_participants: int,
                        dhm_ilc: bool,
                        crossover_chance: float,
                        mutation_chance: float,
                        exploitation_start: float,
                        tracking: int or None,
                        plot_results: bool,
                        save_results: bool):

    """Function to test mutliple times genetic_algorithm,with chosen one set of parameters
    
    returns:
    int: 
    """
    test_start=datetime.now() 

    results12=[]
    for _ in range(0,n): 
        result11=genetic_algorithm( file_name=file_name,
                        base_pop=base_pop,
                        max_generation=max_generation,
                        tournament_pop=tournament_pop,
                        k_participants=k_participants,
                        dhm_ilc=dhm_ilc,
                        crossover_chance=crossover_chance,
                        mutation_chance=mutation_chance,
                        exploitation_start=exploitation_start,
                        tracking=tracking) 

        results12.append(result11)
    results12=sorted(results12, key=lambda d: d['Fitness']) 
    
    print(f'\n############## Final Results ############\n')
    [print("-".join(map(str,x['Result'])), x['Fitness']) for x in results12]
        

    print(f'\n############## Top Result   ############\n')
    

    print('\nResults\n')
    for key, value in results12[0].items():
        if key not in ['distances_max', 'distances_avg', 'distances_min', 'distances_peak', 'Result']:
            print(key, ' : ',value )
    print('\n')

    print("-".join(map(str,results12[0]['Result'])), results12[0]['Fitness'])

    now = datetime.now()
    dt_string = str(now.strftime("%d-%m-%Y[%H_%M]"))
    print(f"\nTest Time: {datetime.now()-test_start}")

    # with open(f"data/results/multi{dt_string}.json", 'w') as f:
    #         json.dump(results12, f) 


