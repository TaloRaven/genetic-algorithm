from random import choice, random, sample, randint
class Mutation():
    """
    Mutatation exchange for population, randomly change position of 2 elemens in invidual  

    Atributes:
    post_cross_population:
        population after crossover 
    mutation_rate:
        propability to mutate chosen character in population 
    
    Methods:
    exchange(): -> list

    """
    def __init__(self,post_cross_population, mutation_rate):
        self.post_cross_population=post_cross_population
        self.mutation_rate=mutation_rate

    def exchange(self) -> list:
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

    def inversion(self):
        population=self.post_cross_population
        post_mut=[]

        for individual in population:
            if random() <= self.mutation_rate:
                first_cross_point = randint(0, len(individual) - 2)
                second_cross_point = randint(first_cross_point + 1, len(individual) - 1)
                new_individual = individual[:first_cross_point]+ individual[first_cross_point:second_cross_point][::-1] + individual[second_cross_point:]
                post_mut.append(new_individual)
            else:
                post_mut.append(individual)
        return post_mut
