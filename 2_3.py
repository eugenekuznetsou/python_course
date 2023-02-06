# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name = input('input your name: ')
age = int(input('input your age: '))
city = input('input your city: ')
print("Hello %s! You are %d, and you from %s!" % (name, age, city))
print("Hello {}! You are {}, and you from {}!".format(name,age,city))
print(f"Hello {name}! You are {age}, and you from {city}!")
