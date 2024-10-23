
def get_multiplied_digits(number):
     str_number = str(number)
     if len(str_number) < 2:
         if number == 0:
             return 1
         else :
             return number
     first = int(str_number[0])
     tail = int(str_number[1:])
     return first * get_multiplied_digits(tail)


result = get_multiplied_digits(40203)
print(result)

