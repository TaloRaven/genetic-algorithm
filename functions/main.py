
from statistics import mean
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from genetic_algorithm import genetic_algorithm
# from parameters_testing import ga_parameters_testing

['berlin52','gr120','pr107', 'kroA100', 'pr1002','ulysses16'



]

if __name__ == "__main__":
    # start=datetime.now()


    genetic_algorithm( file_name='berlin52',
                        base_pop=100,
                        max_generation=50000,
                        tournament_pop=60,
                        k_participants=2,
                        chance_to_pmx=0.95,
                        chance_to_mutate=0.05,
                        tracking=10000,
                        start_roulete=0.1,
                        save_results=True,
                        plot_results=True)
                        
                        

    # print (f"Runtime of the program:  {datetime.now()-start}")
    