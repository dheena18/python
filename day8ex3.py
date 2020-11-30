try:
    print(a)
except NameError:
    print("Variable a is not defined")
except:
    print("Something else went wrong")