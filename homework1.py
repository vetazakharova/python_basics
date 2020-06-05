class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __add__ (self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list1)):

            for j in range(len(self.list2)):
                matr[i][j] = self.list1[i][j] + self.list2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

matrix = Matrix([[5, 6, 7], [5, 6, 7], [5, 6, 7]], [[5, 4, 3], [5, 4, 3], [5, 4, 3]])
print(matrix.__add__())
