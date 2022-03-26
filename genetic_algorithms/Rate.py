class Rate():
    def __init__(self, population, matrix):
        self.population=population
        self.matrix=matrix
    
    def rate(self):
        rates=[]
        for o in self.population:
            n=0
            rates_uq=[]
            try:
                for _ in o:
                    rates_uq.append(self.matrix[o[n]][o[n+1]])
                    n+=1
            except:
                rates_uq.append(self.matrix[o[-1]][o[0]])

            rates.append(sum(rates_uq))

        return [[self.population[i],rates[i]] for i in range(len(self.population))]

