f = open("input-08.txt", "r")
m = [line.strip() for line in f]

def find_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    points = []
    for i in range(1, 500):
        antinode1_x = x1 - i * dx
        antinode1_y = y1 - i * dy
        points.append((antinode1_x, antinode1_y))
        
        antinode2_x = x2 + i * dx
        antinode2_y = y2 + i * dy
        points.append((antinode2_x, antinode2_y))
    
    return points

def within_bounds(p):
    x, y = p
    return x < len(m) and x >= 0 and y < len(m[0]) and y >= 0

locs = {}
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != ".":
            key = m[i][j]
            if key not in locs: locs[key] = [(i,j)]
            else: locs[key].append((i,j))

antinodes = set()
cnt = 0

for antenna in locs.keys():
    a_locs = locs[antenna]
    for i in range(len(a_locs) - 1):
        for j in range(i + 1, len(a_locs)):
            points = find_antinodes(a_locs[i], a_locs[j])
            for p in points:
                if within_bounds(p): antinodes.add(p)
            cnt += 1
            antinodes.add(a_locs[i])
            antinodes.add(a_locs[j])

print(len(antinodes))