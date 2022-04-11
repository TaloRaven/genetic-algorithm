from random import choice, random, sample
class MutationExchange():
    """
    Mutatation exchange for population 

    Atributes:
    post_cross_population:
        population after crossover 
    mutation_rate:
        propability to mutate chosen character in population 
    
    """
    def __init__(self,post_cross_population, mutation_rate):
        self.post_cross_population=post_cross_population
        self.mutation_rate=mutation_rate

    def mutation(self):
        population=self.post_cross_population
        post_mut=[]
        for element in population:
            if random() < self.mutation_rate:
                idx = range(len(element))
                i1, i2 = sample(idx, 2)
                element[i1], element[i2] = element[i2], element[i1]
                post_mut.append(element)
            else:
                post_mut.append(element)
        return post_mut

