class House:                                      #создаем новый класс с именем House.
    def __init__(self,name, number_of_floors):    # этот метод вызывается при создании нового объекта класса House.
        self.name = name                          #создаем атрибут name для объекта и присваиваем ему значение, переданное при создании объекта.
        self.number_of_floors = number_of_floors  #аналогично создаем атрибут number_of_floors для объекта.


    def go_to(self,new_floor):                     #этот метод принимает значение new_floor (номер этажа, на который нужно приехать).
        if 1<= new_floor <= self.number_of_floors: #проверяем, является ли new_floor допустимым номером этажа (в пределах от 1 до количества этажей дома).
            for i in range(1, new_floor +1):       #выведим на экран числа от 1 до new_floor.
                print(i)
        else:
            print('Такого этажа не существует') #если new_floor недопустим, то выводит сообщение “Такого этажа не существует”.

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" #возвращает строку, которая содержит название дома и количество этажей.



    def __eq__(self, other):  # Проверяет, являются ли self и other объектами класса House.
        if isinstance(other, House):
            return  self.number_of_floors == other.number_of_floors#Если да, то сравнивает количество этажей и возвращает True, если они равны.
        return True

    def __lt__(self, other):# операторы сравнения
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):# операторы сравнения
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):# операторы сравнения
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):# операторы сравнения
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):# операторы сравнения
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int): # Проверяет, является ли value целым числом.
            self.number_of_floors += value #Если да, то увеличивает количество этажей на value и возвращает сам объект self.
            return self
        return NotImplemented  #В противном случае возвращает NotImplemented.


    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
