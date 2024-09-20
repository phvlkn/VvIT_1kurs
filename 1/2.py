def greet(name):
    print(f"Привет, {name}")


def square(num):
    return num**2


def max_of_two(x, y):
    if x >= y:
        return x
    else:
        return y


def describe_person(name, age=30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")


def is_prime(num):
    for i in range(2, num):
        if n % i == 0:
            return False
    return True


print("Задание 1")
greet(input("Как вас зовут?"))
n = int(input("Введите число:"))
print(f"Квадрат:{square(n)}")
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print(f"Большее число: {max_of_two(a, b)}")

print("Задание 2")
name = input("Введите имя:")
age = int(input("Введите возраст:"))
describe_person(name, age)
n = int(input("Введите число:"))
if is_prime(n):
    print("Число простое")
else:
    print("Число составное")