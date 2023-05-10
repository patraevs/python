#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4
#
# #Введите  массу тела
# >1
#
# Ответ: 1000 кг

a=input("Введите единицу массы тела")
b=input("Введите  массу тела")
match a :
    case "1":
        print(b)
    case "2":
        print(int(b)*(10**-6))
    case "3":
        print(int(b)*(10**-3))
    case "4":
        print(int(b) * (10 ** 3))
    case "5":
        print(int(b) * (10 ** 2))