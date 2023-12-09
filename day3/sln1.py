with open("input1") as f:
    fi = f.readlines()

sum = 0

def check_connection(one, two, three, s, e):
    for k in range(s-1, e+2):
        if not one[k].isdigit() and one[k] != '.':
            return True
        if not two[k].isdigit() and two[k] != '.':
            return True
        if not three[k].isdigit() and three[k] != '.':
            return True
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

        if check_connection(fi[i-1].strip(), fi[i].strip(), fi[i+1].strip(), start, end) and has_num:
            sum += int(num)

        j += 1


print(sum)