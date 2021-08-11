class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return str(self.my_matrix)

    def __add__(self, other):
        n = len(self.my_matrix)
        result_matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                result_matrix[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix(result_matrix)


A = [[1, 2 ,3],
     [2, 3 ,4],
     [3, 4, 5]]

B = [[7, 8, 9],
     [5, 6, 7],
     [3, 4, 5]]

my_A = Matrix(A)
my_B = Matrix(B)

print(my_A)
print(my_B)
print(my_A + my_B)

