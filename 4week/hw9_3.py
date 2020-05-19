sum = 0

for i in range(1, 10001):
    if i % 3 == 0 or i % 7 == 0 or i % 10 == 0:
        sum += i

print(sum)
