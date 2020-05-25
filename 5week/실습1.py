def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


n = int(input())
print(fac(n))
