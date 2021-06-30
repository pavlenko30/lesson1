class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)])  \
                + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'В первой клетке ячеек больше или же равно второй, вычесть нельзя'

    def __mul__(self, other):
        return 'Умножение ячеек равняется ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Истинное число ячеек ' + str(round(self.nums / other.nums))


cell_1 = Cell(7)
cell_2 = Cell(25)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(5))
