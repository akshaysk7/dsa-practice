n=int(input("enter a number:"))
for i in range(n,0,-1):
    for s in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()