# class Animal:
#     def __init__(self, name):
#         self.alive = True
#         self.fed = False
#         self.name = name
#
# class Plant:
#     def __init__(self, name):
#         self.edible = False
#         self.name = name
#
# class Mammal(Animal):
#     def eat(self, food):
#         if isinstance(food, Plant) and food.edible:
#             print(f"{self.name} съел {food.name}")
#             self.fed = True
#         else:
#             print(f"{self.name} не стал есть {food.name}")
#             self.alive = False
#
# class Predator(Animal):
#     def eat(self, food):
#         if isinstance(food, Plant) and food.edible:
#             print(f"{self.name} съел {food.name}")
#             self.fed = True
#         else:
#             print(f"{self.name} не стал есть {food.name}")
#             self.alive = False
# class Flower(Plant):
#     pass
#
# class Fruit(Plant):
#     def __init__(self, name):
#        super().__init__(name)
#        self.edible = True

class Animal:
    alive = True  # Атрибут класса
    fed = False  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.__class__.fed = True #изменение атрибута класса
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.__class__.alive = False #изменение атрибута класса


class Plant:
    edible = False  # Атрибут класса

    def __init__(self, name):
        self.name = name  # Атрибут экземпляра


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределение атрибута для экземпляра




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
