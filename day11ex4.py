numbers= [1, 2, 4, 5, 7, 8, 10, 11]
def filterOddNum(num):
    if(num % 2) == 0:
        return False
    else:
        return True
oddfilter = filter(filterOddNum, numbers)

print("The odd numbers in the list are: ", list(oddfilter))