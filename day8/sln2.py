import math

with open("input.txt") as fi:
    f = fi.readlines()

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


insts = []
current_nodes = []
loops = {}
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
        
        if current_node[-1] == 'A':
            current_nodes.append(current_node)

steps_cnt = 0
cont = True

while cont:
    for inst in insts:
        steps_cnt += 1
        for i in range(len(current_nodes)):
            if inst == 'L':
                current_nodes[i] = network[current_nodes[i]].left

            elif inst == 'R':
                current_nodes[i] = network[current_nodes[i]].right

            if current_nodes[i][-1] == 'Z' and current_nodes[i] not in loops.keys():
                loops[current_nodes[i]] = steps_cnt
            
            print(loops)
            if len(loops) == len(current_nodes):
                nodes_lcm = math.lcm(*loops.values())
                steps_cnt = nodes_lcm
                cont = False
                break

        if not cont:
            break

print(steps_cnt)
