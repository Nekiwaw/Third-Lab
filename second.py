import math
def one():
    print("Алгоритм со сложностью 3*n:")
    n = int(input())
    sum = 0
    for i in range(3 * n):
        sum += 1
    print(sum, "- сложность алгоритма")
def two():
    print("Алгоритм со сложностью n*log(n):")
    sum = 0
    n = int(input())
    for i in range(int(n * math.log(n, 2))):
        sum += 1
    print(sum, "- сложность алгоритма")
def three():
    print("Алгоритм со сложностью n!:")
    n = int(input())
    sum = 0
    for i in range(math.factorial(n)):
        sum += 1
    print(sum, "- сложность алгоритма")
def four():
    print("Алгоритм со сложностью n^3:")
    n = int(input())
    sum = 0
    for i in range(n ** 3):
        sum += 1
    print(sum, "- сложность алгоритма")
def five():
    print("Алгоритм со сложностью 3*log(n):")
    sum = 0
    n = int(input())
    for i in range(int(3 * math.log(n, 2))):
        sum += 1
    print(sum, "- сложность алгоритма")
one()
two()
three()
four()
five()