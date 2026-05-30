nums=[1,2,3,3,3,3,4,4,5,5,5,6,7,8,9,11,12,34,44,44,44]
seen=set()
unique=set()
k=0
for number in nums:
    if number not in seen:
        unique.add(number)
        k+=1
        seen.add(number)
    
        
nums =unique
print(nums,k)



    





















