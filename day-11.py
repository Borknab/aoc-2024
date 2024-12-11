from collections import defaultdict

f = open("input-11.txt", "r")
nums = defaultdict(int)
for x in f.readlines()[0].strip().split(" "):
    nums[int(x)] += 1

blinks = 0
while blinks < 75:
    new_nums = nums.copy()
    for v in nums.keys():
        if v == 0 and nums[v] != 0:
            temp = nums[0]
            new_nums[0] -= temp
            new_nums[1] += temp
        elif len(str(v)) % 2 == 0 and nums[v] != 0:
            str_num = str(v)
            mid = len(str_num) // 2
            part_one, part_two = int(str_num[:mid]), int(str_num[mid:])
            temp = nums[v]
            new_nums[v] -= temp
            new_nums[part_one] += temp
            new_nums[part_two] += temp
        elif nums[v] != 0:
            temp = nums[v]
            new_nums[v] -= temp
            new_nums[v * 2024] += temp
    for k in new_nums.keys():
        nums[k] = new_nums[k]
    blinks += 1

ans = 0
for k in nums.keys():
    ans += nums[k]
print(ans)
