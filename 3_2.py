# Без использования collections, написать программу, которая будет создавать словарь для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры
text = input ('text: ')
counter = {i: text.count(i) for i in set(text)}
print (counter)