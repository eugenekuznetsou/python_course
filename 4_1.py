# Вывести первые N цисел кратные M и больше K
n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))

some_list = [i for i in range(k, 1000000) if i % m == 0]
print(some_list[1:n + 1])

