def topKFrequent(nums,k):
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    sortd=(sorted(count.items(),key=lambda x: x[1],reverse=True))
    source=sortd[:k]
    topk=[]
    for j in source:
        topk.append(j[0])
    return(topk)
print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))
    



