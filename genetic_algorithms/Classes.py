import random
class Matrix():
    '''
        Atributes:

        txt_file_name: str
            name of matrix in txt format   
    '''

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
    '''
        Atributes:

        matrix: list 
            square symmetrical matrix of distance
        n: int 
            number of base population

    '''

    def __init__(self,matrix, n) -> None:
        self.matrix=matrix
        self.n=n

    def n_pop(self):
        m=[x for x in range(len(self.matrix))]
        return [random.sample(m, len(m)) for _ in range(self.n)]

    def rate(self):
        rates=[]
        population = self.n_pop()
        for o in population:
            n=0
            rates_uq=[]
            try:
                for _ in o:
                    rates_uq.append(self.matrix[o[n]][o[n+1]])
                    n+=1
            except:
                rates_uq.append(self.matrix[o[-1]][o[0]])

            rates.append(sum(rates_uq))

        return [[population[i],rates[i]] for i in range(len(population))]

class TournamentSelection():
    '''
    Atributes:
    
    n: int 
        number of participants in bracket 
    k: int 
        number of tournament brackets
    basepop: list 
        1st base population chosen randomly from matrix  
    
    '''
    def __init__(self, n: int, k: int,basepop: list) -> None:
        self.n=n
        self.k=k
        self.basepop=basepop

    def turnament(self):
        turnament=[]
        for _ in range(self.k):
                bracket = random.sample(self.basepop, self.n)
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
                winner=[random.choice(winner)]
            winners.append(winner)
        return [item for sublist in winners for item in sublist]


class RuleteSelection():
    pass

class EliteSelection():
    pass

class PMX():
    pass

class CX():
    pass
 
class OX():
    pass 
