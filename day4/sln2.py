with open("input") as f:
    fi = f.readlines()

ans = 0

copies = [1 for i in range(len(fi))]

for idx, line in enumerate(fi):
    line_copy = line
    while copies[idx] > 0:
        copies[idx] -= 1
        line_copy = line.split(":")[1]

        winning = line_copy.split("|")[0]
        winning = winning.split(" ")
        i = 0
        while i < len(winning):
            winning[i] = winning[i].strip()
            if winning[i] == '':
                winning.pop(i)
            else:
                i += 1


        chosen = line_copy.split("|")[1]
        chosen = chosen.split(" ")
        i = 0
        while i < len(chosen):
            chosen[i] = chosen[i].strip()
            if chosen[i] == '':
                chosen.pop(i)
            else:
                i += 1

        cnt_matches = 1
        for num in chosen:
            if num in winning:
                copies[idx + cnt_matches] += 1
                cnt_matches += 1
                ans += 1


print(ans + len(fi))
