with open("input") as f:
    s = f.readlines()

sum = 0
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in s:
    digits = []
    for idx, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        for idx2, word in enumerate(words):
            if line[idx:].startswith(word):
                digits.append(idx2 + 1)

    sum += int(str(digits[0]) + str(digits[-1]))

print(sum)
