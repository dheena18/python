first = float(input("first number:"))
second = float(input("Second number:"))
print("1.add 2.sub 3.multiply 4.division")
try:
    operator=int(input("Option:"))
    if operator==1:
        print(first+second)
    elif operator==2:
        print(first-second)
    elif operator == 3:
        print(first*second)
    elif operator == 4:
        print(first/second)
    else:
        print("Enter a valid integer")
except NameError:
    print("Please use number only")
except SyntaxError:
    print("Please use number only")
except TypeError:
    print("Please use number only")
except AttributeError:
    print("Please use number only")
except ValueError:
    print("Please use number only")