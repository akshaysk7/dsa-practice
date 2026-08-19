nums=[1,2,3,4,5,1,2]
def has_duplicatenums(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j!=i and nums[j]==nums[i]:
                return(True)
    
    return(False)
print(has_duplicatenums(nums))


def has_duplicate_set(nums):
    dup=set()
    for i in nums:
        if i in dup:
            return (True)
        dup.add(i)
    return(False)
print(has_duplicatenums(nums))
print(has_duplicate_set(nums))


