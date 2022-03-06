

def txt_to_matrix(txt_name):
    matrix = []
    with open('./data/{}.txt'.format(txt_name), 'r') as f:
            for line in f:
                matrix.append(list(map(str,line.split())))
    f.close()

    matrix=matrix[1:]

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


test=txt_to_matrix('test')

[print(i) for i in test]