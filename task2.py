'''

Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, 
а некоторые – гербом. 
Определите минимальное число монеток, 
которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть

'''

n = int(input())
a = 0
b = 0
for i in range(n):
    x = int(input())
    if x == 0:
        a += 1
    else:
        b += 1
if a > b:
    print(a)
else:
    print(b)