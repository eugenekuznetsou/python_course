# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
# a = int(input('input dec digit: '))


# def dec2bin(a):
#     b = ''
#     while a > 0:
#         b = str(a % 2) + b
#         a = a // 2
#     return b
#
#
# print(dec2bin(a))
# print(bin(a))

# Код Морзе для представления цифр и букв использует тире и точки. Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе. (словари в помощь)



def text2morze():
    morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
             's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    text = input('Input text: ')
    result = []
    for word in text.split():
        #print(word)
        word2 = []
        for i in word:
            word2.append(morze[i])
            #print(word2)
    result.append(' '.join(word2))
    #print(result)
    print('\n'.join(result))
    return result

text2morze()
