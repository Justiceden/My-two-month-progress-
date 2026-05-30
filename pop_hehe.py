nums = [2,7,11,15]
target = 9
nums.sort()
seen=set()
needed=[]
result=[]
for n in nums:
    if n in seen:
        continue 
    needed= target-n
    seen.add(n)
    if needed in nums:
        result.append((needed,n))
      
     
print(result)    



)




















