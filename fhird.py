import math
def one():
    print("Алгоритм со сложностью 1:")
    a = list(map(int, input().split()))
    print(a[0])
    print("1 - сложность алгоритма")
def two():
    print("Алгоритм со сложностью log(n):")
    n = int(input())
    sum = 0
    for i in range(int(math.log(n, 2))):
        sum += 1
    print(sum, "- сложность алгоритма")
def three():
    print("Алгоритм со сложностью n^2:")
    n = int(input())
    sum = 0
    for i in range(n ** 2):
        sum += 1
    print(sum, "- сложность алгоритма")
def four():
    print("Алгоритм со сложностью 2^n:")
    n = int(input())
    sum = 0
    for i in range(2 ** n):
        sum += 1
    print(sum, "- сложность алгоритма")
one()
two()
three()
four()