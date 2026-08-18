nums=[1,2,3,4,5]
def has_duplicatenums(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j!=i and nums[j]==nums[i]:
                return(True)
    
    return(False)
print(has_duplicatenums(nums))
    