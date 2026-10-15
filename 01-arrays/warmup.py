def smallestduplicatevalue(a):
    dup_values=set()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                dup_values.add(a[i])
    smallest=None
    for v in dup_values:
        if smallest==None or v<smallest:
            smallest=v
    return(smallest)
print(smallestduplicatevalue([1,2,4,5,2,3,3]))



        
                


