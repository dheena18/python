try:
    a=input("please enter an integer:")
    a=int(a)
    print("it is an integer")
except ValueError:
    print("Not a valid integer")