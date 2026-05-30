nums = [2,7,11,15]
target = 13
seen={}
result=[]
for n in range(len(nums)):
    needed = target - nums[n]
    if needed in seen:
        print(f"{n} {seen[needed]}")
        
    seen[nums[n]]=n

























