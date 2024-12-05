f = open("input-04.txt", "r")
lines = []
for l in f: lines.append(l.strip())

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

def find_xmas(r, c, dy, dx):
    for i in range(4):
        nr, nc = r + i * dy, c + i * dx
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or lines[nr][nc] != "XMAS"[i]:
            return False
    return True

for r in range(rows):
    for c in range(cols):
        for dy, dx in directions:
            if find_xmas(r, c, dy, dx):
                count += 1

print(count)

# 
# M.S
# .A. 
# M.S 
# 
# S.S
# .A. 
# M.M 
# 
# M.M
# .A. 
# S.S 
# 
# S.M
# .A. 
# S.M
def is_real_xmas(r,c):
    if (r == 0 and c == 0): print(lines[r][c:c+3])
    if lines[r][c] == "M" and lines[r][c +2] == "S" and lines[r + 1][c +1] == "A" and lines[r + 2][c] == "M" and lines[r +2][c +2] == "S":
        return True
    if lines[r][c] == "S" and lines[r][c +2] == "S" and lines[r + 1][c +1] == "A" and lines[r + 2][c] == "M" and lines[r +2][c +2] == "M":
        return True
    if lines[r][c] == "M" and lines[r][c +2] == "M" and lines[r + 1][c +1] == "A" and lines[r + 2][c] == "S" and lines[r +2][c +2] == "S":
        return True
    if lines[r][c] == "S" and lines[r][c +2] == "M" and lines[r + 1][c +1] == "A" and lines[r + 2][c] == "S" and lines[r +2][c +2] == "M":
        return True
    return False

real_xmas = 0
for r in range(rows):
    for c in range(cols):
        if r + 2 < rows and c + 2 < cols:
            if is_real_xmas(r,c):
                real_xmas += 1
print(real_xmas)

