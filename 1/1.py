"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list[1] = 100

for i in range(1, 11):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")
"""
print("Задача 1")
n = int(input("Введите число:"))
for i in range(1, n + 1):
    print(i)

print("Задача 2")
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if a >= b:
    print(f"Большее число: {a}")
else:
    print(f"Большее число: {b}")