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

