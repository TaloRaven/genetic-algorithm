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