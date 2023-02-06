# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text = input('Input text: ')
print(text.replace(' ','-'))
print('-'.join(text.split(' ')))
