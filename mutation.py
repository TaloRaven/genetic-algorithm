from genetic_algorithms.Classes import Matrix,BasePop,TournamentSelection
import random

FILE_NAME='test'

m1=Matrix(FILE_NAME).txt_to_matrix()
b1=BasePop(m1,6).rate()
t1=TournamentSelection(3,6,b1).sellect_winners()


print('\nMatrix \n')
[print(x) for x in m1]
print('\nBase population \n')
[print(x) for x in b1]
print('\nTournament selecton \n')
[print(x) for x in t1]

t2=[]
for x in t1:
    t2.append(x[0])
print(t2)

#p1
print(len(t2[0]))
# punkt yprzeciecia
pkt_prze=random.sample(range(1, len(t2[0])), 2)
#
print(t1[0][0])
# for i in pkt_prze:
#     for x in t1[0]:
#         print(x[i])


def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]


# Driver Code
r1, r2 = 0, len
b_pop=createList(r1, len(t1[0][0]))

b_pop_pair = {}

for p in range(len(b_pop) // 2):
    b_pop_pair[p+1] = (b_pop.pop(random.randrange(len(b_pop))),
                  b_pop.pop(random.randrange(len(b_pop))))

print(b_pop_pair)


pary_osobnik=[]
for x in b_pop_pair:
    #print(b_pop_pair[x])
    print(t2[b_pop_pair[x][0]],t2[b_pop_pair[x][1]] )
    pary_osobnik.append((t2[b_pop_pair[x][0]],t2[b_pop_pair[x][1]],random.sample(range(1, len(t1[0][0])), 2)))

print(pary_osobnik)

for x in pary_osobnik:
    print(x)


# g=gencoordinates(0,len(t1[0][0]))
# for x in range(len(t1[0][0])):
#     print(next(g))
#zamana robi duza namieszanie
# inwersja mniej zmaieszania