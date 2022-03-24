from genetic_algorithms.BasePop import *
from genetic_algorithms.Matrix import *
from genetic_algorithms.TournamentSelection import *


def main():
    FILE_NAME='berlin52'

    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,100).rate()
    t1=TournamentSelection(3,22,b1).sellect_winners()
    print('\nMatrix \n')
    [print(x) for x in m1]
    print('\nBase population \n')
    [print(x) for x in b1]
    print('\nTournament selecton \n')
    [print(x) for x in t1]

if __name__ == "__main__":
    main()