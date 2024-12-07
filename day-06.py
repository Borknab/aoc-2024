f = open("input-06.txt", "r")
maze = []
for line in f: maze.append(line.strip())
rows = len(maze)
cols = len(maze[0])
cur_pos, start_pos = None, None

for i in range(rows):
    for j in range(cols):
        if maze[j][i] == "^": 
            cur_pos = (j, i)
            start_pos = (j, i)

def move(pos, dir):
    if dir == 0: return (pos[0] - 1, pos[1])
    elif dir == 1: return (pos[0], pos[1] + 1)
    elif dir == 2: return (pos[0] + 1, pos[1])
    else: return (pos[0], pos[1] - 1)

cycles = 0
for i in range(rows):
    for j in range(cols):
        if maze[j][i] == ".":
            maze[j] = maze[j][:i] + "#" + maze[j][i + 1:]
            cur_pos = start_pos
            all_pos = set()
            dir = 0 # 0,1,2,3

            while True:
                new_el = (cur_pos[0], cur_pos[1], dir)
                if new_el in all_pos:
                    cycles += 1
                    break
                all_pos.add(new_el)
                prev_pos = cur_pos
                cur_pos = move(cur_pos, dir)
                if cur_pos[0] < 0 or cur_pos[1] < 0 or cur_pos[0] >= rows or cur_pos[1] >= cols:
                    break
                elif maze[cur_pos[0]][cur_pos[1]] == "#":
                    cur_pos = prev_pos
                    dir = (dir + 1) % 4
            maze[j] = maze[j][:i] + "." + maze[j][i + 1:]
        else:
            continue

print(cycles)
