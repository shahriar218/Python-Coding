# creating a stack
def create_stack():
    stack = []
    return stack

# creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# push item into stack
def push(stack, item):
    stack.append(item)
    print("pushed item " + item)

def popy(stack):
    if (check_empty(stack)):
        print("stack is empty")
    return stack.pop()

stack = create_stack()
print(stack)
print(type(stack))

# push in stack
push(stack, str(1))
print(stack)
push(stack, str(2))
print(stack)
print(len(stack))
print("first item " + stack[0])
print("second item " + stack[1])
push(stack, str(3))
print(stack)
push(stack, str(4))
print(stack)



# pop from stack
popy(stack)

print(stack)

popy(stack)

print(stack)

push(stack, str(3))
print(stack)
push(stack, str(2))
print(stack)