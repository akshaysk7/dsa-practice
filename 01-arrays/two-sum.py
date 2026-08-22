def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return[]
print(twosum([1,3,4,7],11))
            

#dictionary version o(n) complexity
def twosum(nums,target):
    dict1={}
    for i , num in enumerate(nums):
        if target-num in dict1:
            return [dict1[target-num],i]
        dict1[num]=i
    return[]
print(twosum([1,3,4,7],11))
