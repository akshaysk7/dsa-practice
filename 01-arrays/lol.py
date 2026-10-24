n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for r in range(1,i+1):
        print(chr(r+64),end="")
    for c in range(i-1,0,-1):
        print(chr(c+64),end="")
    print()

    
    
        