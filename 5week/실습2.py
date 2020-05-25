def avgn(*args):
    sum = 0
    for i in args:
        sum += i

    return sum / len(args)


print(avgn(1, 1, 1, 1, 1, 1, 1))
print(avgn(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
