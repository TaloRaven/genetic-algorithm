import os


class Matrix():
    '''
        Class represent a square matrix 

        Atributes:
        file_name: str
            Name of triangular matrix matrix in txt format placed in data folder
        cwd: str
            Current directory
        Returns:
        matrix: list 
            square matrix

        Methods:
        txt_to_matrix():
            Loads txt file and tranform it to square matrix 
        save_matrix(file_name='matrix'):
            Save matrix, default name 'matrix' 

    '''

    def __init__(self, cwd, txt_file_name) -> None:
        self.txt_file_name = txt_file_name
        self.cwd = cwd

    def txt_to_matrix(self):
        matrix = []

        with open(r'{}/data/{}.txt'.format(self.cwd, self.txt_file_name), 'r') as f:
            for line in f.readlines()[1:]:
                matrix.append(list(map(int, line.split())))
        f.close()

        for count, value in enumerate(matrix):
            z = count + 1
            for _ in range(len(matrix) - z):
                value.append(matrix[z][count])
                z += 1
        return matrix

    def save_matrix(self, file_name='matrix'):
        with open("{}.txt".format(file_name), 'w') as file:
            for row in self.txt_to_matrix():
                s = " ".join(map(str, row))
                file.write(s + '\n')
