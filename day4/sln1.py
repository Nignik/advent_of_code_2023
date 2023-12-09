with open("test") as f:
    fi = f.readlines()

ans = 0

for line in fi:
    line = line.split(":")[1]

    winning = line.split("|")[0]
    winning = winning.split(" ")
    i = 0
    while i < len(winning):
        winning[i] = winning[i].strip()
        if winning[i] == '':
            winning.pop(i)
        else:
            i += 1


    chosen = line.split("|")[1]
    chosen = chosen.split(" ")
    i = 0
    while i < len(chosen):
        chosen[i] = chosen[i].strip()
        if chosen[i] == '':
            chosen.pop(i)
        else:
            i += 1

    score = 2
    cnt_matches = 0
    for num in chosen:
        if num in winning:
            score = 2 ** cnt_matches
            cnt_matches += 1

    if cnt_matches > 0:
        ans += score


print(ans)
