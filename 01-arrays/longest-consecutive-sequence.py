def longestConsecutive(nums):
    if nums==[]:
        return 0
    sorted_nums=sorted(nums)
    current=1
    best=1
    for i in range(1,len(sorted_nums)):
        num=sorted_nums[i]
        prev=sorted_nums[i-1]
        if num==prev+1:
            current+=1
            if current>best:
                best+=1
        elif num==prev:
            continue
        else:
            current=1
    return(best)
print(longestConsecutive([1,2,3,10,11,12,13]))

##set version
def longestConsecutive(nums):
    nums_set=set()
    best=0
    for i in nums:
        nums_set.add(i)
    for x in nums_set:
        if x-1 in nums_set:
            continue
        s=x
        length=1
        while s+1 in nums_set:
           s=s+1
           length+=1
        if length>best:
            best=length
    return(best)
print(longestConsecutive([1,2,3,10,11,12,13]))

        




       
