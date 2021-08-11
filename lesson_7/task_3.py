class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        sub = self.n - other.n
        if sub > 0:
            return sub
        return "Разность ячеек клеток меньше нуля"

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return round(self.n / other.n)

    def make_order(self, length):
        for i in range(self.n // length):
            print(' * ' * length, end='\n')
        print(' * ' * (self.n % length))


my_cell_1 = Cell(12)
my_cell_2 = Cell(15)

print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_2 - my_cell_1)
print(my_cell_1 * my_cell_2)
print(my_cell_1 / my_cell_2)

my_cell_1.make_order(5)
my_cell_2.make_order(5)


