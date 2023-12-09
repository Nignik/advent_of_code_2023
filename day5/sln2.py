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
        i = 0
        while i < len(entry) - 1:
            seeds.append((int(entry[i]), int(entry[i]) + int(entry[i+1]) - 1))
            i += 2
        seeds.sort()
        print(seeds)

    else:
        entry = entry.split("\n")
        entry = [item for item in entry if item != '']

        to_erase = set()
        to_append = []
        
        for items in entry:
            items = items.split(' ')
            items[0] = int(items[0])
            start = int(items[1])
            end = int(items[1]) + int(items[2]) - 1
            
            i = 0
            while i < len(seeds):
                if seeds[i] == (-1, -1):
                    i += 1
                    continue

                diff = items[0] - start
                
                #print(f"{start} < {seeds[i][0]} and {end} >= {seeds[i][1]}")
                if start <= seeds[i][0] and end >= seeds[i][1]:
                    to_append.append((seeds[i][0] + diff, seeds[i][1] + diff))
                    seeds[i] = (-1, -1)

                elif start <= seeds[i][0] and seeds[i][0] < end < seeds[i][1]:
                    #to_append.append((end + 1, seeds[i][1]))
                    seeds.append((end + 1, seeds[i][1]))
                    to_append.append((seeds[i][0] + diff, end + diff))
                    seeds[i] = (-1, -1)

                elif seeds[i][0] < start < seeds[i][1] and end >= seeds[i][1]:
                    #to_append.append((seeds[i][0], start - 1))
                    seeds.append((seeds[i][0], start - 1))
                    to_append.append((start + diff, seeds[i][1] + diff))
                    seeds[i] = (-1, -1)

                elif seeds[i][0] < start < seeds[i][1] and seeds[i][0] < end < seeds[i][1]:
                    #to_append.append((seeds[i][0], start - 1))
                    #to_append.append((end + 1, seeds[i][1]))
                    seeds.append((seeds[i][0], start - 1))
                    seeds.append((end + 1, seeds[i][1]))
                    to_append.append((start + diff, end + diff))
                    seeds[i] = (-1, -1)

 #               print(f"{idx}, {items}, {seeds[i]}: {seeds}")
                i += 1

        for delete_element in to_erase:
            seeds[delete_element] = (-1, -1)

        new_seeds = set()
        for seed in seeds:
            if seed != (-1, -1):
                new_seeds.add(seed)
        
        for new_element in to_append:
            new_seeds.add(new_element)

        seeds = list(new_seeds.copy())

        if idx < 30:
            print(f"{idx}: {seeds}")

print(min(seeds, key=lambda x: x[0]))

