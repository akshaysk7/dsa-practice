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



       
