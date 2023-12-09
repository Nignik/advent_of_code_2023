with open("input.txt") as fi:
    f = fi.readlines()

ans = 0

time = int(''.join(f[0].split(":")[1].split()))
record = int(''.join(f[1].split(":")[1].split()))

for i in range(time):
    if i * (time - i) > record:
        ans += 1

print(ans)
