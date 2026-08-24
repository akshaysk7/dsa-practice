def groupAnagram(self,strs):
    groups={}
    for i in strs:
        key="".join(sorted(i))
        if key in groups:
            groups[key].append(i)
        else:
            groups[key]=[i]
    return list(groups.values())
    
print(groupAnagram(["cat","tac","rat","car","silent","listen"]) )
  


    
        
