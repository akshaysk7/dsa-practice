#reversing a list 
l = [1, 2, 3, 4, 5]
reversed_l = []
for num in l:
    reversed_l.insert(0, num)
print(reversed_l)

#reversing a string using stack[the string is sent into a list by appending it into the stack[] and then a reverse
#  list is defined and the stack is poped(lifo cuz stack top element comes out first) and sent into the reversed_list]

def reversestring(orginal_string):
    stack=[]
    for ch in orginal_string:
        stack.append(ch)
    reversed_string=""
    while len(stack)>0:
        reversed_string+=stack.pop()
    return reversed_string
print(reversestring("imakshaylmao"))




