from genetic_algorithm import genetic_algorithm
from datetime import datetime
import json
import pandas as pd

from utils.takesecond import  takeSecond


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
    

    # dd/mm/YY H:M:S
    

    results12=[]
    chance_to_pmx_range=[x/100 for x in range(85,86,5)]
    chance_to_mutate_range=[x/100 for x in range(21,21,2)]
    k_participants_range=[2]
    tournament_pop_range=[x for x in range(500,501,50)]
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


def ga_mutliple_attempts(dt_string,n,file_name,
                                base_pop,
                                max_generation,
                                tournament_pop,
                                k_participants,
                                chance_to_pmx,
                                chance_to_mutate):

    """Function to test mutliple times genetic_algorithm,with chosen one set of parameters
    
    returns:
    int: 
    """
    test_start=datetime.now() 

    results12=[]
    for _ in range(0,n): 
        result11=genetic_algorithm(file_name, base_pop,
                                    max_generation=max_generation,
                                    tournament_pop=tournament_pop,
                                    k_participants=k_participants,
                                    chance_to_pmx=chance_to_pmx,
                                    chance_to_mutate=chance_to_mutate)                           
        results12.append(result11)

    results12.sort(key=takeSecond)
    print(f'\n############## Final Results ############\n')
    [print("-".join(map(str,x[0])), x[1]) for x in results12]
        

    print(f'\n############## Top Result   ############\n')
    print([print(x) for x in results12[0][1:]])
    print("-".join(map(str,results12[0][0])), results12[0][1])


    now = datetime.now()
    dt_string = str(now.strftime("%d-%m-%Y[%H_%M]"))
    with open(f"data/results/multi{dt_string}.json", 'w') as f:
            json.dump(results12, f) 



    print(f"\nTest Time: {datetime.now()-test_start}")


now = datetime.now()
dt_string = str(now.strftime("%d-%m-%Y[%H_%M]"))


# # 259045
genetic_algorithm( file_name='berlin52',
    base_pop=100,
    max_generation=10000,
    tournament_pop=700,
    k_participants=2,
    chance_to_pmx=0.8,
    chance_to_mutate=0.2,
    tracking=1000,
    plot_results=True)



# ga_mutliple_attempts(n=20,dt_string=dt_string, file_name='berlin52',
#     base_pop=100,
#     max_generation=5000,
#     tournament_pop=500,
#     k_participants=5,
#     chance_to_pmx=0.8,
#     chance_to_mutate=0.2)
