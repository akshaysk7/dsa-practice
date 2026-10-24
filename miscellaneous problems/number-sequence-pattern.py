#n=int(input("enter a number:"))
#for i in range(1,n+1):
    #for j in range(1,i+1):
        #print((i+j)%2,end="")
    #print()



n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(2*(n-i)):
        print(" ",end="")
    for r in range(j,0,-1):
        print(r,end="")
    print()

















