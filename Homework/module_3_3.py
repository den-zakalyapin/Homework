def print_params(a = 1, b = 'строка', c = True):
    print(f"a = {a}, b = {b}, c = {c}")
print_params()
print_params(2)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(3, 'new string', False)

values_list = [4, 'another string', False]
values_dict = {'a': 5, 'b': 'yet another string', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
