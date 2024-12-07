f = open("input-07-1.txt", "r")
m = []

for line in f:
    [goal, nums] = line.split(":")
    nums = [int(x.strip()) for x in nums.split(" ") if x != '']
    m.append([int(goal.strip()), nums])

valid_goals = set()
def recurse(goal, nums, nums_idx, idx, cur_res, operation):
    if cur_res == goal and idx == len(nums): 
        valid_goals.add((goal, nums_idx))
        return
    if idx >= len(nums): return

    new_res = None
    if operation == "||": new_res = int(f"{cur_res}{nums[idx]}")
    if operation == "*": new_res = cur_res * nums[idx]
    if operation == "+": new_res = cur_res + nums[idx]

    recurse(goal, nums, nums_idx, idx + 1, new_res, "||")
    recurse(goal, nums, nums_idx, idx + 1, new_res, "+")
    recurse(goal, nums, nums_idx, idx + 1, new_res, "*")

nums_idx = 0
for [goal, nums] in  m:
    recurse(goal, nums, nums_idx, 0, 1, "*")
    nums_idx += 1

res = 0
for (x, _) in valid_goals:
    res += x
print(res)

