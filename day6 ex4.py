num=int(input('Enter a number'))
n=num
def arm(num):
    sum1=0
    num2=num
    cnt=0
    while(num>0):
        cnt=cnt+1
        num=num/10
    while(num2>0):
        rem=num2%10
        sum1+=rem**cnt
        num2/=10
    return sum1
sum_1=arm(num)
if(n==sum_1):
    print('the number is an armstrong')
else:
    print('the number is not an armstrong')