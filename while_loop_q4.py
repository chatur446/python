# print element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

i = 1
while i<=10:
    print(i*i)
    i+=1
# or
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
