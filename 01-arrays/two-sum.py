def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return[]
print(twosum([1,3,4,7],12))
            

    