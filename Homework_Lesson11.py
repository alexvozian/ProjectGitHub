#Ex1:
from my_library.square import square

a = square(12)
print(a)
a.set_length(6)
print(a)
print(a.get_length(4))
print(a)

#Ex2:
class List:
    def __init__(self, lis:list):
        self.Lis = lis



class NumbersList(List):

    def __init__(self, lis:list):
        self.Lis = list()
        for el in lis:
            self.Lis.append(float(el))

    def get_sum(self):
        return sum(self.Lis)

    def get_average(self):
        return self.get_sum() / len(self.Lis)

z = NumbersList([2, 3, 5])
print(z.Lis)
print(z.get_sum())
print(z.get_average())