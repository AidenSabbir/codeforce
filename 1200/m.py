nums = [1,2,4,6]
res = [1]*(len(nums))

for i in range(len(nums)-1):
  res[i] *= nums[i+1]
for i in range(len(nums)-1,-1,-1):
  res[i] *= nums[i]
print(res)