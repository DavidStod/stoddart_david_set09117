MyStack = []
StackSize = 3
def DisplayStack():
    print("Stack currently contains:")
    for Item in MyStack:
        print(Item)
def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is full")
def Pop():
    if len(MyStack) > 0:
        MyStack.pop()
    else:
        print("Stack is empty")
first = raw_input("What to store first ")
bfirst = first[::-1]
Push(bfirst)
Push(2)
Push(3)
DisplayStack()
raw_input("Press any key to continue...")
Push(4)
DisplayStack()
raw_input("Press any key to continue...")
Pop()
DisplayStack()
raw_input("Press any key to continue...")
Pop()
Pop()
Pop()
DisplayStack()
raw_input("We done here")
