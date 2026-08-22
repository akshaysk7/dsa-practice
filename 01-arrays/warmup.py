chcount={}
strng="manchester city is my favourite football club"
for i in strng:
    if i in chcount:
        chcount[i]+=1
    else:
        chcount[i]=1
print(chcount)


