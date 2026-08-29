def encode(strs):
    s=""
    for st in strs:
        s= s + str(len(st))+"#"+ st
    return s
def decode(s):
    res=[]
    i=0
    while i<len(s):
       j = s.find("#",i)
       length=int(s[i:j])
       strngs=s[j+1:j+1+length]
       res.append(strngs)
       i=j+1+length



            
        

print(encode(["hello","my","name","is","akshay"]))
        


    
