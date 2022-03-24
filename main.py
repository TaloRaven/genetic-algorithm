from genetic_algorithms.Classes import Matrix,BasePop,TournamentSelection,Pairindividuals

def main():
    FILE_NAME='berlin52'

    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,100).rate()
    t1=TournamentSelection(3,50,b1).sellect_winners()
    pair=Pairindividuals(t1).pair_individuals_intercepts()
    print('\nMatrix \n')
    [print(x) for x in m1]
    print('\nBase population \n')
    [print(x) for x in b1]
    print('\nTournament selecton \n')
    [print(x) for x in t1]

    [print(x) for x in pair]


if __name__ == "__main__":
    main()