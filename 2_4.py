# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
# как написать без if?
count_p = 0
count_n = 0
digit1 = int(input('Input 1st digit: '))
digit2 = int(input('Input 2nd digit: '))
digit3 = int(input('Input 3rd digit: '))
if digit1 >= 0: count_p = count_p+1
else: count_n = count_n+1
if digit2 >= 0: count_p = count_p+1
else: count_n = count_n+1
if digit3 >= 0: count_p = count_p+1
else: count_n = count_n+1
print(f'count of positive digits is {count_p}, count of negative digits is {count_n}')