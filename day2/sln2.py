def find_occurrences(s, char):
    return [i for i, c in enumerate(s) if c == char]

with open("input1") as f:
    games = f.readlines()

sum = 0

for nr, line in enumerate(games):
    bag = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
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
                bag[color.strip()] = max(bag[color.strip()], int(number))
            idx += 1

    sum += bag["red"] * bag["green"] * bag["blue"]

print(sum)