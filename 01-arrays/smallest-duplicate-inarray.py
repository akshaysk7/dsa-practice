def smallestduplicatevalue(a):
    dups=set()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                dups.add(a[i])
    smallest=None
    for v in dups:
        if smallest==None or v<smallest:
            smallest=v
    return(smallest)

                

#set version
def smallestduplicatevalue(a):
    seen=set()
    for i in a:
        if i in seen:
            smallest==None or i<smallest
            smallest=i
        seen.add(i)
    return(smallest)
print(smallestduplicatevalue([1,2,4,5,2,3,3]))

