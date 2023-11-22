#stack,queue,deque
#stack
max_stack=5
stack=[0]*max_stack
def init_stack():
    global top
    top=-1
def isEmpty_stack():
    return top==-1
def isFull_stack():
    return top+1==max_stack
def push_stack(e):
    global top,stack
    if isFull_stack():
        print("full")
        return
    top+=1
    stack[top]=e
    print(stack)
def pop_stack():
    global top
    if isEmpty_stack():
        print("empty")
        return
    pop_element=stack[top]
    top-=1
    print(stack)
    return pop_element
def peek_stack():
    if isEmpty_stack():
        print("empty")
        return
    return stack[top]
init_stack()
push_stack(1)
push_stack(2)
push_stack(3)
push_stack(4)
push_stack(5)
push_stack(6)
print(pop_stack(),top)
