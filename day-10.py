from collections import defaultdict

f = open("input-10.txt", "r")
map = []
for line in f: map.append([int(x) for x in line.strip()])
trails = defaultdict(int)

def traverse_paths(start_coords, i, j, cur_path, prev_num):
    if (i,j) in cur_path: return
    if i >= len(map) or j >= len(map[0]) or i < 0 or j < 0: return

    if map[i][j] - prev_num == 1 and map[i][j] == 9:
        trails[(start_coords[0], start_coords[1])] += 1
    elif map[i][j] - prev_num == 1:
        cur_path.add((i,j))
        traverse_paths(start_coords, i + 1, j, cur_path, map[i][j])
        traverse_paths(start_coords, i - 1, j, cur_path, map[i][j])
        traverse_paths(start_coords, i, j + 1, cur_path, map[i][j])
        traverse_paths(start_coords, i, j - 1, cur_path, map[i][j])
        cur_path.remove((i,j))

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            cur_path = set()
            traverse_paths((i,j), i, j, cur_path, -1)

print(sum(trails.values()))
