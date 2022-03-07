import random

def txt_to_matrix(txt_name):
    matrix = []
    with open('./data/{}.txt'.format(txt_name), 'r') as f:
        for line in f.readlines()[1:]:
            matrix.append(list(map(int,line.split())))
    f.close()


    for count, value in enumerate(matrix):
        z=count+1
        for i in range(len(matrix)-z):
            value.append(matrix[z][count])
            z+=1
            
    return matrix


def save_matrix(matrix):
    with open("file.txt", 'w') as file:
            for row in matrix:
                s = " ".join(map(str, row))
                file.write(s+'\n')


def n_pop(matrix, n):
    m=[x for x in range(len(matrix))]
    return [random.sample(m, len(m)) for _ in range(n)]


def rate(matrix,n_pop):
    rates=[]
    for o in n_pop:
        n=0
        rates_uq=[]
        try:
            for i in o:
                rates_uq.append(matrix[o[n]][o[n+1]])
                n+=1
        except:
            rates_uq.append(matrix[o[-1]][o[0]])

        rates.append(sum(rates_uq))
    matrix_rate=[]
    [matrix_rate.append([n_pop[i],rates[i]]) for i in range(len(n_pop))]
    return matrix_rate






test=txt_to_matrix('test')
osb=n_pop(test,5)
[print(i) for i in test]
print(osb)
print(rate(test,osb))

