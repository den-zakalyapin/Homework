my_dict={'Anton':1970,'Max':1971,'Den':1972}
print(my_dict)
my_dict['Alex']=1900
my_dict.update({'Masha':1950,'Tosha':1960})
my_dict['Антон']=2000
print(my_dict)
print(my_dict.pop('Антон'))
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Pasha','Такого ключа нет'))


my_set={22,23,24,25,22,25}
print(my_set)
my_set={21,22,23,'строка',True}
print(my_set.remove(22))
print(my_set.add(88))
print(my_set)

