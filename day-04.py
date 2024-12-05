f = open("input-04.txt", "r")
lines = []
for l in f: lines.append(l.strip())

word = "XMAS"
rows = len(lines)
cols = len(lines[0])
count = 0

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1), 
    (-1, 1), 
    (1, -1),
    (1, 1) 
]

def find_word(r, c, dy, dx):
    for i in range(4):
        nr, nc = r + i * dy, c + i * dx
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or lines[nr][nc] != word[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        for dy, dx in directions:
            if find_word(r, c, dy, dx):
                count += 1

print(count)