#todo: Вводится число, например: 1231.
# Вывести строчку, например: один два три один.
# Подсказка: создайте словарь

conversion = {'1': 'один',
              '2': 'два',
              '3': 'три',
              '4': 'четыре',
              '5': 'пять',
              '6': 'шесть',
              '7': 'семь',
              '8': 'восемь',
              '9': 'девять',
              '0': 'ноль',}

print('Введите число:', end = ' ')
sentence = input()
result = ''
for char in sentence:
    result+=(' ' + conversion[char])
print(result)
