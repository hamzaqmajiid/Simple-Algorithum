stack = ["hamza","sarib","ahsan"]
input_=input("Push or pop? ")
if input_=="push":
    input2=input("Enter the nme to pop: ")
    stack.append(input2)
    print(stack)
elif input_=="pop":
    stack.pop()
    print(stack)
else:
    print("The worng command is given")