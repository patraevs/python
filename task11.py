 Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     print(i)
# for i in range(0, 10):
#     print(a[i])
lst = [i+1 for i in a]
print(lst)
