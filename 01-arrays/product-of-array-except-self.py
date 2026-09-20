def productExceptSelf(nums):
    result=[]
    for i in range(len(nums)):
        product=1
        for j in range(len(nums)):
            if j!=i:
                product*=nums[j]
        result.append(product)
    return(result)
print(productExceptSelf([1,0,4,5]))


#dict version o(n) time complexity
def productExceptSelf(nums):
    result=[]
    product=1
    for i in range(len(nums)):
        result.append(product)
        product*=nums[i]
    product=1
    for j in range(len(nums)-1,-1,-1):
        result[j]*=product
        product*=nums[j]
    return(result)
print(productExceptSelf([1,2,3,4]))





            
            
        

                