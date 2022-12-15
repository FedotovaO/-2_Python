# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)

str_number = input('Введите число: ')
numbers = []
summa = 0

for char in str_number:
    if char.isdigit():
        numbers.append(int(char))
i = 0
while i < len(numbers):
    summa += numbers[i]
    i += 1
print(summa)