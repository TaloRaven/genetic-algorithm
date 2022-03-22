from genetic_algorithms.Classes import Matrix,BasePop,TournamentSelection
import random

FILE_NAME='test'

m1=Matrix(FILE_NAME).txt_to_matrix()
b1=BasePop(m1,6).rate()
t1=TournamentSelection(3,6,b1).sellect_winners()

#robimy liste bez oceny
t2=[]
for x in t1:
    t2.append(x[0])
print(t2)

def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]

# Driver Code
r1, r2 = 0, len
b_pop=createList(r1, len(t1[0][0]))
