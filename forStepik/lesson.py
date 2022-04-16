# a = int(input("Введите a и b"))
# b = int(input())
# c = a+b
# print(c)
# print('Здравствуй, мир!')
# print('4', '8', '15', '16', '23', '42')
#
#
#
# s = '*'
# for i in range(7):
#     print(s)
#     s = s+'*'
#
# print('*'*100)

# name = input()
# print(name, '- чемпион!')

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# a = int(input())
# print(a, a*2, a*3, a*4, a*5, sep='---')
# print(a, '-', b, '=', a-b)
# print(a, '*', b, '=', a*b)

# Задачка с Таносом - сама неотвратимость!
# a = int(input())
# p = a//2
# o = a - p * 2
# print(p+o)

a, b, c = int(input()), int(input()), input()

if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "*":
    print(a * b)
if c == "/":
    if b == 0:
        print("На ноль делить нельзя!")
    elif a == 0:
        print("0.0")
    else:
        print(a // b)