f = open("input-05.txt", "r")
rules = set()

while True:
  line = f.readline()
  if line == "\n": break
  sp = line.split("|")
  rules.add((int(sp[0]), int(sp[1])))

moves = []
for line in f:
  moves.append([int(x) for x in line.split(",")])

res = 0
for m in moves:
  line_valid = True
  initially_incorrect = False
  iter = 0
  while True:
    if iter == 1000: 
      if line_valid and initially_incorrect: res += m[len(m) // 2]
      break
    for i in range(0, len(m) - 1):
      if(m[i], m[i + 1]) not in rules:
        initially_incorrect = True
        if (m[i + 1], m[i]) in rules:
          m[i], m[i + 1] = m[i + 1], m[i]
        else:
          line_valid = False
    iter += 1

print(res)