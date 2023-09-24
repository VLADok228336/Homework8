print("Enter three numbers")
nums = []
for i in range(3):
    nums.append(int(input()))
nums.sort()
print(nums[1])