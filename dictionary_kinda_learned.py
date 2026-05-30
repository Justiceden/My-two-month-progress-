

nums = [1, 2, 3, 1]
k = 3
seen={}
for i,n in enumerate(nums):
    if n not in seen: 
        seen[n]= i
    elif abs(i-seen[n]) <=k:
        print("True") 
    else:
        print("False")
























