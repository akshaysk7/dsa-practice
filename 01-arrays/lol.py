d = {"a": [1,2], "b": [3]}
print(d.values())
count = {1: 3, 2: 2, 3: 1}
print(count.items())
sortd=sorted(count.items(),key=lambda x: x[1],reverse=True)
print(sortd)
source=sortd[:k]
topk=[]
for i in source:
    topk.append(i[0])
print(topk)