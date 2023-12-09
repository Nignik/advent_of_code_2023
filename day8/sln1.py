with open("input.txt") as fi:
    f = fi.readlines()

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


insts = []
network = {}

for i in range(len(f)):
    if i == 0:
        insts = list(f[i].strip())

    elif i == 1:
        pass

    else:
        current_node = f[i].split('=')[0].strip()
        next_nodes = f[i].split('=')[1].strip()
        left_node = next_nodes.split(',')[0][1:]
        right_node = next_nodes.split(',')[1][1:-1]

        network[current_node] = Node(left_node, right_node)

current_node = 'AAA'
steps_cnt = 0
cont = True

while cont:
    for inst in insts:
        print(current_node)
        steps_cnt += 1
        if inst == 'L':
            current_node = network[current_node].left

        elif inst == 'R':
            current_node = network[current_node].right

        if current_node == 'ZZZ':
            cont = False
            break

print(steps_cnt)
