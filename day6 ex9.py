print("choose from the options 1.Add 2.subtract 3.multiply 4.Divide")

select=int(input("enter the number:"))

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if select == 1:
    print(num1,"+",num2,"=",num1+num2)
elif select == 2:
    print(num1,"-",num2,"=",num1-num2)
elif select == 3:
    print(num1, "*", num2, "=", num1*num2)
elif select == 4:
    print(num1,"/",num2,"=",num1//num2)
else:
    print("invalid input")