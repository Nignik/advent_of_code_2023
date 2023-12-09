with open("input.txt") as fi:
    f = fi.read().split("\n\n")

seeds = []

entries = []
for entry in f:
    entries.append(entry.split(":")[1])

for idx, entry in enumerate(entries):
    if idx == 0:
        entry = entry.split(' ')
        entry = [item for item in entry if item != '']
        for i in entry:
            seeds.append(int(i))

    else:
        entry = entry.split("\n")
        entry = [item for item in entry if item != '']

        change = {}
        
        for items in entry:
            items = items.split(' ')
            items[0] = int(items[0])
            items[1] = int(items[1])
            items[2] = int(items[2])

            for i in range(len(seeds)):
                if items[1]  <= seeds[i] < items[1] + items[2]:
                    change[i] = items[0] - items[1]

        for x in change.keys():
            seeds[x] += change[x]

print(min(seeds))
