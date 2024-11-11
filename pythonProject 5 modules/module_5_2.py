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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))