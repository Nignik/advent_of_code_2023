with open("input") as f:
    s = f.readlines()

sum = 0
for line in s:
    y = [x for x in line if x.isdigit()]
    sum += eval(str(y[0]) + str(y[-1]))

print(sum)
