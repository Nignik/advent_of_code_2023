with open("input.txt") as fi:
    f = fi.readlines()

value_map = { '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8,
        'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13 }

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

def sort_hands(s):
    return [value_map.get(char, float('inf')) for char in s]

hands = []
bids = []

for line in f:
    hands.append(line.split(" ")[0])
    bids.append(line.split(" ")[1])

bids_map = {}
for i in range(len(bids)):
    bids_map[hands[i]] = int(bids[i])

for i in range (len(hands)):
    hand = sorted(list(hands[i])).copy()
    cnt = 1
    max_cnt = 0
    for j in range(1, len(hand)):
        if hand[j] == hand[j-1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1

    max_cnt = max(max_cnt, cnt)
    diff_size = len(set(hand))
    if diff_size == 1:
        five_of_kind.append(hands[i])
    
    elif diff_size == 2 and max_cnt == 4:
        four_of_kind.append(hands[i])
    
    elif diff_size == 2 and max_cnt == 3:
        full_house.append(hands[i])

    elif diff_size == 3 and max_cnt == 3:
        three_of_kind.append(hands[i])

    elif diff_size == 3 and max_cnt == 2:
        two_pair.append(hands[i])

    elif diff_size == 4:
        one_pair.append(hands[i])

    elif diff_size == 5:
        high_card.append(hands[i])

rank = 1
hand_mapping = {}

for hand_type in [high_card, one_pair, two_pair, three_of_kind, full_house, four_of_kind, five_of_kind]:
    for x in sorted(hand_type, key=sort_hands):
        hand_mapping[x] = rank
        rank += 1

ans = 0

for key, value in hand_mapping.items():
    print(f"rank: {value}, hand: {key}, bid: {bids_map[key]}")
    ans += value * bids_map[key]

print(ans)
