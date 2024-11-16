class House:
    houses_history = []


    def __new__(cls,name, number_of_floors,*args,**kwargs):
        new_house = super().__new__(cls)
        new_house.name = name
        new_house.number_of_floors = number_of_floors
        cls.houses_history.append(name)
        return new_house

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


    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
