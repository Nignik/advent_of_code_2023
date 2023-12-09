from collections import defaultdict

with open("input1") as f:
    fi = f.readlines()

sum = 0

star_dict = defaultdict(set)

def check_connection(one, two, three, s, e):
    for k in range(s-1, e+2):
        if one[k] == '*':
            return 1, k
        if two[k] == '*':
            return 2, k
        if three[k] == '*':
            return 3, k
    return False

fi.insert(0, '.' * len(fi[0]))
fi.append('.' * len(fi[0]))

for i in range(1, len(fi)-1):
    fi[i] = '.' + fi[i].strip() + '.'

for i in range(1, len(fi)-1):
    j = 1
    while j < len(fi[i]) - 2:
        num = ""
        start = j
        has_num = False
        while fi[i][j].isdigit() and fi[i][j] != '.':
            has_num = True
            num += fi[i][j]
            if j < len(fi[i]) - 2:
                j += 1
            else:
                break
        end = j-1

        check = check_connection(fi[i-1].strip(), fi[i].strip(), fi[i+1].strip(), start, end)
        if not check:
            pass
        elif check[0] == 1 and has_num:
            star_dict[(i-1, check[1])].add(int(num))
        elif check[0] == 2 and has_num:
            star_dict[(i, check[1])].add(int(num))
        elif check[0] == 3 and has_num:
            star_dict[(i + 1, check[1])].add(int(num))

        j += 1

for value in star_dict.values():
    if len(value) == 2:
        temp = 1
        for i in value:
            temp *= i

        sum += temp

print(sum)