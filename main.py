from genetic_algorithms.BasePop import *
from genetic_algorithms.Matrix import *
from genetic_algorithms.TournamentSelection import *
from genetic_algorithms.Pairindividuals import *
from genetic_algorithms.PMX import *
from genetic_algorithms.Rate import *
def main():
    FILE_NAME='test'

    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,8).n_pop()
    r1=Rate(b1,m1).rate()
    t1=TournamentSelection(3,8,r1).sellect_winners()
    c1=PMX(t1).c1_c2_pmx()


    print('\nMatrix \n')
    [print(x) for x in m1]
    print('\nBase population \n')
    [print(x) for x in b1]
    print('\nRates of base population \n')
    [print(x) for x in r1]
    print('\nTournament selecton \n')
    [print(x) for x in t1]
    print('\n PMX \n')
    [print(x) for x in c1]


if __name__ == "__main__":
    main()