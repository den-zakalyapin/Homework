#immutable_var=1,2,3,'1','2','3','apple'
#print(immutable_var)
#print(type(immutable_var))
#immutable_var[6]= 6
#print(immutable_var)
#immutable_var=1,2,3,['1','2','3'],'apple'
#print(type(immutable_var[3]))#здесь вывели 3 злемент кортежа состоящий из трёх элементов списка
#immutable_var[3]=5
#print(immutable_var)#пишет объект "кортеж" не поддерживает назначение элементов
mutable_list=(1,[2,3],['a','b','v'],'cola')#сдлал в кортеже 3 элемента ,во втором элементе поменял второй по индексу элемент
print(mutable_list)
mutable_list[2][2]='5'
print(mutable_list)


