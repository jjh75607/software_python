sum = 0
for year in range(1, 2021):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        sum += 1

print(sum)
