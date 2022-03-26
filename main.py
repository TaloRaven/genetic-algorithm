from genetic_algorithms.BasePop import *
from genetic_algorithms.Matrix import *
from genetic_algorithms.TournamentSelection import *
from genetic_algorithms.Pairindividuals import *
from genetic_algorithms.PMX import *
def main():
    FILE_NAME='test'

    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,50).rate()
    t1=TournamentSelection(3,12,b1).sellect_winners()
    p1=Pairindividuals(t1).pair_individuals_intercepts()
    p1_1=Pairindividuals(t1).intercepts_individuals()
    c1=PMX(t1).c1_c2_pmx()
    print('\nMatrix \n')
    [print(x) for x in m1]
    print('\nBase population \n')
    [print(x) for x in b1]
    print('\nTournament selecton \n')
    [print(x) for x in t1]
    print('\nPair to cross \n')
    [print(x) for x in p1]
    print('\nPair to cross after ciecie \n')
    [print(x) for x in p1_1]
    print('\n Individuals after PMX \n')
    [print(x) for x in c1]


if __name__ == "__main__":
    main()