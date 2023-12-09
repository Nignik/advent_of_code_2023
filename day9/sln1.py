with open("input.txt") as fi:
    f = fi.readlines()

ans = 0

for line in f:
    line.strip()
    line = line.split(' ')
    diffs = []
    cont = True
    temp = [int(x) for x in line]
    diffs.append(temp)
    while cont:
        level = []
        cont = False
        for i in range(1, len(line)):
            diff = int(line[i]) - int(line[i-1])
            level.append(diff)
            if diff != 0:
                cont = True
        
        line = level
        diffs.append(level)

    diffs.reverse()
    for i in range(1, len(diffs)):
        diffs[i].append(diffs[i-1][-1] + diffs[i][-1])
    
    print(diffs)
    ans += diffs[-1][-1]
    
print(ans)

