# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#    *Пример:*
#    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число n: '))
nums = []
product = 1

for i in range(1, n + 1, 1):
    nums.append(i)
print(nums)
i = 0
while i < len(nums):
    product *= nums[i]
    print(product)
    i += 1