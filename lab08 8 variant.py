import array
import random
import math

# Введення кількості елементів масиву
n = int(input("Введіть кількість елементів масиву: "))

# Створення масиву з випадкових чисел у діапазоні [0;10]
arr = array.array('i', [random.randint(0, 10) for _ in range(n)])

# Виведення масиву
print("Згенерований масив:", arr)

# Фільтрація парних елементів
even_numbers = [x for x in arr if x % 2 == 0]

# Обчислення середнього геометричного для парних елементів
if even_numbers:
    geometric_mean = math.prod(even_numbers) ** (1 / len(even_numbers))
    print(f"Середнє геометричне парних елементів: {geometric_mean:.2f}")
else:
    print("У масиві немає парних елементів.")
import numpy as np

# Введення розмірів масивів
M = int(input("Введіть кількість рядків (M): "))
N = int(input("Введіть кількість стовпців (N): "))

# Створення масивів A та B з випадкових чисел
A = np.random.randint(1, 31, size=(M, N))
B = np.random.randint(31, 51, size=(M, N))

# Додавання масивів A і B для отримання масиву C
C = A + B

# Виведення масивів A, B і C
print("Масив A:\n", A)
print("Масив B:\n", B)
print("Масив C (A + B):\n", C)

# Пошук стовпця з найменшою сумою елементів
column_sums = np.sum(C, axis=0)
min_sum_column = np.argmin(column_sums)

print(f"Стовпчик з найменшою сумою елементів: {min_sum_column + 1}")
print(f"Сума елементів цього стовпця: {column_sums[min_sum_column]}")
