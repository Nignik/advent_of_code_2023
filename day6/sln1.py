with open("input.txt") as fi:
    f = fi.readlines()

ans = 1

times = f[0].split(":")[1]
times = times.split(" ")
temp_times = times.copy()
times = []
for i in range(len(temp_times)):
    if temp_times[i].strip() != "":
        times.append(temp_times[i])

records = f[1].split(":")[1]
records = records.split(" ")
temp_records = records.copy()
records = []
for i in range(len(temp_records)):
    if temp_records[i].strip() != "":
        records.append(temp_records[i])

for i in range(len(times)):
    time = int(times[i])
    record = int(records[i])

    cnt = 0
    for i in range(time):
        distance = i * (time - i)
        if distance > record:
            cnt += 1

    ans *= cnt

print(ans)
