from random import sample, choice, randrange

class Matrix():

    def __init__(self,txt_file_name) -> None:
        self.txt_file_name=txt_file_name

    def txt_to_matrix(self):
        matrix = []
        with open('./data/{}.txt'.format(self.txt_file_name), 'r') as f:
            for line in f.readlines()[1:]:
                matrix.append(list(map(int,line.split())))
        f.close()

        for count, value in enumerate(matrix):
            z=count+1
            for _ in range(len(matrix)-z):
                value.append(matrix[z][count])
                z+=1         
        return matrix

    def save_matrix(self):
        with open("file.txt", 'w') as file:
                for row in self.txt_to_matrix():
                    s = " ".join(map(str, row))
                    file.write(s+'\n')

class BasePop():
    def __init__(self,matrix, n) -> None:
        self.matrix=matrix
        self.n=n

    def n_pop(self):
        m=[x for x in range(len(self.matrix))]
        return [sample(m, len(m)) for _ in range(self.n)]

    def rate(self):
        rates=[]
        for o in self.n_pop():
            n=0
            rates_uq=[]
            try:
                for i in o:
                    rates_uq.append(self.matrix[o[n]][o[n+1]])
                    n+=1
            except:
                rates_uq.append(self.matrix[o[-1]][o[0]])

            rates.append(sum(rates_uq))

        return [[self.n_pop()[i],rates[i]] for i in range(len(self.n_pop()))]

class TournamentSelection():
    def __init__(self, n, k,basepop) -> None:
        self.n=n
        self.k=k
        self.basepop=basepop

    def turnament(self):
        turnament=[]
        for _ in range(self.k):
                bracket = sample(self.basepop, self.n)
                turnament.append(bracket)
        return turnament
    
    def sellect_winners(self):
        winners=[]
        for bracket in self.turnament():
            score=[]
            for x in bracket:
                score.append(x[1])
            winner=[]
            for index, x in enumerate(score):
                if x == min(score):
                    winner.append(bracket[index])
                else:
                    continue
            if len(winner) != 1:
                winner = [choice(winner)]
            winners.append(winner)
        return [item for sublist in winners for item in sublist]


class RuleteSelection():
    pass

class EliteSelection():
    pass

class Pairindividuals():

    def __init__(self, turnament_selection) -> None:
        self.turnament_selection=[x[0] for x in turnament_selection]

    def intercepts(self):
        roll1=choice(range(1, len(self.turnament_selection[0])))
        roll2=choice(range(roll1, len(self.turnament_selection[0])))
        return [roll1,roll2]
        
    def createlist(self):
        return [item for item in range(0, len(self.turnament_selection))]

    def pair_individuals(self):
        indexes=self.createlist()
        pairs_pn = {}
        for p in range(len(indexes) // 2):
            pairs_pn[p+1] = (indexes.pop(randrange(len(indexes))),
                        indexes.pop(randrange(len(indexes))))
        return pairs_pn

    def pair_individuals_intercepts(self):
        pairs_pn=self.pair_individuals()
        t = self.turnament_selection

        pairs=[]
        for x in pairs_pn:
            pairs.append((t[pairs_pn[x][0]],t[pairs_pn[x][1]],self.intercepts()))
        return pairs



class PMX(Pairindividuals):
    pass

class CX(Pairindividuals):
    pass
 
class OX(Pairindividuals):
    pass

class Mutationexchage():
    pass

class MutationInv():
    pass