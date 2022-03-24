from random import sample

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
        return [sample(m, len(m)) for _ in range(self.n)]

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