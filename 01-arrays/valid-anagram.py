def isAnagram(s,t):
    if len(s) != len(t):
        return False 
    count1={}
    count2={}
    for ch in s:
        if ch in count1:
            count1[ch]+=1
        else:
            count1[ch]=1
    for ch1 in t:
        if ch1 in count2:
            count2[ch1]+=1
        else:
            count2[ch1]=1
    return count1==count2
print(isAnagram("listen","silent"))
print(isAnagram("rat","car"))
        

