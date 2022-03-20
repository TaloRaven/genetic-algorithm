from genetic_algorithms.Classes import Matrix,BasePop,TournamentSelection

def main():
    FILE_NAME='test'

    m1=Matrix(FILE_NAME).txt_to_matrix()
    b1=BasePop(m1,5).rate()
    t1=TournamentSelection(3,5,b1).sellect_winners()
    print('\nMatrix \n')
    print(m1)
    print('\nBase population \n')
    [print(x) for x in b1]
    print('\nTournament selecton \n')
    [print(x) for x in t1]

if __name__ == "__main__":
    main()