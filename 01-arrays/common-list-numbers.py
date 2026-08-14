l1=[2,3,2,4,2,5,6,3,6,7,9,8]
l2=[2,2,3,7,8,9,8,7,6,2,5,0]
set_l2=set(l2)
common=set()
for num in l1:
    if num in set_l2:
        common.add(num)
print(common)
