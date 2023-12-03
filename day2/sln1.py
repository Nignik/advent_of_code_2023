
def find_occurrences(s, char):
    return [i for i, c in enumerate(s) if c == char]

with open("input1") as f:
    games = f.readlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum = 0

for nr, line in enumerate(games):
    valid = True
    line = line[8:]
    semis = line.split(";")

    for semi in semis:
        idx = 0
        while idx < len(semi):
            if semi[idx].isdigit():
                number = ""
                while semi[idx].isdigit():
                    number += semi[idx]
                    idx += 1

                color = ""
                idx += 1
                while idx < len(semi) and semi[idx] != ',':
                    color += semi[idx]
                    idx += 1
                if bag[color.strip()] < int(number):
                    valid = False
            idx += 1

    if valid:
        sum += nr + 1

print(sum)
