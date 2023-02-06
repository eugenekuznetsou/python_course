# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
digit1 = int(input('Input 1st digit: ')) # где динамическая типизация? без int не работает.
digit2 = int(input('Input 2nd digit: '))
digit3 = int(input('Input 3rd digit: '))
avg_digit = ((digit1+digit2+digit3)/3)
print(round(avg_digit,3))
