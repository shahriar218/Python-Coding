# create stack
def create_stack():
    stack = []
    return stack

# check empty stack
def check_empty(stack):
    return len(stack) == 0

# push item into stack
def push(stack, item):
    stack.append(item)
    print("one item pushed")

# pop item from stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack_list = create_stack()
push(stack_list, str(1))
push(stack_list, str(2))
push(stack_list, str(3))
print(stack_list)

print("popped item " + pop(stack_list))

print(stack_list)