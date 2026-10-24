#right alphabet pyramid
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()


#invert right alpahbet pyramid
n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()

#half diamond alphabet pyramid
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for r in range(i):
        print(chr(r+64),end="")
    print()
       
  