nums = [0,1,0,3,12]
result = []
for i in nums:
    if i !=0:
        result.append(i)
zero_count = nums.count(0)
result +=[0]* zero_count
print(result)
