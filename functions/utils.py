
from lib2to3.pgen2.pgen import generate_grammar
from unicodedata import name
import matplotlib.pyplot as plt
import os
from datetime import datetime
import json
import re

import pandas as pd 

os.makedirs(r'C:\Users\macie\Desktop\Projects\ue_zsi\data\results', exist_ok=True)

def takeSecond(elem):
    return elem[1]


def load_result():
    pass

def save_result(result, format: str) -> None:
    """
    result: dict
        result from genetic_algorithm
    format: str
        availible formats 'json', 'csv'
    """
    # assume you have the following dictionary
    if format=='json':
        now = datetime.now()
        dt_string = str(now.strftime("%H.%M_%d-%m-%Y"))

        with open("results/{}_{}.json".format(result['Name'], dt_string), "w+") as write_file:
            json.dump(result, write_file, sort_keys=True, default=str)
    else:
        now = datetime.now()
        dt_string = str(now.strftime("%H.%M_%d-%m-%Y"))

        df=pd.DataFrame.from_dict(result, orient='index',columns=['distances_max', 'distances_avg', 'distances_min'])
        df.head()

def get_optimum(file_name)-> int:
    """ get global optimum value from txt file with perfect scores for chosen TSP problems """

    with open("data/tsp_optima.txt", "r") as f:
        optimas = f.read()

    patern = re.compile(r'(.*) : (.*)')

    matches = patern.finditer(optimas)

    optimals_dict={}
    for match in matches:
        optimals_dict[match.group(1)]=match.group(2)

    try:
        optimum=optimals_dict[file_name]
    except:
        optimum=None
    
    return optimum

def plot_result(result: dict) -> plt.show():
    """Line plot showing algorithm progression with finding global optimum """
    # plt.title(f'''peak: {distatnces_peak[-1]}, chance_to_mutate, {chance_to_mutate},chance_to_pmx, {chance_to_pmx}, k_participants, {k_participants} \n
    # tournament_pop,{tournament_pop}, max_generation {max_generation} ''')

    optimum = get_optimum(result["Name"])

    optimum


    gen=[x for x in range(0,result['max_generation'])]

    plt.title('Genetic Algorithm/TSP proble: {}'.format(result['Name']))
    
    
    plt.plot(gen, result['distances_max'], color='r', alpha=0.1)
    plt.plot(gen, result['distances_avg'], color='orange', alpha=0.8)
    plt.plot(gen, result['distances_min'], color='b')
    plt.plot(gen, result['distances_peak'], color='green', linewidth=2)
    if optimum != None:
        plt.axhline(y = int(optimum), color = 'r', linestyle = 'dashed', label='optimum')
        plt.yticks(list(plt.yticks()[0]) + [int(optimum)])   

    plt.axhline(y = result['distances_peak'][-1], color = 'green', linestyle = 'dashed', label='result')
    plt.yticks(list(plt.yticks()[0]) + [result['distances_peak'][-1] ])   
    plt.text(0.7, 0.7, f"""

    'Fitness': {result['Fitness']}
    "Global optimum": {result['Global_optimum']}
    'chance_to_mutate': {result['chance_to_mutate']}
    'chance_to_pmx': {result['chance_to_pmx']}
    'k_participants': {result['chance_to_pmx']}
    'tournament_pop': {result['tournament_pop']}
    'max_generation': {result['max_generation']}
    'nuke_count': {result['nuke_count']}
    'RunTime': {result['RunTime']}

    """,
     fontsize=10, transform=plt.gcf().transFigure)  

    plt.ylabel('Distance')
    plt.xlabel('t-generations')
    plt.legend(['max', 'avg','min for t','peak for t','optimum','peak all time'], loc='upper right')


    return plt.show() 