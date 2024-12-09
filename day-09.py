f = open("input-09.txt", "r")
mem = ""
for line in f: mem += line.strip()

new_mem = []
indices = {}
indices_cur = 0

for i in range(len(mem)):
    if i % 2 == 0:
        for j in range(int(mem[i])): new_mem.append(indices_cur)
        indices[indices_cur] = mem[i]
        indices_cur += 1
    else:
        for j in range(int(mem[i])): new_mem.append(".")

def find_window(from_idx, till_idx):
    cur_id = -1
    i = from_idx
    window_id, window_start_idx, window_end_idx = None, None, None

    while i > till_idx:
        if new_mem[i] != ".":
            cur_id = new_mem[i]
            k = i
            while new_mem[k] == cur_id:
                window_end_idx = k
                k -= 1
            window_id = cur_id
            window_start_idx = window_end_idx
            window_end_idx = i
            break
        i -= 1

    return window_id, window_start_idx, window_end_idx

# keep finding windows, overwriting locations
search_from, search_till = len(new_mem) - 1, 0
x = 0
while True:
    # Large enough to get the right answer
    if x == 20000: break
    window_id, start_idx, end_idx = find_window(search_from, search_till)
    window_size = end_idx - start_idx + 1
    for j in range(0, start_idx):
        if j == start_idx - 1:
            search_from = j
            break
        elif new_mem[j] == ".":
            st, e = j,j
            k = j
            cur_len = 0
            while new_mem[k] == "." and cur_len < window_size:
                e = k
                k += 1
                cur_len += 1
            if cur_len == window_size:
                for k in range(st, e + 1): new_mem[k] = window_id
                for k2 in range(start_idx, end_idx + 1): new_mem[k2] = "."
                search_from = start_idx
                break
    x += 1

res = 0
for i in range(len(new_mem)):
    if new_mem[i] != ".":
        res += int(new_mem[i]) * i

print(res)
