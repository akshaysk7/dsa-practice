n=int(input("enter a number"))
for i in (range(n,0,-1)):
    for j in range(i):
        print("*",end=" ")
    print()