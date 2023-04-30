stack = []


size= int(input("Enter the size of the stack"))
i=size

while(size>0):
    stack.append(input("Enter to the stack"))
    size=size-1

print(stack)

while(i>0):
    print(stack.pop())
    i=i-1

print(stack)