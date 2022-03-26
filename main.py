from genetic_algorithms.BasePop import *
from genetic_algorithms.Matrix import *
from genetic_algorithms.TournamentSelection import *
from genetic_algorithms.Pairindividuals import *
from genetic_algorithms.PMX import *
from genetic_algorithms.Rate import *
from genetic_algorithms.MutationExchange import MutationExchange
import random

FILE_NAME='berlin52'
LEN_BASE_POP=100
NUM_GENERATIONS=2000
TURNAMENT_SELECTION_NUM_BRACKET=100
NUMBER_OF_PARTICIPANTS_IN_BRACKET=3
CHANCE_TO_MUTATE=0.35


def main():
    t=0
    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,LEN_BASE_POP).n_pop()
    r1=Rate(b1,m1).rate()
    while not t==NUM_GENERATIONS:
        t1=TournamentSelection(NUMBER_OF_PARTICIPANTS_IN_BRACKET,TURNAMENT_SELECTION_NUM_BRACKET,r1).sellect_winners()
        c1=PMX(t1).c1_c2_pmx()
        mut1=MutationExchange(c1,CHANCE_TO_MUTATE).mutation()
        r1=Rate(mut1,m1).rate()
        t=t+1

    print('Last generation {}'.format(t))
    [print(x) for x in r1]
    print('\n Best rate \n')
    rates=[y[1] for y in r1]
    print(min(rates))

if __name__ == "__main__":
    main()