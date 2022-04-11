
from statistics import mean
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from genetic_algorithm import genetic_algorithm
from parameters_testing import ga_parameters_testing



if __name__ == "__main__":
    start=datetime.now()    
    ga_parameters_testing('berlin52')
    print (f"Runtime of the program:  {datetime.now()-start}")
    